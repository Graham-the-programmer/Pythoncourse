# time convertor
import datetime
from datetime import timedelta

num_of_secs = int(input("Please input seconds: "))
result = timedelta(seconds = num_of_secs)
print(result)
