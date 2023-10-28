"""
Два участника p1 и p2 участвуют в дуэли.
Напишите функцию whos_first, которая принимает две строки и возвращает имя игрока, который выстрелил первым.
Если игроки выстрелили одновременно, то вернуть строку "tie".
Примеры вызовов и возвратов:
whos_first(
"   Bang!        ",
"        Bang!   "
) ➞ "p1"
# p1 стреляет быстрее p2
whos_first(
"               Bang! ",
"             Bang!   "
) ➞ "p2"
# p2 стреляет быстрее p1
whos_first(
"     Bang!   ",
"     Bang!   "
) ➞ "tie"
# ничья
"""


def whos_first(str1: str, str2: str) -> str:
    return 'p1' if str1.find('B') < str2.find('B') else 'p2' if str1.find('B') > str2.find('B') else 'tie'
