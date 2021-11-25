from .data import _Data_, INSERT_LEVEL, INSERT_WORD, INSERT_COURSE
from .extract import Level, Course


class Data(_Data_):
    """Database for store data\n
    Methods:
    - `update_level(Level)` : Integrate the level into the database
    - `update_level(Course)` : Integrate the course into the database"""

    def update_level(self, level: Level) -> None:
        __level = level.get_record()
        try:
            self.__update(INSERT_LEVEL, __level)
        except:
            print("RecordError: Fail to update record", __level)
        else:
            self.conn.commit()
        finally:
            __words = level.get_words()
            self._update(INSERT_WORD, level.get_words())

    def update_course(self, course: Course) -> None:
        try:
            __course = course.get_record()
            self.__update(INSERT_COURSE, __course)
        except:
            print("RecordError: Fail to update record", course.get_record())
        else:
            self.conn.commit()
        finally:
            levels = course.get_levels()
            for level in levels:
                self.update_level(level)
                self.conn.commit()
