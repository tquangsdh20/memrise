"""Library Memrise Scraping"""

class Level:
    '''Level of the Memrise course infomation'''
    def __init__(self)-> None:
        ...
    def get_record(self)->tuple:
        '''Return the record of level'''
        ...
    def get_words(self)->list:
        '''Return the words in level'''
        ...

class Course:
    '''Course of Memrise information'''
    def __init__(self,course_id:int,language_id:int)->None:
        ...
    def get_record(self) -> tuple:
        '''Return the record of course'''
        ...
    def get_levels(self) -> list:
        '''Return the list of levels in course'''
        ...

class Data:
    '''Database for store data'''
    def __init__(self,filename:str)->None:
        ...
        
    def init_database(self)->None:
        ...

    def update_db_en(self,course_id,language):
        '''Update meanings and ipa of English language in database\n
        ~~~~~~~~~~~~~~~~
        Parameters:\n
        `course_id` Identify of the Memrise Course
        `language` Input your mother language (Format: 'en', 'vi', 'fr' ...)
        '''
        ...

    def update_db(self,course_id,language):
        '''Update meanings language in database\n
        ~~~~~~~~~~~~~~~~
        Parameters:\n
        `course_id` Identify of the Memrise Course
        `language` Input your mother language (Format: 'en', 'vi', 'fr' ...)
        '''
        ...
    def update_course(self,course:Course) -> None:
        '''Update database with the course avaiable'''
        ...
    
    def close(self):
        '''Close the database'''
        ...

from .memrise import Course, Level, Data

__all__ = ['Level','Course','Data']
