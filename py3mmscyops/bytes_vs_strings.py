
s = "65\u00B0 in Durham"
print(s)
print(len(s))

b = s.encode()
print(b)
print(len(b))
print(s[0], b[0])
print(list(s))
print(list(b))

value = b'abc'
s2 = value.decode('utf-8', 'replace')
print(value, repr(s2))


