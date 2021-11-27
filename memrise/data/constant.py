# ******* Constant Define *******
CREATE_TABLE = """
DROP TABLE IF EXISTS languages ;
CREATE TABLE languages(
    "code"    TEXT NOT NULL UNIQUE,
    "name"    TEXT NOT NULL,
    PRIMARY KEY("code") );

DROP TABLE IF EXISTS courses ;
CREATE TABLE courses (
    "id"    INTEGER NOT NULL UNIQUE,
    "name"  TEXT NOT NULL,
    "language_code" TEXT NOT NULL,
    PRIMARY KEY("id")
    FOREIGN KEY("language_code") REFERENCES "languages"("code")
);

DROP TABLE IF EXISTS levels ;
CREATE TABLE "levels" (
    "course_id"    INTEGER NOT NULL,
    "id"    INTEGER NOT NULL,
    "name"    TEXT NOT NULL,
    FOREIGN KEY("course_id") REFERENCES "courses"("id"),
    PRIMARY KEY("course_id","id")
);

DROP TABLE IF EXISTS words ;
CREATE TABLE "words" (
    "id"    INTEGER NOT NULL,
    "word"    TEXT NOT NULL,
    "meaning"    TEXT DEFAULT NULL,
    "sub"    TEXT DEFAULT NULL,
    "IPA"    TEXT DEFAULT NULL,
    "audio"    BLOB DEFAULT NULL,
    "course_id"    INTEGER,
    "level_id"    INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("course_id", "level_id") REFERENCES "levels"("course_id", "id")
);
"""
INIT_LANGUAGE = 'INSERT INTO "languages" ("code","name") VALUES (?,?);'

INSERT_COURSE = (
    """INSERT INTO "courses" ("id", "name", "language_code") VALUES (?,?,?);"""
)
INSERT_LEVEL = """INSERT INTO "levels" ("course_id","id","name") VALUES (?,?,?)"""

INSERT_WORD = """INSERT INTO
"words" (
    "word"
    ,"meaning"
    ,"course_id"
    ,"level_id" )
VALUES (?,?,?,?);"""

# ------------------------------ IPA INSERT------------------------------
INSERT_IPA = """UPDATE "words" SET "IPA" = ? WHERE "words".id = ?;"""
WORD_4IPA = """SELECT word
FROM "words" JOIN "courses"
    ON "words".course_id = "courses".id
WHERE ("courses".language_id BETWEEN 1 AND 2) AND (IPA is NULL);
"""
WORD_IN_ENGLISH_4IPA = """SELECT
    "words".id
    ,word
    ,CASE
        WHEN language_code = 'en' THEN 'br'
        END AS 'Language'
FROM "words" JOIN "courses"
    ON "words".course_id = "courses".id
WHERE ("courses".language_code = 'en') AND (IPA is NULL);
"""


# ------------------------- Translation ---------------------------------
INSERT_SUB = """UPDATE "words" SET sub = ? WHERE "words".id = ?;"""
WORD_4TRANS = """
SELECT
    "words".id
    ,word
    ,language_code
FROM
    "words" JOIN "courses" ON
        "courses".id = "words".course_id
WHERE sub is NULL;
"""

LANGUAGES = {
    "af": "afrikaans",
    "sq": "albanian",
    "am": "amharic",
    "ar": "arabic",
    "hy": "armenian",
    "az": "azerbaijani",
    "eu": "basque",
    "be": "belarusian",
    "bn": "bengali",
    "bs": "bosnian",
    "bg": "bulgarian",
    "ca": "catalan",
    "ceb": "cebuano",
    "ny": "chichewa",
    "zh-cn": "chinese (simplified)",
    "zh-tw": "chinese (traditional)",
    "co": "corsican",
    "hr": "croatian",
    "cs": "czech",
    "da": "danish",
    "nl": "dutch",
    "en": "english",
    "eo": "esperanto",
    "et": "estonian",
    "tl": "filipino",
    "fi": "finnish",
    "fr": "french",
    "fy": "frisian",
    "gl": "galician",
    "ka": "georgian",
    "de": "german",
    "el": "greek",
    "gu": "gujarati",
    "ht": "haitian creole",
    "ha": "hausa",
    "haw": "hawaiian",
    "iw": "hebrew",
    "he": "hebrew",
    "hi": "hindi",
    "hmn": "hmong",
    "hu": "hungarian",
    "is": "icelandic",
    "ig": "igbo",
    "id": "indonesian",
    "ga": "irish",
    "it": "italian",
    "ja": "japanese",
    "jw": "javanese",
    "kn": "kannada",
    "kk": "kazakh",
    "km": "khmer",
    "ko": "korean",
    "ku": "kurdish (kurmanji)",
    "ky": "kyrgyz",
    "lo": "lao",
    "la": "latin",
    "lv": "latvian",
    "lt": "lithuanian",
    "lb": "luxembourgish",
    "mk": "macedonian",
    "mg": "malagasy",
    "ms": "malay",
    "ml": "malayalam",
    "mt": "maltese",
    "mi": "maori",
    "mr": "marathi",
    "mn": "mongolian",
    "my": "myanmar (burmese)",
    "ne": "nepali",
    "no": "norwegian",
    "or": "odia",
    "ps": "pashto",
    "fa": "persian",
    "pl": "polish",
    "pt": "portuguese",
    "pa": "punjabi",
    "ro": "romanian",
    "ru": "russian",
    "sm": "samoan",
    "gd": "scots gaelic",
    "sr": "serbian",
    "st": "sesotho",
    "sn": "shona",
    "sd": "sindhi",
    "si": "sinhala",
    "sk": "slovak",
    "sl": "slovenian",
    "so": "somali",
    "es": "spanish",
    "su": "sundanese",
    "sw": "swahili",
    "sv": "swedish",
    "tg": "tajik",
    "ta": "tamil",
    "te": "telugu",
    "th": "thai",
    "tr": "turkish",
    "uk": "ukrainian",
    "ur": "urdu",
    "ug": "uyghur",
    "uz": "uzbek",
    "vi": "vietnamese",
    "cy": "welsh",
    "xh": "xhosa",
    "yi": "yiddish",
    "yo": "yoruba",
    "zu": "zulu",
}
