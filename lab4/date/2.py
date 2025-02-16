from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days= 1)
tomorrow = today + timedelta(days = 1)
print('today: ', today)
print('yesterday: ', yesterday)
print('tomorrow: ', tomorrow)