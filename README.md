<p align="center">
    <img src="https://raw.githubusercontent.com/tquangsdh20/memrise/main/.github/memrise.svg">
</p>

<p align="center"> 
   <a href="https://github.com/tquangsdh20/memrise/runs/4333596041"><img src="https://github.com/tquangsdh20/text2ipa/actions/workflows/test.yml/badge.svg"></a> <a href="https://app.codecov.io/gh/tquangsdh20/memrise"><img src = "https://codecov.io/gh/tquangsdh20/memrise/branch/main/graphs/badge.svg?branch=main"></a> <img src = "https://img.shields.io/pypi/pyversions/memrise"> <img src="https://img.shields.io/pypi/implementation/memrise"> <img src="https://img.shields.io/github/last-commit/tquangsdh20/memrise"> <img src="https://img.shields.io/github/license/tquangsdh20/memrise">
</p>

## Features:
- Support scraping the courses in MEM to take the vocabulary

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

Access the Website: [Memrise](https://app.memrise.com/course/) and copy the Course ID as the following picture:

<p align="center">
  <img src="https://raw.githubusercontent.com/tquangsdh20/memrise/main/.github/CourseID.PNG">
</p>

### Import library and initialize database

```python
from memrise import Course, Data
#Create file database output
db = Data('English.sqlite') #Other format is .db
#Connect to file database and init
db.init_database()
```

### Scraping course with ID

Regarding to Module Course with two paramemters:
- `CourseID`: Get the Course ID as above
- `LanguageID`: The Language ID of the Course which you study.

Where, the LanguageID is define as the followings:
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

The following example is scraping the English course for Vietnamese with IPA of English US, so the Language ID is 2.
```python
#Connect the course to scraping info this maybe take a few momment.
course = Course(1658724,2)
#Update information about the course
db.update_course(course)
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

<p align="center">
  <img src="https://raw.githubusercontent.com/tquangsdh20/memrise/main/.github/OUTPUT.PNG" height=200 width=600 />
</p>

Show the words table as the following steps: **Browse Data > Table > Word**

<p align="center">
  <img src="https://raw.githubusercontent.com/tquangsdh20/memrise/main/.github/OUTPUT2.PNG" height=500 width=800>
</p>

If you want to choose the raw meaning, you could run the following SQL statement.

```SQL
SELECT word, sub, IPA FROM words
```
Steps : **Execute SQL > Typing SQL Statements > Run**

<p align="center">
  <img src="https://raw.githubusercontent.com/tquangsdh20/memrise/main/.github/OUTPUT3.PNG" height=500 width=800>
</p>

[<b>Github:</b> https://github.com/tquangsdh20/memrise](https://github.com/tquangsdh20/memrise)

### Log changes:

**v1.0.0**: Implementation Scrapping Vocabulary  
**v1.1.0**: Update IPA Function   
**v1.2.1** : Release check for fixing ERROR IPA and update new TRANSLATE FUNCTION  

<a href="https://github.com/tquangsdh20/memrise"><p align="center"><img src="https://img.shields.io/badge/Github-tquangsdh20-orange?style=social&logo=github"></p></a>
