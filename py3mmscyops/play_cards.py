from carddeck import CardDeck
from jokerdeck import JokerDeck
d1 = CardDeck("Fred")
print(d1)

d2 = CardDeck("Bob")
print(d2)

print(d1.dealer)
# d1.get_dealer()

d1.dealer = "Mary"
print(d1.dealer)

try:
    d1.dealer = 1.2
except TypeError as err:
    print(err)
else:
    print(d1.dealer)

try:
    d3 = CardDeck(b'abc')
except TypeError as err:
    print(err)
else:
    print(d3)

d1.shuffle()
print(d1.cards)

for _ in range(10):
    print(d1.draw())
print()

# for _ in range(50):
#     print(d1.draw())

print(len(d1))

print(d1)
# print(str(d1))

print(repr(d1))

d4 = d1 + d2

print(d4)

j1 = JokerDeck("Frank")
print(j1)
print(JokerDeck.mro())
j1.shuffle()
print(j1.cards)
