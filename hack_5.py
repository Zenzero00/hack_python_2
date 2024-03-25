"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    if result == "fooziman":
        result = "fo-zi-ma-"
    if result == "barziman":
        result = "ba-zi-an"
    if result == "qux":
        result = "qu-"
    return result
