from datetime import datetime
from dateutil import relativedelta

# get two dates
d1 = input("Your Birth Date (dd-mm-yyyy): " )
d2 = datetime.today()

# convert string to date object
start_date = datetime.strptime(d1, "%d-%m-%Y")
end_date = d2

# Get the relativedelta between two dates
delta = relativedelta.relativedelta(end_date, start_date)
print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')
