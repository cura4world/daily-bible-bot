#!/usr/bin/env python3
import os, json, requests
from datetime import datetime
from bible_data import get_reading_plan, get_youversion_link

TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
PROGRESS_FILE = "progress.json"
START_BOOK = "HEB"
START_CHAPTER = 13

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"day_index": 0}

def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f)

def get_todays_reading():
    plan = get_reading_plan(START_BOOK, START_CHAPTER)
    progress = load_progress()
    day_index = progress.get("day_index", 0)
    if day_index >= len(plan):
        day_index = 0
    chapters = plan[day_index]
    progress["day_index"] = day_index + 1
    save_progress(progress)
    return chapters, day_index + 1

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
    idx = day_number % 7

    greetings = [
        "Shalom, selamat pagi U0001f60a",
        "Syalom! Selamat pagi U0001f31e",
        "Selamat pagi, saudara-saudari U0001f64f",
        "Halo semua, selamat pagi U0001f44b",
        "Tuhan memberkati pagi ini ✨",
        "Pagi yang indah untuk bersyukur U0001f33f",
        "Salam dalam kasih Tuhan ❤️",
    ]
    intros = [
        f"Hari ini kita akan bersama-sama mendengarkan firman Tuhan dari kitab {book_range} U0001f4d6",
        f"Bacaan firman kita hari ini adalah {book_range} U0001f4d6",
        f"Mari kita dengarkan firman Tuhan hari ini dari {book_range} U0001f4d6",
        f"Firman Tuhan untuk kita hari ini diambil dari {book_range} U0001f4d6",
        f"Bersama-sama kita mendengarkan {book_range} hari ini U0001f4d6",
        f"Hari ini kita membuka {book_range} bersama U0001f4d6",
        f"Jadwal bacaan kita hari ini: {book_range} U0001f4d6",
    ]
    closings = [
        "Mari kita hidup dalam iman dan ketaatan kepada Tuhan hari ini ❤️",
        "Kiranya firman-Nya menguatkan langkah kita hari ini ❤️",
        "Selamat mendengarkan dan kiranya Tuhan berbicara kepada kita ❤️",
        "Tuhan memberkati dan menguatkan kita semua hari ini ❤️",
        "Mari tetap berjalan bersama Tuhan hari ini ❤️",
        "Semoga firman-Nya menjadi pelita bagi langkah kita ❤️",
        "Kiranya kita semakin mengenal Tuhan melalui firman-Nya ❤️",
    ]

    return f"{link}\n\n{greetings[idx]}\n\n{intros[idx]}\n\n{closings[idx]}"

def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "disable_web_page_preview": False}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    print("Message sent!")
    return response.json()

def main():
    print(f"Running at {datetime.now()}")
    chapters, day_number = get_todays_reading()
    print(f"Day {day_number}: {format_chapter_range(chapters)}")
    message = generate_message(chapters, day_number)
    print(f"--- Message ---\n{message}\n---")
    send_telegram(message)

if __name__ == "__main__":
    main()
