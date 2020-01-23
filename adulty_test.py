import datetime
def adulty_test(year=1970,month=1,day=1):
    now = datetime.datetime.now()
    adult_year = datetime.datetime(now.year - 18, now.month, now.day)
    if adult_year <= datetime.datetime(year,month,day):
        return False
    else:
        return True
print(adulty_test(2002,1,23))