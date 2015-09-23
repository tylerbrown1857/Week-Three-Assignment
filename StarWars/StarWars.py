__author__ = "Tyler Brown"
__program__ = "StarWarsName"
__assignment__ = "WeekThreeLab"

def main():
    x = 0
    while x != 1:
#recieve input
        first = input("Enter your first name: ")
        last = input("Enter your last name: ")
        mother = input("Enter your mother's maiden name: ")
        city = input("Enter the city you were born in: ")
        
        
#compiles first name
        starFirst = last[0:3] + first[0:2]
        starLast = mother[0:2] + city[0:3]
        
#prints new name
        print(starFirst + starLast)
        
main()