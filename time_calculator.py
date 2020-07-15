def add_time(start, duration, day='today'):

  def set_ampm(hour):
    if hour < 12:
      ampm == 'AM'
    else:
      ampm == 'PM'

  startDay = day.islower()

  p = start.replace(':',' ')
  p = p.split(' ')
  startHour = int(p[0])
  startMinute = int(p[1])
  ampm = p[2]

  r = duration.split(':')
  addHour = int(r[0])
  addMinute = int(r[1])
  hours = 0
  minutes = 0
  daysLater = 0

  totalHour = startHour + addHour

 
  if totalHour < 24:
    if totalHour < 12:
      hours = totalHour
      set_ampm(totalHour)
    elif totalHour >= 12:
      hours = totalHour - 12
      set_ampm(totalHour)

  if startMinute + addMinute < 60:
    minutes = startMinute + addMinute
    # return str(minutes)
  else:
    minutes = startMinute + addMinute - 60
    hours += 1
    # return str(hours) + ': ' + str(minutes)

  new_time = str(hours) + ':' + '%02d' % minutes + ' ' + ampm
  
  return new_time