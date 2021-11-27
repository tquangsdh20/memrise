<p align="center">
    <img src="https://raw.githubusercontent.com/tquangsdh20/memrise/main/.github/memrise.svg">
</p>

<p align="center"> 
   <a href="https://github.com/tquangsdh20/memrise/runs/4333596041"><img src="https://github.com/tquangsdh20/text2ipa/actions/workflows/test.yml/badge.svg"></a> <a href="https://app.codecov.io/gh/tquangsdh20/memrise"><img src = "https://codecov.io/gh/tquangsdh20/memrise/branch/main/graphs/badge.svg?branch=main"></a> <img src = "https://img.shields.io/pypi/pyversions/memrise"> <img src="https://img.shields.io/github/last-commit/tquangsdh20/memrise"> <img src="https://img.shields.io/github/license/tquangsdh20/memrise">
</p>

## Features:
- Support scraping the courses in MEM to take the vocabulary
- Translate the words to your own language
- Get the IPA for the English course

## Installation

**Window**
```msDoc
python -m pip install memrise
```
**Linux**
```
pip install memrise
```
**macOS**
```
sudo pip3 install memrise
```
## Appplication Requires

### Install DB Browser : [SQLite](https://sqlitebrowser.org/dl/)

### Install Library: 
```
pip install googletrans==4.0.0rc1
```

## Guidelines

### How to take Course ID?

Access the [Memrise Website](https://app.memrise.com/course/) and copy the Course ID as the following picture

<p align="center">
  <img src="https://raw.githubusercontent.com/tquangsdh20/memrise/main/.github/courseid.svg">
</p>

### Import library and initialize database

```python
from memrise import Course, Data
#Create file database output
db = Data('English.db') # Or *.sqlite easy to open
#Connect to file database and init
db.init_database()
```

### Scraping course with ID

The following example is scraping [the English course](https://app.memrise.com/course/2157577/anglais-britannique-2/) for the French 

```python
# Connect the course to scraping info this maybe take a few momment.
course = Course(2157577)
# Update information about the course
db.update_course(course)
```

### Update the IPA in database

Use the method `update_ipa()` if the **Language Course** is **English** for update the IPA information auto.  
The parameter `language` default is `br`  
- `br` : English UK
- `am` : English US

```python
# Update IPA for database with default `br`
db.update_ipa()
# Use the follow if English US
# db.update_ipa('am')
```

### Translate the vocaburaly to your own language

Use the method `update_trans(language)`  

The parameter `language` follow the [ISO 639-1 codes](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) as the bottom

```python
# Translate to Vietnamese
db.update_trans('vi')
```

### Show the output with SQLite Browser Application

Open the SQLite Browser Application and follow the steps below

<p align="center">
  <img src="https://raw.githubusercontent.com/tquangsdh20/memrise/main/.github/output1.svg">
</p>

<p align="center">
   <img src="https://raw.githubusercontent.com/tquangsdh20/memrise/main/.github/output2.svg"> 
</p>

Feel free to make your own course with the SQL query

Steps : **Execute SQL > Typing SQL Statements > Run**

```SQL
SELECT word, sub, IPA FROM words ; 
```

<p align="center">
  <img src="https://raw.githubusercontent.com/tquangsdh20/memrise/main/.github/sql.svg">
</p>

## Languages ISO369-1 Code


```
af : afrikaans                 fy : frisian                   ky : kyrgyz                sr : serbian
sq : albanian                  gl : galician                  lo : lao                   st : sesotho
am : amharic                   ka : georgian                  la : latin                 sn : shona
ar : arabic                    de : german                    lv : latvian               sd : sindhi
hy : armenian                  el : greek                     lt : lithuanian            si : sinhala
az : azerbaijani               gu : gujarati                  lb : luxembourgish         sk : slovak
eu : basque                    ht : haitian creole            mk : macedonian            sl : slovenian
be : belarusian                ha : hausa                     mg : malagasy              so : somali
bn : bengali                   haw : hawaiian                 ms : malay                 es : spanish
bs : bosnian                   iw : hebrew                    ml : malayalam             su : sundanese
bg : bulgarian                 he : hebrew                    mt : maltese               sw : swahili
ca : catalan                   hi : hindi                     mi : maori                 sv : swedish
ceb : cebuano                  hmn : hmong                    mr : marathi               tg : tajik
ny : chichewa                  hu : hungarian                 mn : mongolian             ta : tamil
zh-cn : chinese (simplified)   is : icelandic                 my : myanmar (burmese)     te : telugu
zh-tw : chinese (traditional)  ig : igbo                      ne : nepali                th : thai
co : corsican                  id : indonesian                no : norwegian             tr : turkish
hr : croatian                  ga : irish                     or : odia                  uk : ukrainian
cs : czech                     it : italian                   ps : pashto                ur : urdu
da : danish                    ja : japanese                  fa : persian               ug : uyghur
nl : dutch                     jw : javanese                  pl : polish                uz : uzbek
en : english                   kn : kannada                   pt : portuguese            vi : vietnamese
eo : esperanto                 kk : kazakh                    pa : punjabi               cy : welsh
et : estonian                  km : khmer                     ro : romanian              xh : xhosa
tl : filipino                  ko : korean                    ru : russian               yi : yiddish
fi : finnish                   ku : kurdish (kurmanji)        sm : samoan                yo : yoruba
fr : french                    gd : scots gaelic              zu : zulu       
```

### Log changes:

**v1.0.0**: Implementation Scrapping Vocabulary  
**v1.1.0**: Update IPA Function   
**v1.2.1** : Release check for fixing ERROR IPA and update new TRANSLATE FUNCTION  

<a href="https://github.com/tquangsdh20/memrise"><p align="center"><img src="https://img.shields.io/badge/Github-tquangsdh20-orange?style=social&logo=github"></p></a>
