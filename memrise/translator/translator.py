from typing import List
from googletrans import Translator


class MissingItem(Exception):
    ...


translator = Translator()

# ----------------------- Function -----------------------
# Name : _transLimit(bulk,src,dest,sep)
# Type : Local Funtion
# Feature: Translate list of text and check error status


def _transLimit(bulk: List[str], src: str, dest: str, sep: str) -> List[str]:
    # Initialation
    texts = ""
    for text in bulk:
        texts += text + sep
    translated = translator.translate(text=texts, dest=dest, src=src)
    res = translated.text.lower().split(sep)
    trans = res[0 : len(res)]
    if len(bulk) != len(trans):
        raise MissingItem("Miss the text")
    else:
        # Doing nothing CChecker
        ...
    return trans


def get_trans(bulk: List[str], src: str, dest: str, sep: str, limit: int) -> List[str]:
    # Initialation
    retList = []
    length = len(bulk)
    leng = len(bulk)
    cnt = 0
    while leng > 0:
        start = cnt * limit
        end = (start + limit) if (start + limit) < length else length
        try:
            subList = _transLimit(bulk[start:end], dest=dest, src=src, sep=sep)
        except MissingItem as e:
            print(e)
            subList = _transLimit(bulk[start:end], dest=dest, src=src, sep="\r\n")
        else:
            retList += subList
        cnt += 1
        leng -= limit
    return retList


# ----------------------- Function -----------------------
# Name : transUntilDone(bulk,src,dest,sep)
# Type : Public Funtion
# Feature: Return the list of translated text, handle error


def transUntilDone(bulk: List[str], src: str, dest: str, sep: str) -> List[str]:
    try:
        trans = get_trans(bulk, src, dest, sep, 100)
    except MissingItem:
        start = 0
        end = len(bulk)
        middle = int(end / 2)
        LeftSubList = transUntilDone(bulk[start:middle], src, dest, sep)
        RightSubList = transUntilDone(bulk[middle:end], src, dest, sep)
        trans = LeftSubList + RightSubList
    return trans
