#Joe Melia EET-107

def main():
    char = input("What character would you like to repeat? ")
    num = int(input(f"How many {char} 's would you like: "))
    string = []
    repeat(char, num, string)
    result = ""
    print(result.join(string))

def repeat(char, num, string):
    if num > 0:
        string.append(char)
        num -= 1
        repeat(char, num, string) 
main()
