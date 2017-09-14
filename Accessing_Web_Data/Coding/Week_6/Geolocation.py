import urllib.request
import urllib.parse
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    #add the parameters needed to the url
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})

    uh = urllib.request.urlopen(url)
    data = uh.read().decode('utf8')

    js = json.loads(str(data))

    #print the response, enable for debug
    #print json.dumps(js, indent=4)

    #extract place_id
    place_id = js["results"][0]['place_id']
    print (place_id)
