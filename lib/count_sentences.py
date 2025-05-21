#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, string):
        if isinstance(string, str):
            self._value = string
        else:
            print("The value must be a string.")
    def is_exclamation(self):
        return True if self.value[-1] == "!" else False

    def is_sentence(self):
        return True if self.value[-1] == "." else False
    def is_question(self):
        return True if self.value[-1] == "?" else False
    def count_sentences(self):
        symb = []
        for x in range(len(self.value)):
            if (self.value[x] in ("!", ".", "?")):
                if (self.value[x-1].isalpha()):
                    symb.append(self.value[x])
        return len(symb)