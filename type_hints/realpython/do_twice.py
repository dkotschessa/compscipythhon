from typing import Callable

def do_twice(func: Callable[[str], str], argument:str) -> None:
    print(func(argument))
    print(func(argument))

def create_greeting(name: str) -> str:
    return f"Hello {name}"


do_twice(create_greeting, "Jekyll")