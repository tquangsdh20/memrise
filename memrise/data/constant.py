# ******* Constant Define *******
CREATE_TABLE = """
DROP TABLE IF EXISTS languages ;
CREATE TABLE languages(
    "id"    INTEGER NOT NULL UNIQUE,
    "name"    TEXT NOT NULL UNIQUE,
    PRIMARY KEY("id" AUTOINCREMENT) );
DROP TABLE IF EXISTS courses ;
CREATE TABLE courses (
    "id"    INTEGER NOT NULL UNIQUE,
    "name"  TEXT NOT NULL,
    "language_id" INTEGER NOT NULL,
    PRIMARY KEY("id")
    FOREIGN KEY("language_id") REFERENCES "languages"("id")
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
    "audio"    TEXT DEFAULT '{}',
    "course_id"    INTEGER,
    "level_id"    INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("course_id", "level_id") REFERENCES "levels"("course_id", "id")
);

INSERT INTO "languages" ("id","name") VALUES (0,'Unknown');
INSERT INTO "languages" ("id","name") VALUES (1,'English UK');
INSERT INTO "languages" ("id","name") VALUES (2,'English US');
INSERT INTO "languages" ("id","name") VALUES (3,'Chinese');
INSERT INTO "languages" ("id","name") VALUES (4,'Janpanese');
INSERT INTO "languages" ("id","name") VALUES (5,'French');
INSERT INTO "languages" ("id","name") VALUES (6,'Spanish Mexico');
INSERT INTO "languages" ("id","name") VALUES (7,'Italian');
INSERT INTO "languages" ("id","name") VALUES (8,'German');
INSERT INTO "languages" ("id","name") VALUES (9,'Russian');
INSERT INTO "languages" ("id","name") VALUES (10,'Dutch');
INSERT INTO "languages" ("id","name") VALUES (11,'Korean');
INSERT INTO "languages" ("id","name") VALUES (12,'Arabic');

"""

INSERT_COURSE = (
    """INSERT INTO "courses" ("id", "name", "language_id") VALUES (?,?,?);"""
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
        WHEN language_id = 1 THEN 'br'
        WHEN language_id = 2 THEN 'am'
        END AS 'Language'
FROM "words" JOIN "courses"
    ON "words".course_id = "courses".id
WHERE ("courses".language_id BETWEEN 1 AND 2) AND (IPA is NULL);
"""

# ----------------------------------------------------------------------
INSERT_SUB = """UPDATE "words" SET sub = ? WHERE "words".id = ?;"""
WORD_4TRANS = """SELECT
    "words".id
    ,word
FROM "words"
WHERE sub is NULL;
"""
