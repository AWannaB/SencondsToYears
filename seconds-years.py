a = True
while a is True:
    seconds = int(input('Seconds:'))
    years = seconds // 31536000

    days = seconds % 31536000 // 86400

    hours = seconds % 31536000 % 86400 // 3600

    minutes = seconds % 31536000 % 86400 % 3600 // 60

    final_seconds = seconds % 31536000 % 86400 % 3600 % 60 % 60

    print(f'{seconds} seconds is the same as')
    print(f'{years} years, {days} days, {hours} hours, {minutes} minutes, and {final_seconds} seconds')
