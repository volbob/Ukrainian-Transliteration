from dictionary import *

class TransliteratedWord:
    def __init__(self, string):
        self.string = string

    def transliteration(self):
        def replaceWithDict(string):
            output=''
            k=0

            for i in string.lower():
                if k==0:
                    if i in dict_first:
                        output+=dict_first[i]
                    else:
                        output+=dict[i]
                else:
                    if i in dict:
                        output+=dict[i]
                k+=1

            return output
            
        def uppercase(string):
            temp_output=''
            i=0

            while i < len(string):
                if i == 0:
                    temp_output+=string[i].upper()
                else:
                    temp_output+=string[i]
                i+=1

            return temp_output

        output=uppercase(replaceWithDict(self.string))
        return output

        

name = TransliteratedWord(input("Name: "))
surname = TransliteratedWord(input("Surname: "))

print("Output:",name.transliteration(),surname.transliteration())