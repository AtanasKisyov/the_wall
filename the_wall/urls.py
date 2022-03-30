from django.contrib import admin
from django.urls import path

from the_wall.api_app.views import WallView, SpecificDayOverviewView, SpecificProfileAndDayOverviewView, \
    AllDaysOverviewView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profiles/<int:profile>/days/<int:day>', WallView.as_view()),
    path('profiles/<int:profile>/overview/<int:overview>', SpecificProfileAndDayOverviewView.as_view()),
    path('profiles/overview/<int:overview>', SpecificDayOverviewView.as_view()),
    path('profiles/overview/', AllDaysOverviewView.as_view()),
]
