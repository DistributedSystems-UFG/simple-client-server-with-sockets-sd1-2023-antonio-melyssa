from socket import *
import json
from constCS import *

HOST = '127.0.0.1'  # Replace with the appropriate host address
PORT = 8080  # Replace with the appropriate port number

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

# Create the API request payload
request_payload = {
    "days": 2,
    "location": "Goiania",
    "action": "weather"   # forecast / time / now
}
request_data = json.dumps(request_payload)

s.send(str.encode(request_data))  # send the request data
data = s.recv(1024)               # receive the response
print(bytes.decode(data))         # print the result

s.close()                         # close the connection
