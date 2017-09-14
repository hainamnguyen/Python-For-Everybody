import re
text = open("mbox.txt", 'r')
text = open('regex_sum_347350.txt', 'r')
sum1 = 0
for line in text:
    number = re.findall('[0-9]+', line)
    number = map(int, number )
    smallSum = sum(number)
    sum1 += smallSum
print(sum1)
