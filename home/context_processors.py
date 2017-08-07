from models import Team


def teams_processor(request):
    teams = Team.objects.all()
    return {'teams': teams}

