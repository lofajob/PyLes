# -*- coding: utf-8 -*-
from string import maketrans

alphabet = "abcdefghijklmnopqrstuvwxyz .()"
changed_alphabet = "cdefghijklmnopqrstuvwxyzab .()"
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


new_text = maketrans(alphabet,changed_alphabet)
print text.translate(new_text)
