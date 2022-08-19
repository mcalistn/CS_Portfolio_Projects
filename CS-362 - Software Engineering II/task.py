def conv_num(num_str):
    """Takes in a string and converts it into a base 10 number."""
    # Returns None if num_str is empty or not a string
    if not num_str or isinstance(num_str, str) is False:
        return None
    # Returns None if num_str is a hex but does not have '0x' prefix
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in num_str:
        if i in alphabet and num_str[0] != '0' and num_str[1] != 'x':
            return None
    # Returns None if number of decimals is greater than one
    dec_count = 0
    for i in num_str:
        if i == '.':
            dec_count += 1
        if dec_count > 1:
            return None
    # Converts hex string to base 10 number
    if num_str[0] == '0' and num_str[1] == 'x':
        return hex_converter(num_str)
    # Converts int or float string to base 10 number
    else:
        return int_float_converter(dec_count, num_str)


def hex_converter(num_str):
    """Helper function to handle hex conversion for conv_num."""
    hex_list = "0123456789ABCDEF"
    num_conv = 0
    for i, j in enumerate(num_str):
        if i < 2:
            continue
        if j not in hex_list:
            return None
        value = hex_list.index(j)
        pwr = len(num_str) - (i + 1)
        num_conv += value * 16 ** pwr
    return num_conv


def int_float_converter(dec_count, num_str):
    """Helper function to handle int and float conversion for conv_num."""
    # Checks if number is negative
    is_neg = False
    # Sets is_neg to True if number is negative
    if num_str[0] == '-':
        num_str = num_str[1:]
        is_neg = True
    num_conv = 0
    dec_conv = 0
    # Create a copy of num_str if no decimals
    if dec_count == 0:
        num_copy = num_str
    # Split the numbers to the left and right of decimal
    if dec_count == 1:
        num_copy, dec = num_str.split('.')
        dec_conv = dec_converter(dec_conv, dec)
    if dec_count == 0 or dec_count == 1:
        num_conv, multiplier = num_converter(num_copy, num_conv)
    # Combines the number and decimal digits
    num_conv *= 10 ** multiplier
    if dec_count == 1:
        num_conv += dec_conv
    # Sets number to negative if is_neg is True
    if is_neg is True:
        return num_conv * -1
    return num_conv


def num_converter(num_copy, num_conv):
    """Helper function that handles int conversion for conv_num."""
    # Converts the number digits
    num_list = '0123456789'
    index = len(num_copy) - 1
    multiplier = index
    for i in range(len(num_list)):
        if index < 0:
            break
        num_conv /= 10
        num_conv += num_list.index(num_copy[index])
        index -= 1
    return num_conv, multiplier


def dec_converter(dec_conv, dec):
    """Helper function that handles decimal conversion for conv_num."""
    # Converts the decimal digits
    num_list = '0123456789'
    index = len(dec) - 1
    for i in range(len(num_list)):
        if index < 0:
            break
        dec_conv /= 10
        dec_conv += num_list.index(dec[index])
        index -= 1
        if index < 0:
            dec_conv /= 10
    return dec_conv


def my_datetime(num_sec):
    """
    Takes one parameter: seconds(int): returns a date(string) that is the parameter seconds into
     the future starting at 01-01-1970.
     Ex: if 0 seconds, return 01-01-1970
    """
    if num_sec == 0:
        return '01-01-1970'
    # get days from seconds
    days = seconds_to_days(num_sec)
    # get year and left over days from days
    (year, left_over_days) = days_to_years(days)
    # get day and month from days and year
    month_day = days_to_months(left_over_days, year)
    return month_day + str(year)


def check_leap_year(year):
    """
    A function that takes a year  as a parameter and returns true if its a leap year or false if not
    Reference: https://en.wikipedia.org/wiki/Leap_year#Algorithm
    """
    # case for leap year
    if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
        return True
    # return case for normal year otherwise
    return False


def days_month_to_string(month, day):
    """
    Takes a month(index) and day ints and returns their string value
    examle: month = 2 and day = 7 would return the string "03-07-"
    """

    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    day_string = str(day)
    # case for if day is a single digit
    if day < 10:
        day_string = "0" + day_string
    month_day_string = months[month] + "-" + day_string + "-"
    return month_day_string


def days_to_months(days, year=1970):
    """
    Takes days and year as a parameter. Need year as a parameter to check if leap year
    Returns the month and day of the new date
    """
    # check if leap year, and if leap year change the max sum of days for each month starting in february
    months = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
    if check_leap_year(year):
        months = [31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]

    # for each month, max sum of days so far in year
    for i in range(len(months)):
        maxDays = months[i]
        # if maxDays is greater than given days paramater
        if maxDays >= days:
            # if i is equal to zero and days is less than or equal to 31 - keeps days the same
            # case if i is greater than the zero
            # days is equal to days minus the max sum of days so far in year from the month before
            if i > 0:
                days = days - months[i - 1]
            return days_month_to_string(i, days)


def days_to_years(days):
    """
    A function that returns the year and left over days based on how many days.
    Starting at 1970 example: if days is to equal 365, it returns year 1971
    """
    # start year, add one to days because starting on the first
    year = 1970
    days += 1
    while days > 365:
        days_in_year = 365
        # if a leap year
        if check_leap_year(year):
            days_in_year = 366
        # subtrack a year of days from days, and increment year
        days -= days_in_year
        year += 1
    return (year, days)


def seconds_to_days(seconds):
    """
    A function that divides the paramater seconds by seconds per day and returns how many days
    """
    seconds_per_day = 86400
    return seconds // seconds_per_day


def conv_endian(num, endian='big'):
    """Converts number to hexadecimal string"""
    hex_num_str_table = ['0', '1', '2', '3', '4', '5', '6', '7',
                         '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    negative = False

    if endian != 'big' and endian != 'little':
        return None
    if num < 0:
        negative = True
        num *= -1
    # Converts number to big-endian hexadecimal
    hex_str = dec_hex_helper(num, "", hex_num_str_table)
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str
    # Converts string to little-endian format
    if endian == 'little':
        hex_str = conv_little_endian_helper(hex_str)
    # Adds spaces to format string
    hex_str = add_spaces_helper(hex_str)
    if negative:
        return '-' + hex_str
    return hex_str


def dec_hex_helper(num, hex_str, conv_table):
    """Helper function that converts decimal number to hexadecimal format"""
    if num <= 0:
        return hex_str
    return dec_hex_helper(num // 16, conv_table[num % 16] + hex_str,
                          conv_table)


def conv_little_endian_helper(hex_str):
    """Helper function that converts hexadecimal from big to little-endian
       format"""
    temp_hex_before = ""
    temp_hex_after = ""
    # For odd number of hexadecimal byte pairs, save the middle numbered pair
    if (len(hex_str) / 2) % 2 != 0:
        temp_hex_mid = hex_str[(len(hex_str) // 2) - 1:
                               (len(hex_str) // 2) + 1]
    else:
        temp_hex_mid = ''
    # Reverse the order of the hexadecimal byte pairs
    for i in range(0, (len(hex_str) // 2) - 1, 2):
        temp_hex_before = hex_str[i: i + 2] + temp_hex_before
        temp_hex_after += hex_str[len(hex_str) - i - 2: len(hex_str) - i]
    return temp_hex_after + temp_hex_mid + temp_hex_before


def add_spaces_helper(hex_str):
    """Helper function that adds a space between each hexadecimal byte pair"""
    i = len(hex_str) - 2
    while i >= 2:
        hex_str = hex_str[:i] + " " + hex_str[i:]
        i = i - 2
    return hex_str
