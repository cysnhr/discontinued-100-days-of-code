### 20230121

```python
if end_day:

  place = 0
  end_day = end_day.lower()
  week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  for i in range(0, 7):
    if end_day == week[i]:
      place = i
      print(place)
  place += days
  while place > len(week):
    place -= len(week) - 1
  end_day = week[place]
```

Something was super wrong with the list index management but after tinkering with it for a while I solved it. Even though I'm not 100% sure how. I guess it just needed work on numbers and logic and stuff.
