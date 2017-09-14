import re
import os
try:
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'regex_sum_347350.txt')
    text = open(filename)
except:
    print(' File cannot be opened')
    exit()
sum = 0
for line in text:
    number = map(int, re.findall('[0-9]+', line))
    for i in number:
        sum += i
print(sum)
