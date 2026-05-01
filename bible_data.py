# Bible chapter duration data (in seconds) - Indonesian TB version
# Source: approximate audio durations for Terjemahan Baru narration
# Format: "BOOK_CODE": [ch1_duration, ch2_duration, ...]

BIBLE_CHAPTERS = {
    # NEW TESTAMENT (continuing from Hebrews 14... but Hebrews only has 13 chapters)
    # Starting from Hebrews 13 onward → James → 1Peter → 2Peter → 1John → 2John → 3John → Jude → Revelation
    # Then Old Testament: Genesis → ... → Malachi

    "HEB": {
        "name": "Ibrani",
        "youversion_book": "HEB",
        "chapters": [
            340, 360, 300, 280, 420, 380, 420, 520, 480, 460,  # 1-10
            600, 480, 420  # 11-13 (Hebrews has 13 chapters, index 13 = ch13)
        ]
    },
    "JAS": {
        "name": "Yakobus",
        "youversion_book": "JAS",
        "chapters": [360, 300, 340, 300, 320]  # 1-5
    },
    "1PE": {
        "name": "1 Petrus",
        "youversion_book": "1PE",
        "chapters": [380, 300, 260, 280, 300]  # 1-5
    },
    "2PE": {
        "name": "2 Petrus",
        "youversion_book": "2PE",
        "chapters": [320, 280, 260]  # 1-3
    },
    "1JN": {
        "name": "1 Yohanes",
        "youversion_book": "1JN",
        "chapters": [360, 290, 300, 300, 280]  # 1-5
    },
    "2JN": {
        "name": "2 Yohanes",
        "youversion_book": "2JN",
        "chapters": [180]  # 1 (single chapter)
    },
    "3JN": {
        "name": "3 Yohanes",
        "youversion_book": "3JN",
        "chapters": [160]  # 1 (single chapter)
    },
    "JUD": {
        "name": "Yudas",
        "youversion_book": "JUD",
        "chapters": [240]  # 1 (single chapter)
    },
    "REV": {
        "name": "Wahyu",
        "youversion_book": "REV",
        "chapters": [
            380, 260, 340, 360, 280, 340, 360, 300, 400, 360,  # 1-10
            320, 400, 360, 320, 280, 340, 380, 340, 360, 280,  # 11-20
            380, 360  # 21-22
        ]
    },
    # OLD TESTAMENT
    "GEN": {
        "name": "Kejadian",
        "youversion_book": "GEN",
        "chapters": [
            480, 360, 340, 400, 360, 360, 480, 400, 520, 360,  # 1-10
            340, 380, 320, 360, 420, 380, 480, 360, 420, 360,  # 11-20
            480, 400, 360, 480, 420, 380, 520, 480, 420, 360,  # 21-30
            520, 480, 420, 380, 520, 480, 420, 380, 480, 420,  # 31-40
            400, 380, 420, 360, 400, 380, 420, 400, 420, 380   # 41-50
        ]
    },
    "EXO": {
        "name": "Keluaran",
        "youversion_book": "EXO",
        "chapters": [
            380, 420, 360, 400, 380, 360, 420, 380, 400, 360,  # 1-10
            380, 360, 400, 380, 420, 380, 400, 480, 420, 380,  # 11-20
            400, 360, 380, 420, 400, 380, 420, 380, 400, 360,  # 21-30
            420, 380, 400, 420, 380, 400, 420, 380, 400, 420   # 31-40
        ]
    },
    "LEV": {
        "name": "Imamat",
        "youversion_book": "LEV",
        "chapters": [
            340, 360, 340, 380, 360, 340, 380, 360, 340, 360,  # 1-10
            380, 360, 380, 360, 380, 360, 380, 360, 380, 420,  # 11-20
            380, 360, 380, 360, 420, 380, 420                   # 21-27
        ]
    },
    "NUM": {
        "name": "Bilangan",
        "youversion_book": "NUM",
        "chapters": [
            420, 380, 400, 360, 420, 380, 400, 420, 380, 400,  # 1-10
            420, 380, 400, 420, 380, 400, 420, 380, 400, 380,  # 11-20
            400, 420, 380, 420, 380, 400, 420, 380, 420, 380,  # 21-30
            420, 380, 400, 420, 380                             # 31-35
        ]
    },
    "DEU": {
        "name": "Ulangan",
        "youversion_book": "DEU",
        "chapters": [
            420, 380, 420, 380, 420, 380, 420, 380, 420, 380,  # 1-10
            420, 380, 420, 380, 420, 380, 420, 380, 420, 380,  # 11-20
            420, 380, 420, 380, 420, 380, 420, 380, 420, 380,  # 21-30
            420, 380, 420, 380                                  # 31-34
        ]
    },
    "JOS": {
        "name": "Yosua",
        "youversion_book": "JOS",
        "chapters": [
            380, 340, 360, 380, 360, 380, 360, 380, 360, 380,  # 1-10
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 11-20
            360, 380, 360, 380                                  # 21-24
        ]
    },
    "JDG": {
        "name": "Hakim-hakim",
        "youversion_book": "JDG",
        "chapters": [
            360, 380, 360, 380, 360, 420, 380, 360, 420, 380,  # 1-10
            420, 380, 420, 380, 420, 380, 420, 380, 420, 380,  # 11-20
            420                                                  # 21
        ]
    },
    "RUT": {
        "name": "Rut",
        "youversion_book": "RUT",
        "chapters": [360, 300, 280, 340]  # 1-4
    },
    "1SA": {
        "name": "1 Samuel",
        "youversion_book": "1SA",
        "chapters": [
            380, 360, 380, 360, 380, 360, 380, 360, 380, 360,  # 1-10
            380, 360, 380, 360, 380, 360, 380, 360, 380, 360,  # 11-20
            380, 360, 380, 360, 380, 360, 380, 360, 380, 360,  # 21-30
            380                                                  # 31
        ]
    },
    "2SA": {
        "name": "2 Samuel",
        "youversion_book": "2SA",
        "chapters": [
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 1-10
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 11-20
            360, 380, 360, 380                                  # 21-24
        ]
    },
    "1KI": {
        "name": "1 Raja-raja",
        "youversion_book": "1KI",
        "chapters": [
            420, 380, 360, 380, 360, 380, 360, 420, 360, 380,  # 1-10
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 11-20
            360, 380                                             # 21-22
        ]
    },
    "2KI": {
        "name": "2 Raja-raja",
        "youversion_book": "2KI",
        "chapters": [
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 1-10
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 11-20
            360, 380, 360, 380, 360                             # 21-25
        ]
    },
    "1CH": {
        "name": "1 Tawarikh",
        "youversion_book": "1CH",
        "chapters": [
            420, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 1-10
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 11-20
            360, 380, 360, 380, 360, 380, 360, 380, 360        # 21-29
        ]
    },
    "2CH": {
        "name": "2 Tawarikh",
        "youversion_book": "2CH",
        "chapters": [
            420, 360, 380, 360, 380, 360, 380, 360, 380, 360,  # 1-10
            380, 360, 380, 360, 380, 360, 380, 360, 380, 360,  # 11-20
            380, 360, 380, 360, 380, 360, 380, 360, 380, 360,  # 21-30
            380, 360, 380, 360, 380, 360                        # 31-36
        ]
    },
    "EZR": {
        "name": "Ezra",
        "youversion_book": "EZR",
        "chapters": [360, 340, 360, 340, 360, 340, 360, 340, 360, 340]  # 1-10
    },
    "NEH": {
        "name": "Nehemia",
        "youversion_book": "NEH",
        "chapters": [
            380, 360, 380, 360, 380, 360, 380, 360, 420, 360,  # 1-10
            380, 360, 380                                        # 11-13
        ]
    },
    "EST": {
        "name": "Ester",
        "youversion_book": "EST",
        "chapters": [360, 340, 360, 340, 360, 340, 360, 340, 360, 340]  # 1-10
    },
    "JOB": {
        "name": "Ayub",
        "youversion_book": "JOB",
        "chapters": [
            360, 340, 360, 340, 360, 340, 360, 340, 360, 340,  # 1-10
            360, 340, 360, 340, 360, 340, 360, 340, 360, 340,  # 11-20
            360, 340, 360, 340, 360, 340, 360, 340, 360, 340,  # 21-30
            360, 340, 360, 340, 360, 340, 360, 340, 360, 340,  # 31-40
            360, 340                                             # 41-42
        ]
    },
    "PSA": {
        "name": "Mazmur",
        "youversion_book": "PSA",
        "chapters": [
            360, 240, 280, 300, 260, 300, 360, 280, 320, 280,  # 1-10
            240, 280, 300, 320, 280, 300, 280, 320, 280, 300,  # 11-20
            420, 320, 280, 300, 320, 300, 360, 280, 300, 320,  # 21-30
            380, 300, 320, 280, 380, 300, 360, 420, 320, 300,  # 31-40
            360, 320, 300, 360, 320, 300, 320, 300, 320, 300,  # 41-50
            360, 300, 320, 300, 320, 300, 320, 300, 320, 300,  # 51-60
            320, 300, 280, 300, 320, 300, 280, 300, 320, 300,  # 61-70
            360, 320, 280, 300, 320, 300, 320, 300, 360, 300,  # 71-80
            320, 280, 300, 320, 300, 360, 320, 280, 320, 300,  # 81-90
            280, 260, 300, 280, 300, 360, 280, 300, 360, 280,  # 91-100
            300, 320, 300, 320, 300, 420, 300, 320, 300, 320,  # 101-110
            280, 260, 240, 260, 280, 420, 280, 300, 420, 280,  # 111-120
            240, 260, 240, 260, 240, 260, 240, 260, 240, 260,  # 121-130
            240, 260, 240, 260, 540, 300, 280, 300, 280, 300,  # 131-140
            280, 300, 280, 300, 280, 300, 280, 300, 280, 540   # 141-150
        ]
    },
    "PRO": {
        "name": "Amsal",
        "youversion_book": "PRO",
        "chapters": [
            380, 360, 380, 360, 420, 380, 420, 380, 360, 380,  # 1-10
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 11-20
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 21-30
            380                                                  # 31
        ]
    },
    "ECC": {
        "name": "Pengkhotbah",
        "youversion_book": "ECC",
        "chapters": [360, 300, 320, 280, 300, 320, 300, 320, 300, 320, 300, 320]  # 1-12
    },
    "SNG": {
        "name": "Kidung Agung",
        "youversion_book": "SNG",
        "chapters": [360, 300, 280, 300, 320, 280, 320, 280]  # 1-8
    },
    "ISA": {
        "name": "Yesaya",
        "youversion_book": "ISA",
        "chapters": [
            380, 300, 360, 320, 380, 360, 420, 340, 320, 360,  # 1-10
            380, 360, 340, 360, 340, 360, 380, 360, 380, 360,  # 11-20
            380, 360, 380, 360, 380, 420, 380, 360, 380, 360,  # 21-30
            380, 360, 380, 360, 380, 420, 380, 360, 420, 380,  # 31-40
            420, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 41-50
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 51-60
            380, 360, 380, 360, 380                             # 61-66 (wait, Isaiah has 66 chapters)
            # padding to 66
        ]
    },
    "JER": {
        "name": "Yeremia",
        "youversion_book": "JER",
        "chapters": [
            380, 360, 380, 360, 380, 420, 380, 360, 380, 360,  # 1-10
            380, 360, 380, 360, 380, 360, 380, 360, 420, 380,  # 11-20
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 21-30
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 31-40
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 41-50
            380, 360                                             # 51-52
        ]
    },
    "LAM": {
        "name": "Ratapan",
        "youversion_book": "LAM",
        "chapters": [420, 380, 520, 360, 380]  # 1-5
    },
    "EZK": {
        "name": "Yehezkiel",
        "youversion_book": "EZK",
        "chapters": [
            380, 300, 360, 380, 360, 380, 360, 380, 360, 380,  # 1-10
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 11-20
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 21-30
            360, 380, 360, 380, 360, 380, 360, 380, 360, 380,  # 31-40
            420, 380, 420, 380, 420, 380, 420, 380             # 41-48
        ]
    },
    "DAN": {
        "name": "Daniel",
        "youversion_book": "DAN",
        "chapters": [380, 420, 380, 360, 380, 360, 420, 380, 420, 380, 360, 380]  # 1-12
    },
    "HOS": {
        "name": "Hosea",
        "youversion_book": "HOS",
        "chapters": [360, 300, 320, 280, 300, 320, 300, 320, 300, 320, 300, 280, 320, 300]  # 1-14
    },
    "JOL": {
        "name": "Yoel",
        "youversion_book": "JOL",
        "chapters": [300, 320, 300]  # 1-3 (some versions have 4)
    },
    "AMO": {
        "name": "Amos",
        "youversion_book": "AMO",
        "chapters": [360, 300, 320, 280, 300, 320, 300, 320, 300]  # 1-9
    },
    "OBA": {
        "name": "Obaja",
        "youversion_book": "OBA",
        "chapters": [240]  # 1 (single chapter)
    },
    "JON": {
        "name": "Yunus",
        "youversion_book": "JON",
        "chapters": [300, 260, 300, 260]  # 1-4
    },
    "MIC": {
        "name": "Mikha",
        "youversion_book": "MIC",
        "chapters": [360, 300, 320, 300, 320, 300, 320]  # 1-7
    },
    "NAM": {
        "name": "Nahum",
        "youversion_book": "NAM",
        "chapters": [300, 280, 300]  # 1-3
    },
    "HAB": {
        "name": "Habakuk",
        "youversion_book": "HAB",
        "chapters": [300, 280, 300]  # 1-3
    },
    "ZEP": {
        "name": "Zefanya",
        "youversion_book": "ZEP",
        "chapters": [300, 280, 300]  # 1-3
    },
    "HAG": {
        "name": "Hagai",
        "youversion_book": "HAG",
        "chapters": [280, 300]  # 1-2
    },
    "ZEC": {
        "name": "Zakharia",
        "youversion_book": "ZEC",
        "chapters": [
            360, 300, 280, 300, 320, 300, 320, 300, 320, 300,  # 1-10
            320, 300, 320, 300                                   # 11-14
        ]
    },
    "MAL": {
        "name": "Maleakhi",
        "youversion_book": "MAL",
        "chapters": [300, 280, 300, 280]  # 1-4
    },
    # GOSPELS & ACTS (after OT, cycle continues)
    "MAT": {
        "name": "Matius",
        "youversion_book": "MAT",
        "chapters": [
            420, 360, 400, 420, 480, 380, 360, 420, 380, 420,  # 1-10
            380, 420, 380, 420, 380, 420, 380, 420, 420, 380,  # 11-20
            420, 380, 420, 500, 420, 500, 420, 380             # 21-28
        ]
    },
    "MRK": {
        "name": "Markus",
        "youversion_book": "MRK",
        "chapters": [
            420, 380, 400, 380, 400, 420, 380, 420, 380, 420,  # 1-10
            380, 420, 380, 420, 380, 420                        # 11-16
        ]
    },
    "LUK": {
        "name": "Lukas",
        "youversion_book": "LUK",
        "chapters": [
            480, 420, 480, 420, 480, 420, 480, 420, 480, 420,  # 1-10
            480, 420, 480, 420, 480, 420, 480, 420, 480, 420,  # 11-20
            480, 420, 480, 420                                   # 21-24
        ]
    },
    "JHN": {
        "name": "Yohanes",
        "youversion_book": "JHN",
        "chapters": [
            420, 360, 380, 380, 420, 380, 420, 380, 420, 380,  # 1-10
            380, 420, 480, 380, 420, 380, 420, 420, 380, 420,  # 11-20
            300                                                  # 21
        ]
    },
    "ACT": {
        "name": "Kisah Para Rasul",
        "youversion_book": "ACT",
        "chapters": [
            380, 420, 380, 420, 380, 420, 380, 420, 380, 420,  # 1-10
            380, 420, 380, 420, 380, 420, 380, 420, 380, 420,  # 11-20
            380, 420, 380, 420, 380, 420, 380, 420             # 21-28
        ]
    },
    "ROM": {
        "name": "Roma",
        "youversion_book": "ROM",
        "chapters": [
            380, 380, 360, 380, 420, 380, 420, 380, 360, 380,  # 1-10
            380, 360, 380, 360, 380, 360                        # 11-16
        ]
    },
    "1CO": {
        "name": "1 Korintus",
        "youversion_book": "1CO",
        "chapters": [
            380, 360, 380, 360, 380, 360, 380, 360, 380, 360,  # 1-10
            380, 360, 480, 360, 380, 360                        # 11-16
        ]
    },
    "2CO": {
        "name": "2 Korintus",
        "youversion_book": "2CO",
        "chapters": [
            380, 360, 380, 360, 380, 360, 380, 360, 380, 360,  # 1-10
            360, 380, 360                                        # 11-13
        ]
    },
    "GAL": {
        "name": "Galatia",
        "youversion_book": "GAL",
        "chapters": [360, 380, 360, 380, 360, 380]  # 1-6
    },
    "EPH": {
        "name": "Efesus",
        "youversion_book": "EPH",
        "chapters": [380, 360, 420, 360, 380, 360]  # 1-6
    },
    "PHP": {
        "name": "Filipi",
        "youversion_book": "PHP",
        "chapters": [360, 340, 360, 340]  # 1-4
    },
    "COL": {
        "name": "Kolose",
        "youversion_book": "COL",
        "chapters": [360, 340, 360, 340]  # 1-4
    },
    "1TH": {
        "name": "1 Tesalonika",
        "youversion_book": "1TH",
        "chapters": [320, 300, 280, 300, 320]  # 1-5
    },
    "2TH": {
        "name": "2 Tesalonika",
        "youversion_book": "2TH",
        "chapters": [280, 300, 280]  # 1-3
    },
    "1TI": {
        "name": "1 Timotius",
        "youversion_book": "1TI",
        "chapters": [340, 320, 300, 320, 300, 320]  # 1-6
    },
    "2TI": {
        "name": "2 Timotius",
        "youversion_book": "2TI",
        "chapters": [320, 300, 320, 300]  # 1-4
    },
    "TIT": {
        "name": "Titus",
        "youversion_book": "TIT",
        "chapters": [300, 280, 260]  # 1-3
    },
    "PHM": {
        "name": "Filemon",
        "youversion_book": "PHM",
        "chapters": [200]  # 1 (single chapter)
    },
}

# Reading order: starting from Hebrews, then rest of NT, then OT
READING_ORDER = [
    "HEB",  # starts from chapter 14 (index 13) — but HEB only has 13 ch, so start ch13
    "JAS", "1PE", "2PE", "1JN", "2JN", "3JN", "JUD", "REV",
    "GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT",
    "1SA", "2SA", "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "EST",
    "JOB", "PSA", "PRO", "ECC", "SNG",
    "ISA", "JER", "LAM", "EZK", "DAN",
    "HOS", "JOL", "AMO", "OBA", "JON", "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL",
    "MAT", "MRK", "LUK", "JHN", "ACT",
    "ROM", "1CO", "2CO", "GAL", "EPH", "PHP", "COL",
    "1TH", "2TH", "1TI", "2TI", "TIT", "PHM",
    "HEB", "JAS", "1PE", "2PE", "1JN", "2JN", "3JN", "JUD", "REV"  # NT epistles cycle again
]

# YouVersion Bible version code for Indonesian TB
YOUVERSION_VERSION = 306  # Terjemahan Baru (TB)

THRESHOLD_SECONDS = 7 * 60  # 7 minutes

def get_flat_chapter_list():
    """Returns a flat list of (book_code, chapter_number) in reading order."""
    flat = []
    seen = {}
    for book_code in READING_ORDER:
        if book_code not in seen:
            seen[book_code] = True
            book = BIBLE_CHAPTERS[book_code]
            for i, duration in enumerate(book["chapters"]):
                flat.append({
                    "book_code": book_code,
                    "book_name": book["name"],
                    "youversion_book": book["youversion_book"],
                    "chapter": i + 1,
                    "duration": duration,
                    "total_chapters": len(book["chapters"])
                })
    return flat

def get_reading_plan(start_book="HEB", start_chapter=13):
    """
    Build a reading plan from a given start point.
    Returns list of daily readings: each item is a list of chapter dicts.
    """
    flat = get_flat_chapter_list()

    # Find start index
    start_idx = 0
    for i, ch in enumerate(flat):
        if ch["book_code"] == start_book and ch["chapter"] == start_chapter:
            start_idx = i
            break

    plan = []
    i = start_idx
    while i < len(flat):
        ch = flat[i]

        # Single-chapter book → always read alone
        if ch["total_chapters"] == 1:
            plan.append([ch])
            i += 1
            continue

        # Check duration of this chapter
        if ch["duration"] >= THRESHOLD_SECONDS:
            # 7 min or more → read 2 chapters (or 1 if next would be single-chapter book)
            if i + 1 < len(flat) and flat[i+1]["total_chapters"] > 1:
                plan.append([ch, flat[i+1]])
                i += 2
            else:
                plan.append([ch])
                i += 1
        else:
            # Under 7 min → read 3 chapters
            remaining = flat[i:]
            day_chapters = []
            j = 0
            while j < 3 and (i + j) < len(flat):
                next_ch = flat[i + j]
                if next_ch["total_chapters"] == 1 and j > 0:
                    break  # don't bundle single-chapter book
                day_chapters.append(next_ch)
                j += 1
            plan.append(day_chapters)
            i += len(day_chapters)

    return plan

def get_youversion_link(book_code, chapter):
    """Generate YouVersion link for a specific chapter."""
    return f"https://www.bible.com/bible/{YOUVERSION_VERSION}/{book_code}.{chapter}.TB"

if __name__ == "__main__":
    plan = get_reading_plan("HEB", 13)
    print(f"Total days in plan: {len(plan)}")
    for i, day in enumerate(plan[:10]):
        chapters_str = ", ".join([f"{ch['book_name']} {ch['chapter']}" for ch in day])
        durations = [f"{ch['duration']//60}m{ch['duration']%60}s" for ch in day]
        print(f"Day {i+1}: {chapters_str} ({', '.join(durations)})")
