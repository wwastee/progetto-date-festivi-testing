'''
questo progetto deve controllare un tot di date inserite manulamente e tramite una funzione
controllare se i giorni inseriti sono festivi o meno 

non c'è bisogno di input ma le date possono essere iserite manualmente

importare librerie di gestione dei caendari e delle date
'''

import datetime

date = datetime.date(2022, 12, 25)

christmas = datetime.date(2022, 12, 25)
epiphany = datetime.date(2022, 1, 6)
newYear = datetime.date(2022, 12, 31)


def isHoliday(day, holiday1, holiday2, holiday3):
    if day in [holiday1, holiday2, holiday3]:
        return("this is a holyday")
    else:
        return("this is not a holyday")


print(isHoliday(date, christmas, epiphany, newYear))
