# from https://realpython.com/python-type-checking/

# def headline(text, align = True):
#     if align:
#         return f"{text.title()}\n{'-' * len(text)}"
#     else:
#         return f" {text.title()}".center(50, "o")

###
# With type hints


def headline(text: str, align: bool = True):
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()}".center(50, "o")


"""

appears to work:

In [166]: print(headline("python type checking", align ="left"))
Python Type Checking
--------------------
"""

