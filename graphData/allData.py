from urllib.request import urlopen
import json
import matplotlib.pyplot as plt


url = "http://cyrilserver.ddns.net:8080/hardware/esp32/all"
  
# store the response of URL
response = urlopen(url)
arrData = []
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
for i in range(len(data_json)):
    arrData.append(data_json[i]['data_esp32'])

plt.plot(arrData)
plt.show()
# print the json response