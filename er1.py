import re
s = 'jsm.forjsm'
# without using \
match = re.search(r'.', s)
print(match)
# using \
match = re.search(r'\.', s)
print(match)