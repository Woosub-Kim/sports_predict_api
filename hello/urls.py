from django.urls import path
from hello import views
urlpatterns = [
    path("",views.home, name="home"),
    path("KBO",views.KBO, name="KBO"),
    path("MLB",views.MLB, name="MLB"),
    path("NBA",views.NBA, name="NBA"),
    path("house",views.house, name="house"),
]
