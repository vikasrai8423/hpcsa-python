import datetime

def derive_age(date_of_birth):
    age_in_days = datetime.datetime.today() - date_of_birth 
    print("Age in days: ",age_in_days)

date_string = "21 April, 2023 00:00:00 000000"
datetime_object = datetime.datetime.strptime(date_string, "%d %B, %Y %H:%M:%S %f")

derive_age(datetime_object,10,10)
print("The datetime object in string format is " , datetime.datetime.strftime(datetime_object,'%A %B'))
    