# Python is an object-oriented programming language, which means that it provides 
# features that support object-oriented programming.
# It is not easy to define object-oriented programming, but we have already seen some of 
# its characteristics:
# • Programs are made up of object definitions and function definitions, and most of 
# the computation is expressed in terms of operations on objects.
# • Each object definition corresponds to some object or concept in the real world, and 
# the functions that operate on that object correspond to the ways real-world objects 
# interact.


# For example, the Time class defined in Chapter 16 corresponds to the way people record 
# the time of day, and the functions we defined correspond to the kinds of things people 
# do with times. Similarly, the Point and Rectangle classes correspond to the mathe
# matical concepts of a point and a rectangle.
# So far, we have not taken advantage of the features Python provides to support object oriented programming. These features are not strictly necessary; most of them provide 
# alternative syntax for things we have already done. But in many cases, the alternative is 
# more concise and more accurately conveys the structure of the program.
# For example, in the Time program, there is no obvious connection between the class 
# definition and the function definitions that follow. With some examination, 
# 
# it is apparent 
# that every function takes at least one Time object as an argument.

class Time():
    
    
    # Dunder methods are used to define how objects of a class behave in certain situations or in response to specific operations.

    # For example, the __init__ method is a dunder method that is automatically called when an object of a class is created.
    # Similarly, the __str__ method is a dunder method that defines how the object should be represented as a string when str(object) is called.

    # Dunder methods allow you to customize the behavior of your classes and objects to make them more intuitive and Pythonic.
    
    # innit Bruh
    # The init method is a special method(class function) that gets invoked when an object is instantiated
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    
    # when we print an instance of a class, we need a string representation
    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"  
      
    # We can OVERLOAD OPERATORS just like in c++
    
    def __add__(self,other): #overloads the + operator, using 2 instances of Time, self and other
        # Type dispatch
        if isinstance(other,Time):
            return self.add_time(other)
        else:
            return self.increment(other)  
    
    def add_time(self,other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def increment(self,seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def __radd__(self,other):
        # addition: if Time object appears on the right side
         return self.__add__(other)
          
     
    # Non dunder methods

    # Basic print functionality
    def print_time(self): # self represents the instance invoking the function, also called the subject, always passed implicitly
        print(f"{self.hour}:{self.minute}:{self.second}")
        return ""
    
    # convert time instance to seconds (integer)
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
    
    # increment time
    def increment(self,seconds):
        seconds += self.time_to_int() # instance.time_to_int()
        return int_to_time(seconds)
        
    # What if we are working with 2 or more Time objects? :-)
    def is_after(self,other):
        return self.time_to_int() > other.time_to_int()    
    
        
#    ----> Outside class <----        
def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def print_attributes(obj):
    for attr in obj.__dict__:
        print(attr, getattr(obj, attr))


if __name__ == "__main__":
        
    start = Time()
    start.hour = 9
    start.minute = 45
    start.second = 0

    start.print_time()
    end = Time()
    end = start.increment(1337)
    end.print_time()

    print(end.is_after(start))

    # using dunder methods 
    time = Time()
    print(time)
    time1 = Time(9)
    print(time1)
    time2 = Time(9,40)
    print(time2)
    time3 = Time(9,40,30)
    print(time3)
    print()

    start = Time(9,45)
    duration = Time(1,35)
    print(start + duration)
    print(start+1337)

    print(1337+start)
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1,t2,t3])
    print(type(total))
    print(total)
    
    print(print_attributes(total))
