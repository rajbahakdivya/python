# the strftime()method returns string representing data ansd time for the datetime object.
# allows us to display the date and time in a custome specific formate.


import datetime as dt

current_datetime= dt.datetime.now()

print(current_datetime)

String_date= current_datetime.strftime("%A,%B,%d,%Y")
print(String_date)