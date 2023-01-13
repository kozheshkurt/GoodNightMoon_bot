import urllib.request
import urllib.parse
import urllib.error
import re

# The function returns message 'Good night' with emoji of actual moon phase as the last symbol
# Argument x is a day shift like yesterday or tomorrow


def get_goodnight(x):

    # search for moon day at the site
    fhand = urllib.request.urlopen('https://starcity.dp.ua')
    for line in fhand:
        dayinline = re.findall('Місячний день:', line.decode())
        if len(dayinline) < 1:
            continue
        day = re.findall('>([0-9]+)<', line.decode())

    dayint = int(day[0]) + x

    # choosing the emoji depending of moon day
    if dayint <= 2:
        emoji = '🌑'
    elif dayint <= 5:
        emoji = '🌒'
    elif dayint <= 10:
        emoji = '🌓'
    elif dayint <= 13:
        emoji = '🌔'
    elif dayint <= 16:
        emoji = '🌕'
    elif dayint <= 20:
        emoji = '🌖'
    elif dayint <= 24:
        emoji = '🌗'
    elif dayint <= 27:
        emoji = '🌘'
    elif dayint <= 31:  # 31 is for possibility of 'day after tomorrow' on the 28th day
        emoji = '🌑'

    return 'Good night ' + emoji
