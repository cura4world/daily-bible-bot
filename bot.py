#!/usr/bin/env python3
import os, requests
from datetime import datetime, date, timedelta, timezone
from bible_data import get_flat_chapter_list, get_youversion_link, THRESHOLD_SECONDS

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

# KST = UTC+9 (GitHub Actions는 UTC 기준으로 실행되므로 명시적으로 KST 사용)
KST = timezone(timedelta(hours=9))

# ── 앵커(기준점) ──────────────────────────────────────────────
# START_DATE에 START_BOOK의 START_CHAPTER부터 읽기 시작한다.
# 이후 일정은 앵커부터 하루씩 걸어오며 계산한다:
#   · 월~토: 첫 장이 THRESHOLD_SECONDS 이상이면 2장, 미만이면 3장,
#            단독 1장짜리 책은 1장
#   · 일요일: 딱 1장만 소비 (예배에서 함께 읽는 장)
#   → 월요일은 일요일에 읽은 장의 "다음 장"부터 자동으로 이어진다.
#     (일요일 장이 월요일에 중복되거나 일정이 밀리는 일이 구조적으로 불가능)
# 일정을 옮겨야 할 때는 아래 세 값만 바꾸면 된다.
START_DATE = date(2026, 7, 4)   # 토요일
START_BOOK = "EXO"
START_CHAPTER = 28

def _group_starting_at(flat, i):
    """평일 하루치 묶음 규칙 (bible_data.get_reading_plan과 동일, 성경 전체 순환 지원)."""
    n = len(flat)
    ch = flat[i % n]
    if ch["total_chapters"] == 1:
        return [ch]
    if ch["duration"] >= THRESHOLD_SECONDS:
        nxt = flat[(i + 1) % n]
        if nxt["total_chapters"] > 1:
            return [ch, nxt]
        return [ch]
    day = []
    j = 0
    while j < 3:
        nxt = flat[(i + j) % n]
        if nxt["total_chapters"] == 1 and j > 0:
            break
        day.append(nxt)
        j += 1
    return day

def get_todays_reading(today=None):
    """앵커부터 하루씩 걸어오며 오늘 읽을 장을 계산한다.
    일요일은 정확히 1장만 소비하므로, 월요일은 항상 그 다음 장에서 시작된다."""
    if today is None:
        today = datetime.now(KST).date()
    if (today - START_DATE).days < 0:
        return None, None

    flat = get_flat_chapter_list()
    n = len(flat)
    pos = next(i for i, ch in enumerate(flat)
               if ch["book_code"] == START_BOOK and ch["chapter"] == START_CHAPTER)

    d = START_DATE
    day_count = 0
    while True:
        if d.weekday() == 6:              # 일요일: 1장만
            todays = [flat[pos % n]]
        else:                             # 월~토: 묶음 규칙대로
            todays = _group_starting_at(flat, pos)
            day_count += 1
        if d == today:
            return (todays, None) if d.weekday() == 6 else (todays, day_count)
        pos += len(todays)                # 오늘 읽은 만큼 '정확히' 소비
        d += timedelta(days=1)

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
