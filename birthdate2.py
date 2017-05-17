import calendar
age = int(input('ENTER YOUR AGE: \n'))
date = int(input('ENTER DATE OF BIRTHDAY IN FIGURES: \n'))
month = int(input('ENTER MONTH OF BIRTH IN FIGURES: \n'))
current_year = int(input('ENTER CURRENT YEAR: \n'))
year_of_birth = current_year - age
day_of_birth = calendar.weekday(year_of_birth, month, date)
date_of_birth = date
month_of_birth = month
day_string = calendar.day_name[day_of_birth]
print('you were born on ' + day_string + ',' + str(date_of_birth) + ',' + str(month_of_birth) + ',' + str(year_of_birth))
