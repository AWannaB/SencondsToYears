a = True
while a is True:

    seconds = (input('Seconds:'))
    try:
        int(seconds) // 2
    except ValueError:
        if seconds == 'q':
            a = False
            continue
        print('Not a valid number.')
    else:
        years = int(seconds) // 31536000

        days = int(seconds) % 31536000 // 86400

        hours = int(seconds) % 31536000 % 86400 // 3600

        minutes = int(seconds) % 31536000 % 86400 % 3600 // 60

        final_seconds = int(seconds) % 31536000 % 86400 % 3600 % 60 % 60

        print(f'{seconds} seconds is the same as')
        print(f'{years} years, {days} days, {hours} hours, {minutes} minutes, and {final_seconds} seconds')
