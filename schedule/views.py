from django.shortcuts import render
from lxml import html
import requests
from home.views import Team
from bs4 import BeautifulSoup
import pandas as pd


def get_schedule(request):
    return render(request, 'schedule/schedule.html', {'teams': Team.objects.all()})


'''def get_schedule(request):
    # Create a variable with the URL
    url = 'http://www.kdul.ie/roundup.aspx?oid=1012&show=f&cid=10095'

    # Scrape the HTML at the url
    r = requests.get(url)


    # Turn the HTML into a Beautiful Soup object
    soup = BeautifulSoup(r.text, 'html')

    # Create variables to store the scraped data in
    home = []
    away = []
    venue = []
    time = []
    referee = []

    # Create an object of the first object that is class=jtable
    table = soup.find(class_='jtable')

    # Find all the <tr> tag pairs, skip the first one, then for each.
    for row in table.find_all('tr')[1:]:
        game = row.find_all('td')
        try:
            column_1 = game[0].string.strip()
            home.append(column_1)
        except IndexError:
            home.append('')
        # Create a variable of all the <td> tag pairs in each <tr> tag pair,
        try:
            column_2 = game[3].string.strip()
            away.append(column_2)
        except IndexError:
            away.append('')
        try:
            column_3 = game[4].string.strip()
            venue.append(column_3)
        except IndexError:
            venue.append('')
        try:
            column_4 = game[5].string.strip()
            time.append(column_4)
        except IndexError:
            time.append('')
        except AttributeError:
            time.append('')
        try:
            column_5 = game[6].string.strip()
            referee.append(column_5)
        except IndexError:
            referee.append('')
        except AttributeError:
            referee.append('')

    args = { #  'game': game, 'home': home, 'away': away, 'venue': venue, 'time': time, 'referee': referee,
            'teams': Team.objects.all().order_by("-name")}

    return render(request, 'schedule/schedule.html', args)'''


'''def get_schedule(request):
    page = requests.get('http://www.kdul.ie/roundup.aspx?oid=1012&show=f&cid=10095')
    tree = html.fromstring(page.content)
    # // *[ @ id = "body"] / div / section / div[5] / table / thead
    headerrow = tree.xpath('// *[ @ id = "body"] / div / section / div[5] / table / thead//text()')
    home = headerrow[0]
    away = headerrow[1]
    venue = headerrow[2]
    time = headerrow[3]
    referee = headerrow[4]
    args = {
        'home': home,
        'away': away,
        'venue': venue,
        'time': time,
        'referee': referee,
        'teams': Team.objects.all().order_by("-name")
    }
    return render(request, 'schedule/schedule.html', args)

# http://python-guide-pt-br.readthedocs.io/en/latest/scenarios/scrape/
# need to expand on this when schedules are posted
# in xpath // at the end of an expression  selects all children and text() returns just the text

# //*[@id="body"]/div/section/div[5]/table/tbody
# //*[@id="body"]/div/section/div[5]/table/tbody/tr[1]
# body > div > section > div:nth-child(5) > table > tbody > tr:nth-child(2) > td

# //*[@id="body"]/div/section/div[5]/table/tbody/tr[2]/td
# //*[@id="body"]/div/section/div[5]

# body > div > section > div:nth-child(5) > table'''

'''# Find all the <tr> tag pairs, skip the first one, then for each.
for row in table.find_all('tr')[1:]:
    # Create a variable of all the <td> tag pairs in each <tr> tag pair,
    col = row.find_all('td')

    # Create a variable of the string inside 1st <td> tag pair,
    column_1 = col[0].string.strip()
    # and append it to home variable
    home.append(column_1)

    # Create a variable of the string inside 4nd <td> tag pair,
    try:
        column_2 = col[3].string.strip()
        # and append it to away variable
        away.append(column_2)
    except IndexError:
        continue

    # Create a variable of the string inside 5th <td> tag pair,
    column_3 = col[4].string.strip()
    # and append it to venue variable
    venue.append(column_3)

    # Create a variable of the string inside 6th <td> tag pair,
    column_4 = col[5].string.strip()
    # and append it to time variable
    time.append(column_4)

    # Create a variable of the string inside 7th <td> tag pair,
    column_5 = col[6].string.strip()
    # and append it to referee variable
    referee.append(column_5)

# Create a variable of the value of the columns
args = {'home': home, 'away': away, 'venue': venue, 'time': time, 'referee': referee,
        'teams': Team.objects.all().order_by("-name")}

return render(request, 'schedule/schedule.html', args)'''

