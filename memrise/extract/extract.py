import re
import requests
from bs4 import BeautifulSoup
from typing import Any, List, Tuple
from .const import PAGE, LANGCODES

# ******* Function Define ********

# ---------------- Function -----------------------
# Name: _open_soup(URL)
# Type: Local function
# Feature: Return the Soup of the Level or Course URL
# --------------------------------------------------


def _open_soup(url: str):
    html = requests.get(url)
    soup = BeautifulSoup(html.text, "html.parser")
    return soup


# ---------------- Function -----------------------
# Name: _get_name(Tag,Soup)
# Type: Local function
# Feature: Return the name of the level or the course
# --------------------------------------------------


def _get_name(tag_chr: str, soup: BeautifulSoup):
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
    tags_a = soup("div", {"class": "col_a"})
    tags_b = soup("div", {"class": "col_b"})
    records: List[Tuple[Any, Any, Any, Any]] = []
    for idx in range(len(tags_a)):
        record = (tags_a[idx].text, tags_b[idx].text, course_id, level_id)
        records.append(record)
    return records


# ---------------- Function -----------------------
# Name: _get_language(CourseID)
# Type: Local function
# Feature: Return the language name of the course lower
# Format Record : (Word, Meaning, CourseID , LevelID)
# --------------------------------------------------


def _get_language_code(soup):
    # url = f"https://app.memrise.com/course/{courseid}/"
    # res = requests.get(url)
    # soup = BeautifulSoup(res.text,'html.parser')
    tags = soup("a")
    languages = []
    for tag in tags:
        href = tag["href"]
        if re.match("/courses/(.+)/(.+)/", href):
            text = re.findall("[a-z]+/$", href)
            if len(text) > 0:
                languages.append(text[0][0:-1])
            else:
                # Do nothing
                ...
    language = languages[-1]
    if language == "us" or language == "uk":
        language = "english"
    else:
        # Do nothing
        ...
    return LANGCODES[language]


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
        self.__soup = _open_soup(self.__page)
        __name_tmp = _get_name("h3", self.__soup)
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

    def __init__(self, course_id: int):
        __page_tmp = PAGE + "/course/" + str(course_id)
        self.__page = __page_tmp
        self.__soup = _open_soup(self.__page)
        self.course_id = course_id
        __name_tmp = _get_name("h1", self.__soup)
        __language = _get_language_code(self.__soup)
        self.__name = __name_tmp
        self.__record = tuple([course_id, self.__name, __language])
        self.__levels = self.__get_levels(self.__soup)

    def get_levels(self) -> List[Level]:
        return self.__levels

    def __get_levels(self, soup) -> List[Level]:
        # Get all levels with Regular Expression End with "Digital/"
        tags = soup.find_all("a", {"class": "level clearfix"})
        levels: List[Level] = []
        for idx in range(len(tags)):
            item = tags[idx]["href"]
            level = Level(item, idx + 1, self.course_id)
            levels.append(level)

        return levels

    def get_record(self) -> Tuple[Any, ...]:
        return self.__record
