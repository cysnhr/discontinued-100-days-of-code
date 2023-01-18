# 20230118

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
  hour += hour1
  if hour >= 12:
    hour -= 12
    if ap == "am":
      ap = "PM"
    if ap == "pm":
      ap = "AM"

  minute += minutes1
  if minute >= 60:
    hour += 1
    minute -= 60
  # formatting
  if minute < 10:
    minute = f"0{minute}"

  new_time = f"{hour}:{minute} {ap.upper()}"

  # getting the days
  if (start_time[1].lower() == "pm" and ap == "AM") or (int(duration[0]) >= 24):
    new_time = f"{hour}:{minute} {ap.upper()} (next day)"

  
  
  return new_time

print(add_time("11:43 AM", "00:20"))
