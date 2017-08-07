from django.shortcuts import render
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
import re


def get_schedule(request):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    # Create a variable with the URL
    url = 'http://www.kdul.ie/roundup.aspx?oid=1012&show=f&cid=10095'

    # Scrape the HTML at the url
    try:
        r = requests.get(url, headers=headers, timeout=5)

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

    except Exception as e:
        messages.error(request, "The connection to KDUL.ie failed. " + str(e))
        games_list = []

    url2 = 'http://kdfl.ie/fixtures2016.php'

    try:
        r2 = requests.get(url2, headers=headers, timeout=5)
        if r2.status_code != 200:
            l_list = ['WHAT']

        else:
            l_list = []
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
            for l in line_list:
                line = l
                line_date = l.findPreviousSibling(text=datepattern)
                division = l.findPreviousSibling(text=divisionpattern)
                if line is not None:
                    line_details = [line, division, line_date]
                    l_list.append(line_details)

    except Exception as e:
        messages.error(request, "The connection to KDFL.ie failed. " + str(e))
        l_list = []

    args = {
        'Line': l_list,
        'games_list': games_list,
    }
    return render(request, 'schedule/schedule.html', args)

