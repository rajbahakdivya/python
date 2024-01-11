# THis method is the opposite of the strftime()method.
#it converts strings to date time object.

import datetime as dt

date_string = "11 JAN, 2024"

date_object = dt.datetime.strptime(date_string, "%d %b, %Y")

print("Date object:", date_object)
