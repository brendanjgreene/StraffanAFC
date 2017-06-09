from django.shortcuts import render
from lxml import html
import requests
from home.views import Team


def get_schedule(request):
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


