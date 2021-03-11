def alarm_clock(day, vacation):
    if vacation:
        if day > 1 and day < 6:
            return "10:00"
        return "off"
  
