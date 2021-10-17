
'''
n = Number
b = Base
p = Position

nb^p = Decimal

'''

debug = True

'''

[ character , it's value ]

For example:
["X", 55]

so, the value of X is 55
if we replace X with 1, 1 it's value is going to change to 55, if it's stringed.

'''

valuesList = [
    ["0", 0],
    ["1", 1],
    ["2", 2],
    ["3", 3],
    ["4", 4],
    ["5", 5],
    ["6", 6],
    ["7", 7],
    ["8", 8],
    ["9", 9],
    ["a", 10],
    ["b", 11],
    ["c", 12],
    ["d", 13],
    ["e", 14],
    ["f", 15],
    ["g", 16],
    ["h", 17],
    ["i", 18],
    ["j", 19],
    ["k", 20],
    ["l", 21],
    ["m", 22],
    ["n", 23],
    ["o", 24],
    ["p", 25],
    ["q", 26],
    ["r", 27],
    ["s", 28],
    ["t", 29],
    ["u", 30],
    ["v", 31],
    ["w", 32],
    ["x", 33],
    ["y", 34],
    ["z", 35]
]

def getValue(char):
    for valuedChar, value in valuesList:
        if char == valuedChar:
            return value
    
    return char

def toDecimal(base, x):
    result = 0
    pos = 0

    x = x[::-1].lower()

    for i in x:
        if debug:
            print(
                "x =", getValue(i),
                ", base =", base,
                ", position =", pos,
                ", equal =", getValue(i) * base ** pos
            )

        result += int(getValue(i)) * base ** pos
        pos += 1
    
    return result


print(toDecimal(35, "0b142zfjt"))
