# As another example of a Class(user defined type), we will define a class call Time that records the time of Day.

class Time(object): #btw class objects inherently inherit from object
    '''
        Represents the time of day
        
        attributes: hour,minute,second
    '''
    

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(time: Time) -> str : 
    print(f"{time.hour}:{round(time.minute,2)}:{round(time.second,2)}")
    return ""

def is_after(t1: Time, t2: Time) -> bool:
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second) # Thats right we can use tuples to unpack a class

print(print_time(time))

time2 = Time()
time2.hour = 12
time2.minute = 59
time2.second = 31

print(is_after(time,time2)) 

'''
        Time
time -> [hour, minute, second]

'''

def add_time(t1:Time, t2:Time) -> Time:
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute 
    sum.second = t1.second + t2.second
    return sum


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 0

done = add_time(start,duration)
print(print_time(done), end="")
print("^ Is that really what we want, does it make sense")


# We need to improve our function
def add_timeV1(t1:Time,t2:Time) -> Time:
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute 
    sum.second = t1.second + t2.second
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
        
    if sum.minute >=60:
        sum.minute -= 60
        sum.hour += 1
        
    return sum

done = add_timeV1(start, duration)
print(print_time(done), end="")
print("^ This looks better but the function is growing", "\n"*2)

# modifiers
def increment(time, seconds):
    time.second += seconds
    
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
        
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1

def incrementV1(time, seconds):
    new_seconds = time.second + seconds
    minutes, new_seconds = divmod(new_seconds, 60)
    new_hour = time.hour + (minutes // 60)
    new_minute = time.minute + (minutes % 60)
    returnTime = Time()
    returnTime.seconds = new_seconds
    returnTime.minute = new_minute
    returnTime.hour = new_hour
    
    return returnTime


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
        
def add_timeV2(t1, t2):
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)
        
# invariants
def valid_time(time):
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True

def add_timeV3(t1, t2):
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

