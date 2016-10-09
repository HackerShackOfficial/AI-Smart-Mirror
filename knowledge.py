import requests
import json
import feedparser
import datetime


class Knowledge(object):
    def __init__(self, weather_api_token, news_country_code='us'):
        self.news_country_code = news_country_code
        self.weather_api_token = weather_api_token

    def find_weather(self):
        loc_obj = self.get_location()

        lat = loc_obj['lat']
        lon = loc_obj['lon']

        weather_req_url = "https://api.darksky.net/forecast/%s/%s,%s" % (self.weather_api_token, lat, lon)
        r = requests.get(weather_req_url)
        weather_json = json.loads(r.text)

        temperature = int(weather_json['currently']['temperature'])

        current_forecast = weather_json['currently']['summary']
        hourly_forecast = weather_json['minutely']['summary']
        daily_forecast = weather_json['hourly']['summary']
        weekly_forecast = weather_json['daily']['summary']
        icon = weather_json['currently']['icon']
        wind_speed = int(weather_json['currently']['windSpeed'])

        return {'temperature': temperature, 'icon': icon, 'windSpeed': wind_speed, 'current_forecast': current_forecast, 'hourly_forecast': hourly_forecast, 'daily_forecast': daily_forecast, 'weekly_forecast': weekly_forecast}

    def get_location(self):
        # get location
        location_req_url = "http://freegeoip.net/json/%s" % self.get_ip()
        r = requests.get(location_req_url)
        location_obj = json.loads(r.text)

        lat = location_obj['latitude']
        lon = location_obj['longitude']

        return {'lat': lat, 'lon': lon}

    def get_ip(self):
        ip_url = "http://jsonip.com/"
        req = requests.get(ip_url)
        ip_json = json.loads(req.text)
        return ip_json['ip']

    def get_map_url(self, location, map_type=None):
        if map_type == "satellite":
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=13&scale=false&size=1200x600&maptype=satellite&format=png" % location
        elif map_type == "terrain":
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=13&scale=false&size=1200x600&maptype=terrain&format=png" % location
        elif map_type == "hybrid":
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=13&scale=false&size=1200x600&maptype=hybrid&format=png" % location
        else:
            return "http://maps.googleapis.com/maps/api/staticmap?center=%s&zoom=13&scale=false&size=1200x600&maptype=roadmap&format=png" % location

    def get_news(self):
        ret_headlines = []
        feed = feedparser.parse("https://news.google.com/news?ned=%s&output=rss" % self.news_country_code)

        for post in feed.entries[0:5]:
            ret_headlines.append(post.title)

        return ret_headlines

    def get_holidays(self):
        today = datetime.datetime.now()
        r = requests.get("http://kayaposoft.com/enrico/json/v1.0/?action=getPublicHolidaysForYear&year=%s&country=usa" % today.year)
        holidays = json.loads(r.text)

        return holidays

