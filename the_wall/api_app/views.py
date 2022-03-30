from rest_framework import views as rest_views
from rest_framework.response import Response

from the_wall.api_app.helper import calculate_needed_ice_cubic_yards, \
    calculate_needed_gold_for_specific_profile_and_day, calculate_needed_gold_for_specific_day, \
    calculate_needed_gold_for_all_days


class WallView(rest_views.APIView):

    def get(self, request, profile, day):
        result = calculate_needed_ice_cubic_yards(profile, day)
        print(result)
        return Response({"day": day, "ice_amount": result})


class SpecificProfileAndDayOverviewView(rest_views.APIView):

    def get(self, request, profile, overview):
        result = calculate_needed_gold_for_specific_profile_and_day(profile, overview)
        return Response({"day": overview, "cost": result})


class SpecificDayOverviewView(rest_views.APIView):

    def get(self, request, overview):
        result = calculate_needed_gold_for_specific_day(overview)
        return Response({"day": overview, "cost": result})


class AllDaysOverviewView(rest_views.APIView):

    def get(self, request):
        result = calculate_needed_gold_for_all_days()
        return Response({"day": None, "cost": result})
