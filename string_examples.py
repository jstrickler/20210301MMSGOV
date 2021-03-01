
s1 = "spam\n"
s2 = 'spam\n'
print("Bob's your uncle")
print('The "heart" of the matter')
s3 = """spam\n"""
s4 = '''spam\n'''

print("""Bob's your "favorite" uncle""")
s5 = r"spam\n"  # don't interpret backslash
print(s5)

print("77\u00B0 F in Durham today")
data = ['\U0001F95A', '\U0001F414']
print(sorted(data))

actor = "Chris Hemsworth"
print(len(actor))
print(actor.upper())
print(actor.count('h'))
print(actor.lower().count('h'))

name = "Bobxxxxxxxxx"
print(name.rstrip('x'))
name = "     \t    Bob"
print(name.lstrip())
s = "xyxxxxyyyyyyxyxxyyAll my exes live in Texasyyxyyyxyxyyyxxy"
print(s.strip('xy'))

s = "Python Rocks! "
print(s * 5)
x = "wom"
y = "bat"
print(x + y)

print('th' in s, 'sh' in s)
print('py' in s, 'py' in s.lower())

print(actor)
print(actor[0], actor[5], actor[-1], actor[-3])
print(actor[0:5])
print(actor[:5])
print(actor[6:9])
print(actor[8:])
print(actor[-4:])  # last 4 characters

print(actor[::])

x = "this is a test"
print(x.split())
y = "a:b:wombat:c"
print(y.split(':'))
print(list(actor))




















