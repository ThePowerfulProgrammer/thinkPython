# Introdution to user defined types --> Classes
import math

# In modern Python code, you can omit the (object) part, and simply define the class as class Point: because all classes in Python 3 are new-style classes by default. However, 
# using (object) explicitly is still valid and doesn't change the behavior in Python 3.

class Point(object):
    '''Represents a point in 2-D space. '''
    pass


def distance_between_points(point1:Point, point2:Point) -> float:
    sum = math.pow(point2.x - point1.x, 2) + math.pow(point2.y-point1.y,2) 
    return f"Distance between Point A and Point B: {math.sqrt(sum)} "

def print_point(p):
    return f"{(p.x, p.y)}"

if __name__ == "__main__":
    print(Point)
    '''
    In Python, when you define a class or any other top-level object in a script, it gets assigned to the module's namespace. If the script is the main program being executed, its module name is "__main__". 
    As a result, the full name of the class becomes "__main__.Point".
    '''

    point1 = Point()

    '''
    The return value is a reference to a Point object, which we assign to blank. 
    Creating a 
    new object is called instantiation, and the object is an instance of the class.
    When you print an instance,
    Python tells you what class it belongs to and where it is 
    stored in memory (the prefix 0x means that the following number is in hexadecimal).
    '''
    print(point1)

    # Attributes 
    print("We can just assign attributes")
    point1.x = 3.0
    point1.y = 4.0

    print(f"({point1.x, point1.y})")



    # We can assign values using tuples 
    point_a = Point()
    point_b = Point()
    point_a.x = 0
    point_a.y = 0

    point_b.x = 3
    point_b.y = 4

    print(print_point(point_a))
    result = distance_between_points(point_a, point_b)
    print(result)  # Output: 5.0

