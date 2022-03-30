from django import test as django_test

from the_wall.api_app.helper import calculate_needed_ice_cubic_yards, \
    calculate_needed_gold_for_specific_profile_and_day, calculate_needed_gold_for_specific_day, \
    calculate_needed_gold_for_all_days


class WallAPITests(django_test.TestCase):

    def test_ice_value_after_fourth_day_for_first_profile(self):
        expected = 1950
        actual = calculate_needed_ice_cubic_yards(profile=1, days=4)
        self.assertEqual(expected, actual)

    def test_ice_value_after_first_day_for_second_profiles(self):
        expected = 195
        actual = calculate_needed_ice_cubic_yards(profile=2, days=1)
        self.assertEqual(expected, actual)

    def test_gold_value_after_second_day_for_first_profile(self):
        expected = 2223000
        actual = calculate_needed_gold_for_specific_profile_and_day(profile=1, days=2)
        self.assertEqual(expected, actual)

    def test_gold_value_after_fourth_day_for_second_profile(self):
        expected = 1482000
        actual = calculate_needed_gold_for_specific_profile_and_day(profile=2, days=4)
        self.assertEqual(expected, actual)

    def test_gold_value_after_third_day_for_all_profile(self):
        expected = 10003500
        actual = calculate_needed_gold_for_specific_day(day=3)
        self.assertEqual(expected, actual)

    def test_gold_value_for_finishing_all_profiles(self):
        expected = 32233500
        actual = calculate_needed_gold_for_all_days()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    WallAPITests()
