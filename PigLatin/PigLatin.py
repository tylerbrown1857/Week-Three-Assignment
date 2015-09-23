__author__ = "Tyler Brown"

def main():
    x = 0
    v = False
    while x != 1:
        word = input("Enter an english word: ")
#len(str)
        vowels = "aeiou"
        first = 'a'
        if word[0] in vowels :
            print ("This word starts with a vowel")
            v = True
        else :
            print ("This word starts with a consonant")
            v = False
        if v :
            word = word + "yay"
        else :
            first = word[0]
            word = word[1:len(word)]
            word = word + first + "ay"
        print(word)

main()