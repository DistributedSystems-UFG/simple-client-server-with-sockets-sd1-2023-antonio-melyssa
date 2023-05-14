from socket import *
import requests
import json
from constCS import *


def getTime():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer YjNkNzVjY2QtMzEyNy00ZDgxLTgyODUtYjdkZWU2N2Y0MmU2'
    }

    try:
        response = requests.post(
            'https://api.m3o.com/v1/time/Now', headers=headers)
        if response.status_code == 200:
            result = response.json()

            # Process the API response and send it back to the client
            localtime = result.get('localtime', '')
            timestamp = result.get('timestamp', '')
            location = result.get('location', '')
            timezone = result.get('timezone', '')
            unix = result.get('unix', '')

            message = f"Time in {location}: {localtime} ; Timestamp: {timestamp} ; Timezone: {timezone} ; Unix: {unix}"
            return message
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


def getWeatherForecast(data):
    request_data = bytes.decode(data).strip()

    # Call the API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer YjNkNzVjY2QtMzEyNy00ZDgxLTgyODUtYjdkZWU2N2Y0MmU2'
    }

    try:
        response = requests.post(
            'https://api.m3o.com/v1/weather/Forecast', headers=headers, data=request_data)
        if response.status_code == 200:
            result = response.json()

            # Process the API response and send it back to the client
            forecast_data = result.get('forecast', '')
            location = result.get('location', '')

            message = f"Weather forecast for {location}: {forecast_data}"
            return message
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


def getWeatherNow(data):
    request_data = bytes.decode(data).strip()

    # Call the API
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer YjNkNzVjY2QtMzEyNy00ZDgxLTgyODUtYjdkZWU2N2Y0MmU2'
    }

    try:
        response = requests.post(
            'https://api.m3o.com/v1/weather/Now', headers=headers, data=request_data)
        if response.status_code == 200:
            result = response.json()

            # Process the API response and send it back to the client
            location = result.get('location', '')

            message = f"Weather Now for {location}: {result}"
            return message
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


HOST = '127.0.0.1'  # localhost
PORT = 8080  # porta 8080

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
(conn, addr) = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break

    #response = getWeatherForecast(data)
    #response = getTime()
    response = getWeatherNow(data)
    conn.send(str.encode(response))


conn.close()
# close the connection


#
