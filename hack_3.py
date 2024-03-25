"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    result = result[:-1].title() + result[-1].upper()
    result = result.replace("a", "@")
    result = result.replace("e", "3")
    result = result.replace("i", "¡")
    result = result.replace("o", "0")
    for i in range(len(result)):
        if result[i] == "u" or result[i] == "U":
            result = result.replace(result[i], "v")
    return result
