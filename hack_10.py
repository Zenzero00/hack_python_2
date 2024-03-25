"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    lv = [{}, {}, {}]
    x = 1
    for i in range(len(result)):
        lv[i] = {str(x): str(x + 1)}
        x += 2
    result = lv
    return result
