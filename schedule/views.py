from django.shortcuts import render
from lxml import html
import requests
from home.views import Team
from bs4 import BeautifulSoup
import pandas as pd


'''def get_schedule(request):
    return render(request, 'schedule/schedule.html', {'teams': Team.objects.all()})'''


def get_schedule(request):
    # Create a variable with the URL
    url = 'http://www.kdul.ie/roundup.aspx?oid=1012&show=f&cid=10095'

    # Scrape the HTML at the url
    r = requests.get(url)

    # Turn the HTML into a Beautiful Soup object
    soup = BeautifulSoup(r.content, 'html.parser')
    games = soup.find_all(class_='ui-state-default')
    games_list = []
    for game in games:
        date = game.findPreviousSibling(class_='ui-widget-header').get_text()
        league = game.findPreviousSibling().get_text()
        row = game.find_all('td')
        home = row[0].get_text()
        away = row[3].get_text()
        venue = row[4].get_text()
        time = row[5].get_text()
        details = [home, away, venue, time, league, date]
        games_list.append(details)

    args = {'games_list': games_list,
            'teams': Team.objects.all()
    }
    return render(request, 'schedule/schedule.html', args)

