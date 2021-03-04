import re

pattern = r'\br[a-z-]+'

#  \(\d{3}\)
#  [(]\d{3}[)]

rx = re.compile(pattern, re.I)

with open("DATA/alice.txt") as alice_in:
    all_text = alice_in.read()

def make_replacement(match):
    text = match.group()  # text that was matched
    if text.isupper():
        return "**" + text + "**"
    elif text.islower():
        return text.upper()
    else:
        return text

#                   callback
#                  text-or-func
new_text = rx.sub(make_replacement, all_text)
# for m in rx.finditer(all_text):
#     all_text = rx.sub(make_replacement(m), all_text)


with open('alice_r.txt', 'w') as alice_out:
    alice_out.write(new_text)


print(rx.findall(all_text))



