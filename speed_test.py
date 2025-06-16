from datetime import datetime
import pytz

time_zone = pytz.timezone('Asia/Manila')
print(datetime.now(time_zone).strftime('%d-%m-%y %H:%M'))