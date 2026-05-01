#!/usr/bin/env python3
"""
Daily Bible Listening Bot
- Reads from reading plan (stored in progress.json)
- Generates WhatsApp-ready message via Claude API
- Sends to Telegram
"""

import os
import json
import random
import requests
import anthropic
from datetime import datetime
from bible_data import get_reading_plan, get_youversion_link, BIBLE_CHAPTERS

# ── Config from environment variables ──────────────────────────────────────────
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
ANTHROPIC_API_KEY = os.environ["ANTHROPIC_API_KEY"]

PROGRESS_FILE = "progress.json"
START_BOOK = "HEB"
START_CHAPTER = 13  # Hebrews 13

# ── Progress tracking ──────────────────────────────────────────────────────────
def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"day_index": 0}

def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f)

# ── Reading plan ───────────────────────────────────────────────────────────────
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

# ── YouVersion links ───────────────────────────────────────────────────────────
def build_links(chapters):
    links = []
    for ch in chapters:
        link = get_youversion_link(ch["youversion_book"], ch["chapter"])
        links.append(link)
    return links

def format_chapter_range(chapters):
    if len(chapters) == 1:
        ch = chapters[0]
        return f"{ch['book_name']} pasal {ch['chapter']}"

    books = list(set(ch["book_name"] for ch in chapters))
    if len(books) == 1:
        chapter_nums = [str(ch["chapter"]) for ch in chapters]
        if len(chapter_nums) == 2:
            return f"{books[0]} pasal {chapter_nums[0]} dan {chapter_nums[1]}"
        else:
            return f"{books[0]} pasal {', '.join(chapter_nums[:-1])}, dan {chapter_nums[-1]}"
    else:
        parts = [f"{ch['book_name']} pasal {ch['chapter']}" for ch in chapters]
        if len(parts) == 2:
            return f"{parts[0]} dan {parts[1]}"
        else:
            return f"{', '.join(parts[:-1])}, dan {parts[-1]}"

# ── Message generation via Claude ─────────────────────────────────────────────
def generate_message(chapters, links, day_number):
    book_range = format_chapter_range(chapters)
    links_text = "\n".join(links)

    tone_variants = [
        "santai dan hangat, seperti teman dekat yang menyapa",
        "semangat dan penuh sukacita",
        "lembut dan penuh kasih",
        "singkat dan to the point, tapi tetap hangat",
        "penuh rasa syukur dan harapan",
        "seperti seorang gembala yang mengajak jemaat dengan penuh kasih",
        "sederhana dan tulus"
    ]
    tone = tone_variants[day_number % len(tone_variants)]

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    prompt = f"""Kamu adalah asisten yang membantu seorang pendeta membuat pesan harian untuk grup WhatsApp jemaat Indonesia di Korea.

Buatkan pesan WhatsApp untuk hari ini dengan format PERSIS seperti ini:

[LINK]

[SALAM SINGKAT - 1 kalimat, informal, satu baris]

[PEMBERITAHUAN BACAAN - 1-2 kalimat, sebutkan nama kitab dan pasal yang akan didengarkan hari ini]

[KALIMAT MOTIVASI/DORONGAN IMAN - 1 kalimat + emoji hati]

Ketentuan:
- Nada hari ini: {tone}
- Bacaan hari ini: {book_range}
- Link yang harus dicantumkan PERSIS di baris pertama: {links_text}
- Jika ada lebih dari 1 link, cantumkan semua link, masing-masing di baris terpisah
- Gunakan sapaan yang bervariasi (Shalom, Selamat pagi, Syalom, dll) — JANGAN selalu "Shalom, selamat pagi"
- Kalimat motivasi harus relevan dengan isi/tema kitab yang dibaca (kalau bisa)
- JANGAN tambahkan penjelasan, tanda tangan, atau kalimat lain di luar format
- Seluruh pesan dalam bahasa Indonesia

Contoh format output (JANGAN copy isinya, hanya formatnya):
https://www.bible.com/bible/306/HEB.12.TB
https://www.bible.com/bible/306/HEB.13.TB

Syalom, selamat pagi 😊

Hari ini kita mendengarkan firman Tuhan dari kitab Ibrani pasal 12 dan 13 📖

Mari kita terus berlari dengan tekun dalam iman kita ❤️"""

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text.strip()

# ── Telegram send ──────────────────────────────────────────────────────────────
def send_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "disable_web_page_preview": False
    }
    response = requests.post(url, json=payload)
    response.raise_for_status()
    print(f"✅ Message sent to Telegram!")
    return response.json()

# ── Main ───────────────────────────────────────────────────────────────────────
def main():
    print(f"🕐 Running at {datetime.now()}")

    chapters, day_number = get_todays_reading()
    book_range = format_chapter_range(chapters)
    print(f"📖 Day {day_number}: {book_range}")

    links = build_links(chapters)
    for link in links:
        print(f"🔗 {link}")

    print("✍️  Generating message...")
    message = generate_message(chapters, links, day_number)
    print(f"\n--- Message Preview ---\n{message}\n-----------------------\n")

    send_telegram(message)

if __name__ == "__main__":
    main()
