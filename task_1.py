time_string = '1h 45m,360s,25m,30m 120s,2h 60s'
time_values = time_string.split(',')
total_minutes = 0
for value in time_values:
    minutes = 0
    parts = value.split()
    for part in parts:
        if 'h' in part:
            hours = int(part.replace('h', ''))
            minutes += hours * 60
        elif 'm' in part:
            mins = int(part.replace('m', ''))
            minutes += mins
        elif 's' in part:
            seconds = int(part.replace('s', ''))
            minutes += seconds // 60
    total_minutes += minutes
print(total_minutes)