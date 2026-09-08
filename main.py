import requests
import os
import smtplib

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
weather_params = {
    "lat": 44.513317,
    "lon": -88.013298,
    "appid": api_key,
    "cnt": 4,
}

MY_EMAIL = os.environ.get("GMAIL_EMAIL")
PASSWORD = os.environ.get("GMAIL_PASSWORD")

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for check in weather_data['list']:
    if check['weather'][0]['id'] < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="jaguitar75@gmail.com",
            msg=f"Subject: Rain Incoming ☔️\n\nWarning: Rain is coming today. Make sure to bring an umbrella!"
        )
        connection.close()
