from .data.constant import (
    INSERT_SUB,
    INSERT_LEVEL,
    INSERT_WORD,
    INSERT_COURSE,
    WORD_4TRANS,
)
from .data import _Data_
from .extract import Level, Course
from .translator import transUntilDone

# ------------------- Class ----------------------
# Name: Data
# Input: (filename)
# Type: Public Class Child
# Methods:
# - `init_database()` : Initialize database
# - `update_level(Level)` : Integrate the level into the database
# - `update_level(Course)` : Integrate the course into the database
# - `update_ipa()`: Auto update English IPA in Database
# - `close()` : Close the database file
# -------------------------------------------------


class Data(_Data_):
    """Database for store data\n
    Methods:
    - `init_database()` : Initialize database
    - `update_level(Level)` : Integrate the level into the database
    - `update_level(Course)` : Integrate the course into the database
    - `update_ipa()`: Auto update English IPA in Database"""

    def update_level(self, level: Level) -> None:
        __level = level.get_record()

        self._update(INSERT_LEVEL, __level)
        self.conn.commit()
        __words = level.get_words()
        self._update(INSERT_WORD, __words)

    def update_course(self, course: Course) -> None:
        __course = course.get_record()
        self._update(INSERT_COURSE, __course)
        self.conn.commit()
        levels = course.get_levels()
        for level in levels:
            self.update_level(level)
            self.conn.commit()

    def update_trans(self, language: str) -> None:
        """Auto Update Translated Text"""
        self.cur.execute(WORD_4TRANS)
        # word_id | word | language_code
        records = self.cur.fetchall()
        bulk = []
        ids = []
        language_src = records[0][2]
        for record in records:
            ids.append(record[0])
            bulk.append(record[1])
        trans = transUntilDone(bulk, language_src, language, "\r\n")
        retList = self._mergeList(trans, ids)
        self._update(INSERT_SUB, retList)
