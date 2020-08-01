from datetime import date, datetime



def calculate_age(year, month, day):
    year = year
    month = ' ' + month
    day = ' ' + day

    date_of_birth = datetime.strptime('%s' '%s' '%s' % (year, month, day), "%Y %m %d")
    def calculate(born):
        today = date.today()
        return today.year - born.year -((today.month, today.day) < (born.month, born.day))

    age = calculate(date_of_birth)















