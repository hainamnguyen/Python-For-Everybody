import urllib.request
import xml.etree.ElementTree as ET

while True:
    url = input('Enter location: ')
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read()

    tree = ET.fromstring(data)
    #print(tree) 
    results = tree.findall('comments/comment')
    print('Count: ' + str(len(results)))
    sumResult = 0
    for item in results:
        sumResult += int(item.find('count').text)
    print('Sum: ' + str(sumResult))
