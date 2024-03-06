        # Keyword Arguments - 
        
from datetime import date, timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")
output = arrival_time()
print(output)