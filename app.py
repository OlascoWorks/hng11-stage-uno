from flask import Flask, request
import requests, os

app = Flask(__name__)
API_KEY = os.environ.get('API_KEY')

@app.route('/api/hello')
def api():
    visitor_name = request.args.get("visitor_name")
    ip = request.remote_addr
    
    weather_info = requests.get(f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={ip}&aqi=no")
    location = weather_info.json()['location']['region']
    temp = weather_info.json()['current']['temp_c']'
    
    payload = {
		"client_ip": ip
		"location": location
		"greeting": f"Hello, {visitor_name}!, the temperature is {temp} degrees Celcius in {location}"
	}
    return payload

if __name__ == "__main__":
    app.run()
    
#Response:
# {
#   "client_ip": "127.0.0.1", // The IP address of the requester
#   "location": "New York" // The city of the requester
#   "greeting": "Hello, Mark!, the temperature is 11 degrees Celcius in New York"
#}