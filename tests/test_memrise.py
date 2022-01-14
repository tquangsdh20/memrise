from memrise import __version__, Level, Course, Data, TypeError
from memrise.__main__ import main
import os
import unittest


def test_version():
    assert __version__ == "1.3.1"


def test_main():
    assert main() is None


# ------------------- Class ----------------------
# Name: Level
# Input: (Path,LevelID,CourseID)
# Path Format: "/course/{CourseID}/{name-of-course}/{LevelID}/"
# Type: Public Class
# Methods:
# - `get_words()` -> List[Tuple[Word,Meaning,CourseID,LevelID]]
# - `get_record()` -> Tuple[CourseID,LevelID,LevelName]
# -------------------------------------------------

path = "/course/6033092/food-and-drink/1/"
level_id = 1
course_id = 6033092
LEVEL = Level(path, level_id, course_id)


class TestLevelMethods(unittest.TestCase):
    def test_get_words(self):
        words = LEVEL.get_words()
        self.assertListEqual(
            words,
            [
                ("le pain", "bread", 6033092, 1),
                ("le petit déjeuner", "breakfast", 6033092, 1),
                ("les fruits", "fruits", 6033092, 1),
                ("le fromage", "cheese", 6033092, 1),
                ("l'œuf", "egg", 6033092, 1),
                ("le poisson", "fish", 6033092, 1),
                ("la fourchette", "fork", 6033092, 1),
                ("la soupe", "soup", 6033092, 1),
                ("le champignon", "mushroom", 6033092, 1),
                ("le couteau", "knife", 6033092, 1),
                ("le citron", "lemon", 6033092, 1),
                ("la viande", "meat", 6033092, 1),
                ("la cuillère", "spoon", 6033092, 1),
                ("le sucre", "sugar", 6033092, 1),
                ("la salade", "salad", 6033092, 1),
                ("je mange", "I eat", 6033092, 1),
                ("je cuisine", "I cook", 6033092, 1),
            ],
        )

    def test_get_record(self):
        record = LEVEL.get_record()
        self.assertTupleEqual(record, (6033092, 1, "Food"))


# ------------------- Class ----------------------
# Name: Course
# Input: (CourseID,LanguageID)
# Type: Public Class
# Methods:
# - `get_levels()` -> List[Level]
# - `get_record()` -> Tuple[CourseID,Name,LanguageID]
# -------------------------------------------------
path = "/course/6033092/food-and-drink/2/"
course_id = 6033092
COURSE = Course(course_id)
LEVEL1 = Level(path, 2, course_id)


class TestCourseMethods(unittest.TestCase):
    def test_get_levels(self):
        levels = COURSE.get_levels()
        self.assertTupleEqual(levels[0].get_record(), LEVEL.get_record())
        self.assertTupleEqual(levels[1].get_record(), LEVEL1.get_record())
        self.assertListEqual(levels[0].get_words(), LEVEL.get_words())
        self.assertListEqual(levels[1].get_words(), LEVEL1.get_words())

    def test_get_record(self):
        record = COURSE.get_record()
        self.assertTupleEqual(record, (6033092, "FOOD AND DRINK", "fr"))


# ------------------- Class ----------------------
# Name: Data
# Input: (filename)
# Type: Public Class Child
# Methods:
# - `init_database()` : Initialize database
# - `update_level(Level)` : Integrate the level into the database
# - `update_course(Course)` : Integrate the course into the database
# - `update_ipa()`: Auto update English IPA in Database
# - `close()` : Close the database file
# -------------------------------------------------
filename = "TestEnglish.db"
DB = Data(filename)


class TestDataMethods(unittest.TestCase):
    def test_init_database(self):
        DB.init_database()
        DB.cur.execute(
            """
        SELECT name FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
        """
        )
        tables = DB.cur.fetchall()
        self.assertEqual(
            tables,
            [
                ("courses",),
                ("languages",),
                ("levels",),
                ("sqlite_sequence",),
                ("words",),
            ],
        )

    def test_update_level(self):
        DB.init_database()
        DB.cur.execute(
            """INSERT INTO "courses" ("id", "name", "language_code") VALUES (?,?,?);""",
            (6033092, "FOOD AND DRINK", "fr"),
        )
        DB.update_level(LEVEL)
        DB.cur.execute("SELECT word from words ;")
        words = DB.cur.fetchall()
        self.assertListEqual(
            words,
            [
                ("le pain",),
                ("le petit déjeuner",),
                ("les fruits",),
                ("le fromage",),
                ("l'œuf",),
                ("le poisson",),
                ("la fourchette",),
                ("la soupe",),
                ("le champignon",),
                ("le couteau",),
                ("le citron",),
                ("la viande",),
                ("la cuillère",),
                ("le sucre",),
                ("la salade",),
                ("je mange",),
                ("je cuisine",),
            ],
        )

    def test_update_course(self):
        DB.init_database()
        DB.update_course(COURSE)
        DB.cur.execute("SELECT count(*) FROM words ; ")
        __number = DB.cur.fetchone()[0]
        self.assertEqual(__number, 17)

    def test_update_ipa(self):
        DB.init_database()
        course = Course(6056798)
        DB.update_course(course)
        DB.update_ipa()
        DB.conn.commit()
        DB.cur.execute("SELECT IPA,id FROM words ;")
        ipas = DB.cur.fetchall()
        self.assertListEqual(
            ipas,
            [
                ("sʊt", 1),
                ("kʊd", 2),
                ("fʊl", 3),
                ("fʊt", 4),
                ("pʊl", 5),
                ("ʃʊd", 6),
                ("lʊk", 7),
                ("bʊk", 8),
                ("stʊd", 9),
            ],
        )

    def test_update(self):
        # Test in case of wrong data type
        with self.assertRaises(TypeError):
            DB._update("ANY", "str")

    def test_update_ipa2(self):
        # Test in case of wrong data type
        with self.assertRaises(Exception):
            DB.update_ipa("as")

    def test_update_trans(self):
        DB.init_database()
        DB.update_course(COURSE)
        DB.update_trans("vi")
        DB.cur.execute("SELECT sub FROM words WHERE id = 1;")
        le_pain = DB.cur.fetchone()[0]
        DB.cur.execute("SELECT sub FROM words WHERE id = 14;")
        le_sucre = DB.cur.fetchone()[0]
        self.assertEqual(le_pain, "bánh mì")
        self.assertEqual(le_sucre, "đường")

    def test_update_trans2(self):
        DB.init_database()
        course = Course(22542)
        DB.update_course(course)
        DB.update_trans("vi")
        DB.cur.execute("SELECT sub FROM words WHERE id = 1;")
        first = DB.cur.fetchone()[0]
        DB.cur.execute("SELECT sub FROM words WHERE id = 2;")
        second = DB.cur.fetchone()[0]
        self.assertEqual(first, "london")
        self.assertEqual(second, "thuê")

    def test_update_trans3(self):
        DB.init_database()
        # Japanese course
        course = Course(1389173)
        DB.update_course(course)
        DB.update_trans("vi")
        DB.cur.execute("SELECT sub FROM words WHERE id = 1;")
        first = DB.cur.fetchone()[0]
        self.assertEqual(first, "à chính nó đấy")
        DB.cur.execute("SELECT sub FROM words WHERE id = 2;")
        second = DB.cur.fetchone()[0]
        self.assertEqual(second, "có lẽ")

    # def test_update_trans4(self):
    #     DB.init_database()
    #     # Japanese course
    #     course = Course(2141906)
    #     course2 = Course(2141908)
    #     course3 = Course(1125956)
    #     DB.update_course(course)
    #     DB.update_course(course2)
    #     DB.update_course(course3)
    #     DB.update_trans("ja")
    #     DB.cur.execute("SELECT sub FROM words WHERE id = 5;")
    #     first = DB.cur.fetchone()[0]
    #     self.assertEqual(first, "行こう")
    #     DB.cur.execute("SELECT sub FROM words WHERE id = 7;")
    #     second = DB.cur.fetchone()[0]
    #     self.assertEqual(second, "しよう")

    def test_close(self):
        file = "test_close.db"
        db = Data("test_close.db")
        db.init_database()
        db.close()
        os.remove(file)


if __name__ == "__main__":
    unittest.main()
    DB.close()
