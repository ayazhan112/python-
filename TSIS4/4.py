import re
x = re.search(r'([a-zA-Z0-9])\1+', input())
if x:
    print(x.group(1))
else:
    print(-1)