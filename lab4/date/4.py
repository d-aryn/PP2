from datetime import datetime
date1_str = input("y-m-d h:m:s = ")
date2_str = input("y-m-d h:m:s = ")
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
difference = abs((date2 - date1).total_seconds())
print(difference)