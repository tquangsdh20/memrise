import re
import requests
from bs4 import BeautifulSoup
from typing import Any, List, Tuple


PAGE = "https://app.memrise.com"


# ******* Function Define ********

# ---------------- Function -----------------------
# Name: open_soup(URL) 
# Type: Local function
# Feature: Return the Soup of the Level or Course URL
# --------------------------------------------------

def open_soup(url: str):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    return soup

# ---------------- Function -----------------------
# Name: get_name(Tag,Soup) 
# Type: Local function
# Feature: Return the name of the level or the course
# --------------------------------------------------

def get_name(tag_chr: str, soup: BeautifulSoup):
    tag = soup.find(tag_chr)
    # Must be encoded cause tag.text -> return str (UNICODE Python 3)
    name = tag.text.strip()
    return name


# ---------------- Function -----------------------
# Name: _get_words (Soup,CoureID,LevelID) 
# Type: Local function
# Feature: Return list of record of words in Memrise
# Format Record : (Word, Meaning, CourseID , LevelID)
# --------------------------------------------------


def _get_words(
    soup: BeautifulSoup, course_id: Any, level_id: Any
) -> List[Tuple[Any, Any, Any, Any]]:
    words = []
    meanings = []
    tags = soup("div")
    count = 0
    # Filter with col_a & col_b
    for tag in tags:
        item = tag.get("class")
        if item is None:
            continue
        if "col_a" in item:
            words.append(tag.text)
        if "col_b" in item:
            count += 1
            meanings.append(tag.text)
    records = list()
    # Get make words in records list: word | meaning | courseID | LevelID
    for i in range(count):
        record = (words[i], meanings[i], course_id, level_id)
        records.append(record)
    return records


# ******* Class Define **********

# ------------------- Class ----------------------
# Name: Level
# Input: (Path,LevelID,CourseID)
# Path Format: "/course/{CourseID}/{name-of-course}/{LevelID}/"
# Type: Public Class
# Methods:
# - `get_words()` -> List[Tuple[Word,Meaning,CourseID,LevelID]]
# - `get_record()` -> Tuple[CourseID,LevelID,LevelName]
# -------------------------------------------------


class Level:
    """Level of the Memrise course infomation\n
    Methods:\n
    - `get_words()` : get all the words in the current level
    - `get_record()` : get the information about the current level"""

    def __init__(self, path, LevelID, CourseID):
        __page_tmp = PAGE + path
        self.__page = __page_tmp
        self.__soup = open_soup(self.__page)
        __name_tmp = get_name("h3", self.__soup)
        self.__name = __name_tmp
        self.__words = _get_words(self.__soup, CourseID, LevelID)
        self.__record = tuple([CourseID, LevelID, self.__name])

    def get_words(self) -> List[Any]:
        return self.__words

    def get_record(self) -> Tuple[Any, ...]:
        return self.__record


# ------------------- Class ----------------------
# Name: Course
# Input: (CourseID,LanguageID)
# Type: Public Class
# Methods:
# - `get_levels()` -> List[Level]
# - `get_record()` -> Tuple[CourseID,Name,LanguageID]
# -------------------------------------------------


class Course:
    """Course of Memrise information\n
    Methods:\n
    - `get_levels()` : get all the words in the current level
    - `get_record()` : get the information about the current level"""

    def __init__(self, course_id: int, language_id: int):
        __page_tmp = PAGE + "/course/" + str(course_id)
        self.__page = __page_tmp
        self.__soup = open_soup(self.__page)
        self.course_id = course_id
        # Get name data type is char* ~ bytes
        __name_tmp = get_name("h1", self.__soup)
        self.__name = __name_tmp
        self.__record = tuple([course_id, self.__name, language_id])
        self.__levels = self.__get_levels(self.__soup)

    def get_levels(self) -> List[Level]:
        return self.__levels

    def __get_levels(self, soup) -> List[Level]:
        # Get all levels with Regular Expression End with "Digital/"
        tags = soup("a")
        levels = list()
        expr = "/(\\d)+/$"  # End with "{digital}/"
        count = 1
        for tag in tags:
            item = tag.get("href", None)
            if re.search(expr, item) is not None:
                level = Level(item, count, self.course_id)
                levels.append(level)
                count += 1
        return levels

    def get_record(self) -> Tuple[Any, ...]:
        return self.__record
