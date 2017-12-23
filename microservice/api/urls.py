from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from api.views import home, justdatabase

urlpatterns = [
    url(r'^$', home, name = 'home'),
    url(r'^justdatabase$', justdatabase, name = 'justdatabase'),
    ]
