import datetime
from datetime import datetime
print('Hi there! Welcome to my simple countdown app! \nTo begin, please enter the countdown date in the following format:')

# Initial function that asks user to input a date and then assigns it to a variable (also assigns current time and date to a variable)
def countdown():
    blue = True
    while blue:
        entry = input('mm/dd/yyyy \n')
        global date
        date = entry[0:2] + entry[3:5] + entry[6:10]
        try:
            int(date)
        except ValueError:
            print('Error! Please enter a valid date.')
            continue
        else:
            try:
                date[7]
            except IndexError:
                print('Error! Please enter a valid date.')
                continue
            else:
                if 1 <= int(date[0:2]) <= 12 and 1 <= int(date[2:4]) <= 31 and 1 <= int(date[4:8]) <= 9999:
                    print(f'The date you entered is {date[0:2]}/{date[2:4]}/{date[4:8]}, correct?')
                    blue = False
                else:
                    print('Error! Please enter a valid date.')
                    continue
    while not blue:
        confirmation = input('Y/N \n')
        if 'y' == confirmation.lower():
            global month
            global day
            global year
            global future_date
            global today
            month = int(date[0:2])
            day = int(date[2:4])
            year = int(date[4:8])
            future_date = datetime(year,month,day)
            today = datetime.now()
            timename_assign()
            break
        elif 'n' == confirmation.lower():
            print('Please enter the correct date in the following format:')
            countdown()
            break
        else:
            print("Invalid response. Please type Y or N.")
            continue

# Secondary function that is executed inside countdown(). Asks user if they would like to assign a time and/or name to the event.
# This function also calculates the difference between the two dates and presents it to the user, and allows them to repeat the entire process for a new date.
# The actual process of accepting event time input is handled by timing_func(), and process of accepting event name input is handled by naming_func().
def timename_assign():
    print("Would you like to assign a time to this event?")
    while True:
        time_confirm = input('Y/N \n')

        if 'y' == time_confirm.lower():
            print("What time will the event take place? You may leave the minutes section blank.")
            timing_func()
            break
        elif 'n' == time_confirm.lower():
            event_hour = 0
            event_minute = 0
            break
        else:
            print('Invalid response. Please type Y or N.')
            continue

    date_diff = future_date - today
        
    print("Would you like to name this event?")
    while True:
        global event_name
        named = input('Y/N \n')
        if 'y' == named.lower():
            naming_func()
            break
        elif 'n' == named.lower():
            event_name = "this event"
            break
        else:
            print('Invalid response. Please type Y or N.')
            continue

    while True:
        if str(date_diff)[0] == '-':
            positive_days = str(date_diff.days)[1:]
            print(f"{event_name} was {positive_days} days, {date_diff.seconds//3600} hours, and {(date_diff.seconds//60)%60} minutes ago!")
            break
        else:
            print(f"There are {date_diff.days} days, {date_diff.seconds//3600} hours, and {(date_diff.seconds//60)%60} minutes until {event_name}!")
            break
    
    print("Would you like to add another date?")
    
    while True:
        repeat = input('Y/N \n')
        if 'y' == repeat.lower():
            countdown()
            break
        elif 'n' == repeat.lower():
            print("Thank you for using my countdown script!")
            break
        else:
            print("Invalid response. Please type Y or N.")
            continue

# This function deals with the process of assigning a name to the event.
def naming_func():
    print("What would you like to name the event?")
    while True:
        global event_name
        event_name = input()
        print(f"The event name is '{event_name}', correct?")
        while True:
            confirm_event = input('Y/N \n')
            if 'y' == confirm_event.lower():
                break
            elif 'n' == confirm_event.lower():
                naming_func()
                break
            else:
                print("Invalid response. Please type Y or N.")
                continue
        break
        
# This function deals with the process of assigning a time to the event.
def timing_func():
    global event_minute
    global event_hour
    while True:
        time = input("hh:mm (24 hr format) \n")
        
        try:
            int(time[0:2])
        except ValueError:
            print("Error! Please enter a valid time.")
            continue
        else:
            pass
            
        if 0 <= int(time[0:2]) <= 23:
            
            if int(time[0:2]) == 0:
                if time[3:5] == '':
                    print("Error! Time cannot be 00:00")
                    # timing_func()
                    # break
                    continue
                else:
                    event_hour = '00'
            else:
                event_hour = int(time[0:2])
                
            try:
                int(time[3:5])
            except ValueError:
                event_minute = '00'
                break
            else:
                if 0 <= int(time[3:5]) <= 59:
                    event_minute = int(time[3:5])
                    break
                else:
                    print("Error! Please enter a valid time.")
                    timing_func()
                    break
        else:
            print("Error! Please enter a valid time.")
            continue
    
    while True:
        if 0 < event_minute < 10:
            adapted_event_minute = '0' + str(event_minute)
            print(f'The event time is {event_hour}:{adapted_event_minute}, correct?')
            break
        else:
            print(f'The event time is {event_hour}:{event_minute}, correct?')
            break
    
    while True:
        confirm_time = input('Y/N \n')
        if 'y' == confirm_time.lower():
            event_minute = int(event_minute)
            event_hour = int(event_hour)
            break
        elif 'n' == confirm_time.lower():
            timing_func()
            break
        else:
            print("Invalid response. Please type Y or N.")
            continue
    
    global future_date
    future_date = future_date.replace(hour=event_hour)
    future_date = future_date.replace(minute=event_minute)
    
countdown()