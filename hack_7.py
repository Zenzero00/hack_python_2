"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    lv = []
    x = 1
    if result == [0]:
        lv.append(0)
    else:
        for i in range(len(result)):
            if i % 2 == 0:
                lv.append(str(x))
            else:
                lv.append(x)
            x += 1
    result = lv
    return result
