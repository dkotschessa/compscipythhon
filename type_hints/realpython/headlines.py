# headlines.py

# def headline(text: str, align: bool = True) -> str:
#     if align:
#         return f"{text.title()}\n{'-' * len(text)}"
#     else:
#         return f" {text.title()} ".center(50, "o")

# print(headline("python type checking"))
# print(headline("use mypy", align="center"))

## this doesn't pass type checking

# headlines.py

def headline(text: str, centered: bool = False) -> str:
    if centered:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "o")

print(headline("python type checking"))
print(headline("use mypy", centered=True))

# passes mypy

