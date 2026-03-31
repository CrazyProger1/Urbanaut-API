from src.apps.news.models import News


def get_all_news():
    return News.objects.all()


def get_published_news():
    return News.objects.filter(is_published=True)
