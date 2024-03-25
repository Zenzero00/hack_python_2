"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    lv = []
    x = 1
    if result == lv:
        lv.append("0")
    else:
        for i in range(len(result)):
            if i % 2 == 0:
                lv.append(str(x))
                x += 2
            else:
                lv.append("-")
    result = lv
    return result
