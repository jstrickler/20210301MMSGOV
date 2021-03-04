from typing import Iterable, Dict, Union, List

NUMERIC = Union[int, float]

def spam(a: NUMERIC, b: NUMERIC) -> NUMERIC:
    return a ** b

print(spam(2, 5))
print(spam(5, 2))

print(spam('a', 'b'))

def ham(values: Dict[str, float]) -> List[tuple]:
    pass


