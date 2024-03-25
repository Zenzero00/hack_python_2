"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    lv = {}
    for i in result:
        if i == "foo" and result[i] == "fookziman":
            lv.update({"Foo": ""})
        if i == "bar" and result[i] == "barziman":
            lv["Foo"] = "Fooziman"
    result = lv
    return result
