from django.shortcuts import render
import requests
from home.views import Team
from bs4 import BeautifulSoup
import re


def get_schedule(request):
    # Create a variable with the URL
    url = 'http://www.kdul.ie/roundup.aspx?oid=1012&show=f&cid=10095'

    # Scrape the HTML at the url
    r = requests.get(url)

    # Turn the HTML into a Beautiful Soup object
    soup = BeautifulSoup(r.content, 'html.parser')

    # find all active games using the class
    games = soup.find_all(class_='ui-state-default')
    # create an empty list
    games_list = []
    for game in games:
        # get date and league using previous sibling
        date = game.findPreviousSibling(class_='ui-widget-header').get_text()
        league = game.findPreviousSibling().get_text()
        # find all columns in the games row and turn them into text
        row = game.find_all('td')
        home = row[0].get_text()
        away = row[3].get_text()
        venue = row[4].get_text()
        time = row[5].get_text()
        # use all the text to use them for details in games list
        details = [home, away, venue, time, league, date]
        games_list.append(details)

    url2 = 'http://kdfl.ie/fixtures2016.php'
    r2 = requests.get(url2)

    pattern = re.compile('Straffan')
    datepattern = re.compile('2017')
    divisionpattern = re.compile('Division')

    kdfl = BeautifulSoup(r2.content, 'html.parser')
    kdfltable = kdfl.find(id='kdflfixtures')
    kdflbr = kdfltable.find_all('br')
    line_list = []
    for i in kdflbr:
        pline = i.findPreviousSibling(text=pattern)
        if pline is not None:
            line_list.append(pline)
    # to remove duplicates
    line_list = list(set(line_list))
    l_list = []
    for l in line_list:
        line = l
        line_date = l.findPreviousSibling(text=datepattern)
        division = l.findPreviousSibling(text=divisionpattern)
        if line is not None:
            line_details = [line, division, line_date]
            l_list.append(line_details)

    args = {
        'Line': l_list,
        'games_list': games_list,
        'teams': Team.objects.all()
    }
    return render(request, 'schedule/schedule.html', args)

