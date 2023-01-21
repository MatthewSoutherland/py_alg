def add_time(start, duration, day=None):

    hour = int(start.split(":")[0])
    minute = int(start.split(":")[1].split(" ")[0])
    sun = start.split(" ")[1]
    day_of_week = day

    if day_of_week:
        day_of_week = day_of_week.lower()

    add_hour = int(duration.split(":")[0])
    add_minute = int(duration.split(":")[1])

    calc_minutes = minute + add_minute
    if sun == "AM":
        calc_hours = hour + add_hour
    else:
        calc_hours = hour + add_hour + 12
    days = 0

    if calc_minutes >= 60:
        calc_minutes = calc_minutes - 60
        calc_hours += 1

    while calc_hours >= 24:
        calc_hours = calc_hours - 24
        days += 1

    if calc_hours < 12:
        sun = "AM"
    else:
        sun = "PM"

    if calc_hours > 12:
        calc_hours = calc_hours - 12

    if calc_hours == 0:
        calc_hours = 12

    dayDic = {
        'monday': 1,
        'tuesday': 2,
        'wednesday': 3,
        'thursday': 4,
        'friday': 5,
        'saturday': 6,
        'sunday': 7
    }

    if day != None:
        day_number = dayDic[day_of_week] + days
    else:
        day_number = days

    while day_number > 7:
        day_number = day_number - 7

    for key, value in dayDic.items():
        if value == day_number:
            day_of_week = key.capitalize()

    if calc_minutes < 10:
        calc_minutes = f'0{calc_minutes}'

    new_time = ""
    if day == None and days == 0:
        new_time = f'{calc_hours}:{calc_minutes} {sun}'
        return new_time
    elif day == None and days == 1:
        new_time = f'{calc_hours}:{calc_minutes} {sun} (next day)'
        return new_time
    elif day == None and days > 1:
        new_time = f'{calc_hours}:{calc_minutes} {sun} ({days} days later)'
        return new_time
    elif day != None and days == 0:
        new_time = f'{calc_hours}:{calc_minutes} {sun}, {day_of_week}'
        return new_time
    elif day != None and days == 1:
        new_time = f'{calc_hours}:{calc_minutes} {sun}, {day_of_week} (next day)'
        return new_time
    elif day != None and days > 1:
        new_time = f'{calc_hours}:{calc_minutes} {sun}, {day_of_week} ({days} days later)'
        return new_time

    return 1


print(add_time("2:59 AM", "24:00", "saturDay"))
