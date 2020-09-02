def which_day(start, nights):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday']
    return days[(start + nights) % 7]


print(which_day(3, 50))  # Saturday
print(which_day(3, 20))  # Tuesday
