<p align="center">
  <h1 align="center">Library Scraping Vocabulary Languages</h1>
</p>

## Features:
- Support scraping the courses in MEM to take the vocabulary
- Support scraping IPA of English Language (US and UK)
- Support translate to your mother language

## Appplication Requires

### Install DB Browser : [SQLite](https://sqlitebrowser.org/dl/)

### Install Library: 
<b>Window</b>
```
 python -m pip install memrise
```
<b>Linux</b>
  ```
  pip install memrise
  ```
 <b>macOS</b>
 ```
 sudo pip3 install memrise
```
## Guidelines

### How to take Course ID?

Access the Website: [Memrise](https://app.memrise.com/) and copy the Course ID as the following picture:

![CourseID](https://github.com/tquangsdh20/memrise/blob/main/pic/CourseID.PNG?raw=true)

### Import library and initialize database

```python
from memrise import Course,Database
#Create file database output
db = Database('English.sqlite') #Other format is .db
#Connect to file database and init
db.connect()
db.init()
```
The output will give you the List Language's ID of the Course, remember the ID for next step. 
```
Language IDs:        
    1. English UK    
    2. English US    
    3. Chinese       
    4. Janpanese     
    5. French        
    6. Spanish Mexico
    7. Italian
    8. German
    9. Russian
    10. Dutch
    11. Korean
    12. Arabic
    13. Spanish Spain

```

### Scraping course with ID
Regarding to Module Course with two paramemters:
- `CourseID`: Get the Course ID as above
- `LanguageID`: The Language ID of the Course which you study.
  
The following example is scraping the English course for Vietnamese with IPA of English US, so the Language ID is 2.
```python
#Connect the course to scraping info this maybe take a few momment.
course = Course(1658724,2)
#Update information about the course
course.update(db)
#Get all levels in course & scraping all levels information
levels = course.get_levels()
for level in levels:
    level.update(db)
```

### Update course with your language meaning

Use the method `update_db_en()` if the LANGUAGE COURSE is **English** for scraping IPA.  
Use the method `update_db()` if the Language Course is the others.  
About the parameters of two above methods are the same:  
- `CourseID` : the ID of the course
- `Language` : your mother language with format <i>'en', 'fr', 'ko', 'vi'...</i>

```python
#If your Course is English language use `update_db_en()`, otherwise use `update_db()` method.
db.update_db_en(1658724,'fr')
```
### Check the output with SQLite

File output

![OUTPUT](https://github.com/tquangsdh20/memrise/blob/main/pic/OUTPUT.PNG?raw=true)

Show the words table as the following steps: **Browse Data > Table > Word**

![OUTPUT1](https://github.com/tquangsdh20/memrise/blob/main/pic/OUTPUT2.PNG?raw=true)

If you want to choose the raw meaning, you could run the following SQL statement.

```SQL
SELECT word, sub, IPA FROM words
```
Steps : **Execute SQL > Typing SQL Statements > Run**

![OUTPUT2](https://github.com/tquangsdh20/memrise/blob/main/pic/OUTPUT3.png?raw=true)

### [Github](https://github.com/tquangsdh20/memrise)
