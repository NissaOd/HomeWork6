import re

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"

TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k",
                "l", "m", "n", "o", "p", "r", "s", "t", "u",
                "f", "h", "ts", "ch", "sh", "sch", "", "y",
                "", "e", "yu", "ja", "je", "i", "ji", "g")
# проверим кол-во букв CYRILLIC_SYMBOLS и кол-во TRANSLATION
print(len(CYRILLIC_SYMBOLS), len(TRANSLATION))
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()
# напишем функцию normalize 
def normalize(nane: str) -> str:
    t_name = nane.translate(TRANS) 
    t_name = re.sub(r'\W', '_', t_name)

# замена всех не латинских букв на подчеркивание'_'(регулярка)
    return t_name
#  print(normalize('Усе прілилі'))



