from django.apps import apps as django_apps


def get_sidebar_context(request):
    sport_model = django_apps.get_model('sports', 'Sport')
    sports = sport_model.objects.all().order_by('name')

    return {
        'sports': sports,
    }
