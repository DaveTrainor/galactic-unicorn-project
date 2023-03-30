from app.screen import load_screen
import time
import network
import settings
from urequests import get as http_get

screen = settings.screen

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(
    settings.wifi_access_point,
    settings.wifi_password
)

while not wlan.isconnected():
    print('Waiting for connection...')
    time.sleep(1)

ip_address, subnet, gateway, dns = wlan.ifconfig()
print(f'ip: {ip_address}\ngateway: {gateway}')

r = http_get("https://api.open-meteo.com/v1/forecast?latitude=53.55&longitude=2.01&current_weather=true&hourly"
             "=temperature_2m,relativehumidity_2m,windspeed_10m")

temp = str(r.json()['current_weather']['temperature'])

# temp = str(10.0)
temp_display = temp + '°C'
colour = 'GREEN'
if float(temp) >= 20:
    colour = 'RED'
if float(temp) <= 4:
    colour = 'BLUE'

screen = load_screen(screen.get('driver'))
screen().show_text(temp_display, 'centre', colour)
