#_*utf-8*_
#__init__.py
"""Library Memrise Scraping"""
from .memrise import _Course_,_Level_
from .memdb import _Data_
from .constant import _LANGUAGE_INFO_

class Level(_Level_):
    '''Level of the Memrise course infomation'''
    def get_record(self)->tuple:
        '''Return the record of level'''
        return self._get_record()
    def get_words(self)->list:
        '''Return the words in level'''
        return self._get_words()
    def update(self,db):
        '''Load data into database'''
        self._update(db)

class Course(_Course_):
    '''Course of Memrise information'''
    def get_record(self) -> tuple:
        '''Return the record of course'''
        return self._get_record()
    def get_levels(self) -> list[Level]:
        '''Return the list of levels in course'''
        return self._get_levels(Level)

    def update(self,db):
        '''Load data into database'''
        self._update(db)
    # def get_words(self) -> list:
    #     '''Return the list of words in course'''
    #     return self._get_words()

class Database(_Data_):
    '''Database for store data'''
    def connect(self):
        self.conn,self.cur = self._get_connection()
    
    def init(self)->None:
        self._init_database()
        print(_LANGUAGE_INFO_)

    def execute(self,cmd,records):
        '''Update database with CMD'''
        for record in records:
            try:
                self.cur.execute(cmd,record)
            except:
                print('RecordError:',record)
        self.conn.commit()

    def update_db_en(self,course_id,language):
        '''Update meanings and ipa of English language in database\n
        ~~~~~~~~~~~~~~~~
        Parameters:\n
        `course_id` Identify of the Memrise Course
        `language` Input your mother language (Format: 'en', 'vi', 'fr' ...)
        '''
        self._update_db_en(course_id,language)

    def update_db(self,course_id,language):
        '''Update meanings language in database\n
        ~~~~~~~~~~~~~~~~
        Parameters:\n
        `course_id` Identify of the Memrise Course
        `language` Input your mother language (Format: 'en', 'vi', 'fr' ...)
        '''
        self._update_db(course_id,language)

    def close(self):
        self.conn.commit()
        self.cur.close()


__all__ = ['Level','Course','Database']
        
