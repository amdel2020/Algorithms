def timeConversion(s):
    time = s.split(':')
    hour = int(time[0])
    min = time[1]
    second = time[2][0:2]
    amorpm = time[2][-2:]

    if amorpm.lower() == 'pm':
        hour += 12
    elif hour < 10:
        hour = '0' + str(hour)
    
    result = ':'.join([str(hour), min, second])
    return result

print(timeConversion('07:05:45PM'))