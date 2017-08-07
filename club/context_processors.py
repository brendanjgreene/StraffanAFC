from models import Club


def club_processor(request):
    club = Club.objects.first()
    return {'club': club}
