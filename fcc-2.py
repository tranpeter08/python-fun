def get_minutes(time):
  [hours, minutes] = time.split(':')

  return int(hours) * 60 + int(minutes)

days_of_week = 'sunday,monday,tuesday,wednesday,thursday,friday,saturday'.split(',')

def add_time(start, duration, day = ''):
  minutes_in_a_day = 60 * 24
  time_period = 'AM'
  current_day = day

  [start_time, period] = start.split(' ')
  period = period.lower()

  start_minutes = get_minutes(start_time)
  dur_minutes = get_minutes(duration)

  if (period == 'pm'):
    start_minutes+= 12 * 60
  
  # calculate how many days pased
  total_minutes = start_minutes + dur_minutes

  # calculate full days passed in minutes
  days = total_minutes // minutes_in_a_day
  minutes_in_days_passed = days * minutes_in_a_day

  remaining_minutes = total_minutes - minutes_in_days_passed

  # calculate hours and minutes
  hours = remaining_minutes // 60
  minutes = remaining_minutes - hours * 60
  
  # determine period and adjust for 12 hour clock
  if (hours >= 12):
    time_period = 'PM'
    hours-= 12
  
  if (hours == 0):
    hours = 12

  # determine if zero needs to be added for minutes less than 10
  zero = '0' if minutes < 10 else ''

  days_pased = 'next day' if days == 1 else f'{days} days later'
 
  message = f'{hours}:{zero}{minutes} {time_period.upper()}'

  # determine current day of the week if included 
  if (day != ''):
    # get index
    day_index = days_of_week.index(day.lower())
    current_day_index = (day_index + days) % 7 
    current_day = days_of_week[current_day_index]
    message += f', {current_day.capitalize()}'

  # add number of days passed to message
  if (days > 0):
    message += f' ({days_pased})'

  print(message)
  return message 

add_time('3:00 PM', '3:10')
add_time('11:30 AM', '2:32', 'Monday')
add_time("11:43 AM", "00:20")
add_time("10:10 PM", "3:30")
add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

add_time("8:16 PM", "466:02", "tuesday")