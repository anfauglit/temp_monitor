import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import time

URL = 'https://www.gismeteo.ru/'

plt.ion()
fig, ax = plt.subplots()

temp_data = []
time_data = []

start_time = time.time()	
first_time = True
while (1):
	if (time.time() - start_time >= 60 or first_time):
		first_time = False
		start_time = time.time()
		page = requests.get(URL, headers = {'User-agent': 'Mozilla/5.0 (Windows NT \
		10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 \
		Safari/537.36'})

		soup = BeautifulSoup(page.content, 'html.parser')

		target = soup.find_all('div', class_='js_meas_container temperature')

		try:
			current_temp = float(target[0]['data-value'])
		except IndexError:
			continue

		temp_data.append(current_temp)
		time_data.append(start_time)

		ax.scatter(time_data, temp_data, c='r')
		

		fig.canvas.draw()
		fig.canvas.flush_events()
