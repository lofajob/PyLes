# -*- coding: utf-8 -*-

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']

class ch:
      
    def change(sekf,string):
        answer = ''
        for character in string:
            if character.isalpha:
                if character ==" ":
                    answer += " "
                if character =="(":
                    answer += "("
                if character ==")":
                    answer += ")"
                if character ==".":
                    answer += "."
                for i in alphabet:
                    if i == character and character !=" ":
                        b = alphabet.index(i) + 2
                        if b >= len(alphabet):
                            b = b - len(alphabet)
                            answer += alphabet[b]
                        else:
                           answer += alphabet[b]
        print answer


b = ch()
b.change(raw_input("Enter the text: "))

