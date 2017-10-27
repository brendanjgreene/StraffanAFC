from models import Subject


def news_processor(request):
    news = Subject.objects.all().order_by('team')
    return {'news': news}
