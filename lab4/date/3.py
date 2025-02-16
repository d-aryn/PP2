from datetime import datetime
a = datetime.now()
newdate = a.replace(microsecond=0)
print(a.strftime("%c"))
print(newdate)