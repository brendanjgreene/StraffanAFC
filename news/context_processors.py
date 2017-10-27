from models import Subject


def news_processor(request):
    news = Subject.objects.all()
    return {'news': news}
