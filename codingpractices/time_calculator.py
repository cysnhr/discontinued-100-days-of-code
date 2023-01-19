# 20230118-20230119

def add_time(start, duration, end_day = None):

  # defining variables
  
  # start
  start_time = start.split(" ")
  # for AM, PM; making sure all cases match
  ap = start_time[1].lower()
  # XX:XX
  time = start_time[0].split(":")
  hour1 = int(time[0])
  minutes1 = int(time[1])

  # duration
  duration = duration.split(":")
  hour = int(duration[0])
  minute = int(duration[1])

  # arithmetic and conditions

  minute += minutes1
  if minute >= 60:
    hour += 1
    minute -= 60
  # formatting
  if minute < 10:
    minute = f"0{minute}"

  # duration of days
  days = 0
  while hour >= 24:
    hour -= 24
    days += 1
  
  hour += hour1

  if hour >= 24:
    days += 1
  if hour >= 12:
    hour -= 12
    if hour == 0:
      hour = 12 # for display purposes
    if ap == "am":
      ap = "PM"
    if ap == "pm":
      ap = "AM"

  # processing days of the week
  if end_day:

    place = 0
    end_day = end_day.lower()
    week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    for i in range(0, 7):
      if end_day == week[i]:
        place = i
    place += days
    end_day = week[place]

    if days == 0:
      new_time = f"{hour}:{minute} {ap.upper()}, {end_day.title()}"
      return new_time
    if days == 1:
      new_time = f"{hour}:{minute} {ap.upper()}, {end_day.title()} (next day)"
      return new_time
    else:
      new_time = f"{hour}:{minute} {ap.upper()}, {end_day.title()} ({days} days later)"
      return new_time
      
  # getting the days
  if days == 0:
    new_time = f"{hour}:{minute} {ap.upper()}"
    return new_time
  elif days == 1:
    new_time = f"{hour}:{minute} {ap.upper()} (next day)"
    return new_time
  elif days != 0 and days != 1:
    new_time = f"{hour}:{minute} {ap.upper()} ({days} days later)"
    return new_time



print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)
