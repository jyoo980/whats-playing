import json
import time
from time import strftime

def format_date():
    month_day_year = "%m/%d/%Y"
    date_today = time.localtime()
    return strftime(month_day_year, date_today)

def parse_theatre(theatre):
    with open('theatres.json') as file:
        data = json.load(file)

    return data[theatre]

def request_url(theatre):
    current_date = format_date()
    theatre = parse_theatre(theatre)
    base_url = "https://www.cineplex.com/Showtimes/any-movie/{0}?Date={1}"
    base_url = base_url.replace("{0}", theatre)
    base_url = base_url.replace("{1}", current_date)
    return base_url
