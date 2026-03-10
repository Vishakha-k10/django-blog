from .models import Category
from extrafeatures.models import Sociallink


def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_link= Sociallink.objects.all()
    return dict(social_link=social_link)
