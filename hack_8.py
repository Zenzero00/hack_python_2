"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    lv = []
    x = len(result)
    for i in range(len(result)):
        if len(result) % 2 == 0:
            lv.append(str(x))
        else:
            lv.append(result[x - 1] + "-" + str(x))
        x -= 1
    result = lv
    return result
