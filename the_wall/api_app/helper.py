from the_wall.settings import BASE_DIR

# Constants
CONFIG_FILE = BASE_DIR / 'the_wall/api_app/files/config.txt'
FILE_MODE = 'r'
SINGLE_ROW = 1
VALUE_TO_MATCH_INDEX = 1
FEET_BY_DAY = 1
CALCULATIONS_INITIAL_VALUE = 0
SECTION_MAX_VALUE = 30
CALCULATION_VALUES = {'days': 195, 'overview': 1900}
ICE_CUBIC_YARDS_PER_FOOT = 195
GOLDEN_DRAGON_COINS_PER_FOOT = 1900


def get_file_length(file):
    """
    Read file length for easier iteration
    :param file: String (path to file)
    :return: File rows count (Integer)
    """
    with open(file, FILE_MODE) as f:
        return sum(SINGLE_ROW for _ in f)


def get_wall_profiles():
    """
    Read wall profiles from config.txt and return the result
    :return: list of integers
    """
    result = []
    with open(CONFIG_FILE, FILE_MODE) as file:
        file_length = get_file_length(CONFIG_FILE)
        for _ in range(file_length):
            row = [int(x) for x in file.readline().split()]
            result.append(row)
        return result


def calculate_needed_ice_cubic_yards(profile, days):
    """
    Calculate needed ice for specified wall profile and specified day of construction
    :param profile: Integer
    :param days: Integer
    :return: Integer
    """
    result = CALCULATIONS_INITIAL_VALUE
    wall_profiles = get_wall_profiles()
    current_profile = wall_profiles[profile - VALUE_TO_MATCH_INDEX]
    for day in range(days):
        current_profile = [x + FEET_BY_DAY for x in current_profile if x < SECTION_MAX_VALUE]
        result += sum(ICE_CUBIC_YARDS_PER_FOOT for _ in current_profile)
    return result


def calculate_needed_gold_for_specific_profile_and_day(profile, days):
    return calculate_needed_ice_cubic_yards(profile=profile, days=days) * GOLDEN_DRAGON_COINS_PER_FOOT


def calculate_needed_gold_for_specific_day(day):
    """
    Calculate needed gold for all wall profiles and specified day of construction
    :param day: Integer
    :return: Integer
    """
    result = CALCULATIONS_INITIAL_VALUE
    wall_profiles = get_wall_profiles()
    for day in range(day):
        for current_profile in wall_profiles:
            result += sum([GOLDEN_DRAGON_COINS_PER_FOOT * ICE_CUBIC_YARDS_PER_FOOT for x in current_profile])
    return result


def calculate_needed_gold_for_all_days():
    """
    Calculate needed gold for the entire wall construction
    :return: Integer
    """
    result = CALCULATIONS_INITIAL_VALUE
    wall_profiles = get_wall_profiles()
    for current_profile in wall_profiles:
        result += sum([(SECTION_MAX_VALUE - x) * GOLDEN_DRAGON_COINS_PER_FOOT * ICE_CUBIC_YARDS_PER_FOOT
                       for x in current_profile])
    return result
