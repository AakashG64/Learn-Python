'''
pip install pyspellchecker
'''

from spellchecker import SpellChecker

txt = "Hi, Akash garg this side. I am pythtn programr. i love to do cod. I wnt to bcome a successfl sftwre develpr"
lst = txt.split(" ")

spell = SpellChecker()
# words = spell.unknown(["Pythn", "is", "god", "Lptop", "mothr", "gd"])
words = spell.unknown(lst)

for word in words:
    print(f"{word}: {spell.correction(word)}")
    print(f"{word}: {spell.candidates(word)}")
