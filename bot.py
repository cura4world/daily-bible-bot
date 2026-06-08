#!/usr/bin/env python3
import os, requests
from datetime import datetime, date, timedelta, timezone
from bible_data import get_reading_plan, get_youversion_link

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# KST = UTC+9 (GitHub Actions는 UTC 기준으로 실행되므로 명시적으로 KST 사용)
KST = timezone(timedelta(hours=9))

# 시작일: 2026-05-04 (월) = 베드로전서 2장 (plan[0])
START_DATE = date(2026, 5, 4)
START_INDEX = 0
START_BOOK = "1PE"
START_CHAPTER = 2

def get_todays_reading():
    today = datetime.now(KST).date()  # UTC가 아닌 KST 기준 날짜
    plan = get_reading_plan(START_BOOK, START_CHAPTER)
    days_elapsed = (today - START_DATE).days

    if days_elapsed < 0:
        return None, None  # 시작일 이전

    # 시작일 이후 지나친 일요일 수 (시작일 당일 제외, weekday 기반으로 정확하게 계산)
    sundays_passed = sum(
        1 for i in range(days_elapsed)
        if (START_DATE + timedelta(days=i)).weekday() == 6
    )

    # plan_slot: 일요일 포함 매일 1씩 전진
    plan_slot = START_INDEX + days_elapsed
    if plan_slot >= len(plan):
        plan_slot = plan_slot % len(plan)

    if today.weekday() == 6:
        # 일요일: 다음 순서 첫 장 링크만 발송, day_count 카운트 안 함
        return [plan[plan_slot][0]], None

    # 평일: day_count는 일요일 제외
    day_count = days_elapsed - sundays_passed
    return plan[plan_slot], day_count + 1

def format_chapter_range(chapters):
    if len(chapters) == 1:
        ch = chapters[0]
        return f"{ch['book_name']} pasal {ch['chapter']}"
    books = list(dict.fromkeys(ch["book_name"] for ch in chapters))
    if len(books) == 1:
        nums = [str(ch["chapter"]) for ch in chapters]
        if len(nums) == 2:
            return f"{books[0]} pasal {nums[0]} dan {nums[1]}"
        return f"{books[0]} pasal {', '.join(nums[:-1])}, dan {nums[-1]}"
    parts = [f"{ch['book_name']} pasal {ch['chapter']}" for ch in chapters]
    if len(parts) == 2:
        return f"{parts[0]} dan {parts[1]}"
    return f"{', '.join(parts[:-1])}, dan {parts[-1]}"

def generate_message(chapters, day_number):
    book_range = format_chapter_range(chapters)
    first_ch = chapters[0]
    link = get_youversion_link(first_ch["youversion_book"], first_ch["chapter"])
    g_idx = day_number % 11
    i_idx = day_number % 13
    c_idx = day_number % 17
    greetings = [
        "Shalom, selamat pagi 😊",
        "Selamat pagi yang cerah! 🌞",
        "Selamat pagi, saudara-saudari 🙏",
        "Halo semua, selamat pagi 👋",
        "Tuhan memberkati pagi ini ✨",
        "Pagi yang indah untuk bersyukur 🌿",
        "Salam dalam kasih Tuhan ❤️",
        "Selamat pagi! Kiranya hari ini penuh berkat 🌅",
        "Hai, selamat pagi 😄",
        "Dengan sukacita menyapa kalian pagi ini 🌸",
        "Pagi ini kita mulai dengan firman Tuhan 📚",
    ]
    intros = [
        f"Hari ini kita akan bersama-sama mendengarkan firman Tuhan dari kitab {book_range} 📚",
        f"Bacaan firman kita hari ini adalah {book_range} 📚",
        f"Mari kita dengarkan firman Tuhan hari ini dari {book_range} 📚",
        f"Firman Tuhan untuk kita hari ini diambil dari {book_range} 📚",
        f"Bersama-sama kita mendengarkan {book_range} hari ini 📚",
        f"Hari ini kita membuka {book_range} bersama 📚",
        f"Jadwal bacaan kita hari ini: {book_range} 📚",
        f"Yuk, kita dengarkan {book_range} bersama hari ini 📚",
        f"Firman hari ini dari {book_range} — mari kita simak bersama 📚",
        f"Kita lanjutkan perjalanan firman kita hari ini di {book_range} 📚",
        f"Untuk hari ini, kita membaca {book_range} 📚",
        f"Kiranya {book_range} memberkati kita hari ini 📚",
        f"Dengarkanlah firman Tuhan hari ini dari {book_range} 📚",
    ]
    closings = [
        "Mari kita hidup dalam iman dan ketaatan kepada Tuhan hari ini ❤️",
        "Kiranya firman-Nya menguatkan langkah kita hari ini ❤️",
        "Selamat mendengarkan dan kiranya Tuhan berbicara kepada kita ❤️",
        "Tuhan memberkati dan menguatkan kita semua hari ini ❤️",
        "Mari tetap berjalan bersama Tuhan hari ini ❤️",
        "Semoga firman-Nya menjadi pelita bagi langkah kita ❤️",
        "Kiranya kita semakin mengenal Tuhan melalui firman-Nya ❤️",
        "Selamat beraktivitas, Tuhan menyertai kita ❤️",
        "Jadikan firman ini bekal kita sepanjang hari ❤️",
        "Bersama firman-Nya, kita jalani hari ini dengan penuh syukur ❤️",
        "Kiranya Tuhan membuka hati kita untuk menerima firman-Nya hari ini ❤️",
        "Mari bawa firman ini dalam setiap langkah kita hari ini ❤️",
        "Tuhan beserta kita — selamat mendengarkan firman-Nya ❤️",
        "Semoga firman hari ini menguatkan iman kita bersama ❤️",
        "Dengan firman Tuhan, hari ini kita jalani dengan penuh harapan ❤️",
        "Kiranya Tuhan berbicara kepada hati kita melalui firman-Nya ❤️",
        "Tetap semangat dalam firman Tuhan hari ini ❤️",
    ]
    return f"{link}\n\n{greetings[g_idx]}\n\n{intros[i_idx]}\n\n{closings[c_idx]}"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "disable_web_page_preview": False}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    print("Message sent!")

def main():
    now = datetime.now(KST)
    today = now.date()
    print(f"Running at {now} (KST), today={today} ({today.strftime('%A')})")

    chapters, day_number = get_todays_reading()

    if chapters is None:
        print("Before start date — no message sent.")
        return

    if day_number is None:
        # 일요일: 첫 장 링크만 발송
        first_ch = chapters[0]
        link = get_youversion_link(first_ch["youversion_book"], first_ch["chapter"])
        print(f"Sunday - link only: {first_ch['book_name']} pasal {first_ch['chapter']}")
        print(f"--- Message ---\n{link}\n---")
        send_telegram(link)
        return

    print(f"Day {day_number}: {format_chapter_range(chapters)}")
    message = generate_message(chapters, day_number)
    print(f"--- Message ---\n{message}\n---")
    send_telegram(message)

if __name__ == "__main__":
    main()
