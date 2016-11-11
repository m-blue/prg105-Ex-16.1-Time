class Time():
    """
    This will hold an object of time

    attributes: hours, minutes, seconds
    """


def print_time(hour, minute, sec):
    print '%.2d:%.2d:%.2d' % (hour, minute, sec)


time = Time()
time.hours = 4
time.minutes = 30
time.seconds = 45

print_time(time.hours, time.minutes, time.seconds)
