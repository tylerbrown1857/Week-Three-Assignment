__author__ = "Tyler Brown"
__program__ = "PigLatinTranslator"
__assignment__ = "WeekThreeLab"

def main():
    x = 0
    v = False
    while x != 1:
        word = input("Enter an english word to translate: ")
#len(str)
#I added the capitol versions to the list to compare to
        vowels = "aeiouAEIOU"
        first = 'a'
#tests first letter consonant
        if word[0] in vowels :
            print ("This word starts with a vowel")
            v = True
        else :
            print ("This word starts with a consonant")
            v = False
#translates word if first is a vowel
        if v :
            word = word + "yay"
#translates word is first is a consonant
        else :
            first = word[0]
            word = word[1:len(word)]
            word = word + first + "ay"
        print(word)

main()