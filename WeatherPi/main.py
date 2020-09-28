import requests
import json

def getparams():
    ret = None
    with open('params.json', 'r') as file:
        ret = json.load(file)
    return ret

URL = "http://api.weatherapi.com/v1/current.json"
parms = getparams()

def main():
    global URL
    global parms 
    get = requests.get(url = URL, params = parms)
    data = get.json()
    print(data['current']['condition']['text'])
    return

if __name__ == "__main__":
    main()
