from holiday import isHoliday
import datetime

def test_isHoliday():

    date = datetime.date(2022, 12, 25)

    christmas = datetime.date(2022, 12, 25)
    epiphany = datetime.date(2022, 1, 6)
    newYear = datetime.date(2022, 12, 31)

    assert isHoliday(date, christmas, epiphany, newYear) == "this is a holyday"


def test_isNotHoliday():

    date = datetime.date(2022, 10, 9)

    christmas = datetime.date(2022, 12, 25)
    epiphany = datetime.date(2022, 1, 6)
    newYear = datetime.date(2022, 12, 31)

    assert isHoliday(date, christmas, epiphany, newYear) == "this is not a holyday"