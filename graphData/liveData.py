import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from urllib.request import urlopen
import json
import time
from allData import url

arrSeconds = []
arrData = []

fig = plt.figure() # initialise la figure
line, = plt.plot([], []) 

def animate(i): 
    response = urlopen(url)
    data_json = json.loads(response.read())
    arrData.append(data_json[len(data_json) - 1]["data_esp32"])
    arrSeconds.append(i)
    plt.plot(arrSeconds, arrData)
    print(data_json[len(data_json)-1]["data_esp32"], "seconds = ", i)
    return line,


ani = animation.FuncAnimation(fig, animate, frames=100, blit=True, interval=1000, repeat=False)

plt.show()
