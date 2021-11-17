NATO_characters = {
    # lowercase letters
    'a': 'alfa',
    'b': 'bravo',
    'c': 'charlie',
    'd': 'delta',
    'e': 'echo',
    'f': 'foxtrot',
    'g': 'golf',
    'h': 'hotel',
    'i': 'india',
    'j': 'juliett',
    'k': 'kilo',
    'l': 'lima',
    'm': 'mike',
    'n': 'november',
    'o': 'oscar',
    'p': 'papa',
    'q': 'quebec',
    'r': 'romeo',
    's': 'sierra',
    't': 'tango',
    'u': 'uniform',
    'v': 'victor',
    'w': 'whiskey',
    'x': 'x-ray',
    'y': 'yankee',
    'z': 'zulu',
    # UPPERCASE letters
    'A': 'ALFA',
    'B': 'BRAVO',
    'C': 'CHARLIE',
    'D': 'DELTA',
    'E': 'ECHO',
    'F': 'FOXTROT',
    'G': 'GOLF',
    'H': 'HOTEL',
    'I': 'INDIA',
    'J': 'JULIETT',
    'K': 'KILO',
    'L': 'LIMA',
    'M': 'MIKE',
    'N': 'NOVEMBER',
    'O': 'OSCAR',
    'P': 'PAPA',
    'Q': 'QUEBEC',
    'R': 'ROMEO',
    'S': 'SIERRA',
    'T': 'TANGO',
    'U': 'UNIFORM',
    'V': 'VICTOR',
    'W': 'WHISKEY',
    'X': 'X-RAY',
    'Y': 'YANKEE',
    'Z': 'ZULU',
    # Numbers
    '0': 'ZERO',
    '1': 'ONE',
    '2': 'TWO',
    '3': 'THREE',
    '4': 'FOUR',
    '5': 'FIVE',
    '6': 'SIX',
    '7': 'SEVEN',
    '8': 'EIGHT',
    '9': 'NINE',
}

def get_character(NATO_word):
    for character, word in NATO_characters.items():
        if NATO_word == word:
            return character

# SELECT MODE
print("SELECT MODE:")
print("A | (Enter STRING)")
print("B | (Enter NATO Words)")
mode = input("Select Mode (Type A or B): ")

if mode == "A" or mode == "a":
    print("---")
    STRING = input('Paste STRING: ')
    print("---")
    for count, character in enumerate(STRING):
        print("Word " + str(count) + ": " + NATO_characters.get(character))

if mode == "B" or mode=="b":
    exit = False
    STRING = []
    print("---")
    print("- Input is CASE sensitive")
    print("- Enter numbers as uppercase words (9 as NINE)")
    print("- Press Enter to Finish (blank word)")
    print("---")
    count = 1
    while exit == False:

        # Get word
        NATO_next = input('Enter Word ' + str(count) + ' : ') 

        # Stop if X or x entered
        if NATO_next in ["X", "x", ""]:
            exit = True
            STRING = ''.join(STRING)
            print("")
            print(str(STRING)) 
        elif get_character(NATO_next):
            STRING.append(get_character(NATO_next))
            count = count + 1
        else:
            print("Invalid word, please try again")