import re
x = re.findall(r'[^aeiou]([aeiouAEIOU]{2,})(?=[^aiueo])', input())
if x:
    print('\n'.join(x))
else:
    print(-1)