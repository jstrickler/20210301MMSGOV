import re
#  919-123-4567
#  (919) 123-4567
#  919.123.

#  r'\d{10}(?=[:;])'

nums = """(123) 456-7890
1234567890
123-456-7890
123-45-8302
123-456-789
123 456 7890
123.456.7890""".split('\n')

tele_pattern = r"\b\(?\d{3}\)?[ -.]?\d{3}[ .-]?\d{4}\b"
rx_tele = re.compile(tele_pattern)

for num in nums:
    print(num, "MATCHED" if rx_tele.fullmatch(num) else "NO MATCH")

