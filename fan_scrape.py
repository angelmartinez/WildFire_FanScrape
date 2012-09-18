import requests
import json

FILE_LOCATION = '/Users/Angel/VM/test/'

     
print("Oh hai bro! Let's scrape")
print("")
url= raw_input("Give me the URL of the monitor link you want to scrape: ")
print("")
brand = raw_input("Name of brand page (this is going to be the name of the actual file ie. 'ge_fan.csv'): ")
print("")

print("Awesome! I'm going to work right now!")

r = requests.get(url, verify=False)


data = json.loads(r.content)

data = data[data.keys()[0]]



# Extract user_likes_count and dump to csv

fout = open(FILE_LOCATION+brand+'_fan.csv', 'w')

for datapoint in data.get('fan_count'):

    date, count = datapoint

    fout.write('{},{}\n'.format(date, count))

fout.close()

print("BOOM fan size is donzo!")
print("")





