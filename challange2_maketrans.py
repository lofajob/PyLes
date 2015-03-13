# -*- coding: utf-8 -*-
from string import maketrans

alphabet = "abcdefghijklmnopqrstuvwxyz .()"
changed_alphabet = "cdefghijklmnopqrstuvwxyzab .()"
text = "map"


new_text = maketrans(alphabet,changed_alphabet)
print text.translate(new_text)
