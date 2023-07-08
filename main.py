#ISS Overhead Notifier

import requests
from datetime import datetime


MY_LAT = 12.971599
MY_LONG = 77.594566


def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #My Position
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True



#Figuring out whether it is a night time or not

def isnight():


    parameters = {
        "lat":MY_LAT,
        "lng": MY_LONG,
        "formatted":0
    }

    response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise= int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset "].split("T")[1].split(":")[0])
    #
    time_now = datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
        return True
    print(data)
# iss_latitude = float(data["is_position"]["latitude"])
# iss_longitute = float(data["is_position"]["longitute"])

#


# print(f"Sunrise: {sunrise}\nSunset: {sunset}")

# hour = sunrise.split("T")[1].split(":")[0]

# print(hour)





# response = requests.get("https://api.kanye.rest")
# print(f"Response Code {response.status_code}")
# data = response.json()
# quote=data["quote"]
# print(f"Here's your quote : {quote}")