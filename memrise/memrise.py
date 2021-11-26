from .data import _Data_, INSERT_LEVEL, INSERT_WORD, INSERT_COURSE
from .extract import Level, Course

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
