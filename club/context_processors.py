from models import Club


def club_processor(request):
    club = Club.objects.last()
    return {'club': club}
