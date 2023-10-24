from intro import Point
import intro
import copy

class Rectangle(object):
    """
        Represents a rectangle
        
        attributes: width:float ,height:float , corner:Point
    """
    
box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

    
# Instances as Return Values
def find_center(rect):
    p = Point
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

center = find_center(box)
print(intro.print_point(center))

print("The objects we created so far are mutable")

box.width = box.width + 50
box.height = box.height + 100

center = find_center(box)
print(intro.print_point(center))

# Functions call also mutate our values
def grow_rectangle(rect,dwidth,dheight):
    rect.width += dwidth
    rect.height += dheight
    
grow_rectangle(box,50,100)
print(box.width, " ", box.height)

# Exercise 15-2 --> Add dx and dy to the coordinates of rectangle, thereby moving it, using corner member
def move_rectangle(rect,dx,dy):
    rect.corner.x += dx
    rect.corner.y += dy

print("\n"*5)
    
# Copying
'''
Aliasing can make a program difficult to read because changes in one place might have 
unexpected effects in another place. It is hard to keep track of all the variables that might 
refer to a given object.
Copying an object is often an alternative to aliasing. The copy module contains a func
tion called copy that can duplicate any object:

In Python, an alias refers to giving a different name to an existing object. It means that two or more names can refer to the same object in memory. 
When you create an alias for an object, you are not creating a new object; instead, you are providing an alternate name to access the same underlying data.

Aliasing occurs when multiple variables or references are used to refer to the same object in memory. It can be intentional or accidental.

'''

p1 = Point()
p1.x = 3.0
p1.y = 4.0
p2 = copy.copy(p1)

print(intro.print_point(p1))
print(intro.print_point(p2))

print(p1 is p2)
print(p1 == p2)

print("Let's try copying a rectangle")
box2 = copy.copy(box)
print(box2 is box)
print(box2.corner is box.corner)

'''
Shallow Copy:
A shallow copy creates a new object, but it does not create new objects for the data inside the original object. 
Instead, it references the same objects that are inside the original object. In other words, the outer structure of the object is copied,
but the internal references are shared. So, changes made to the data inside the original object will be reflected in the copied object and vice versa. 
Shallow copying is typically done using the copy() method or the copy.copy() function from the copy module.

Deep Copy:
A deep copy, on the other hand, creates a new object and recursively copies all the data inside the original object. 
This means that every object and nested object within the original object gets copied to new memory locations. 
As a result, the original and copied objects are completely independent of each other.
Changes made to the data inside the original object will not affect the copied object and vice versa. 
Deep copying is typically done using the copy.deepcopy() function from the copy module.

is checks if two variables refer to the same object in memory. It checks object identity.
== checks if two variables have the same data/values. It checks object equivalence.
In other words:

is checks if the memory addresses of the two objects are the same.
== checks if the data/values of the two objects are the same.

'''

'''
For most applications, this is not what you want. In this example, invoking 
grow_rectangle on one of the Rectangles would not affect the other, but invoking 
move_rectangle on either would affect both! This behavior is confusing and errorprone.
Fortunately, the copy module contains a method named deepcopy that copies not only 
the object but also the objects it refers to, and the objects they refer to, and so on. You 
will not be surprised to learn that this operation is called a deep copy.
'''

box3 = copy.deepcopy(box)
print(box3 is box)
print(box3 == box)

def move_rectangleTwo(rect,dx,dy):
    r = copy.deepcopy(rect)
    r.corner.x += dx
    r.corner.y += dy
    return r

print("Lets check attribute error")

try:
    print(box.z)
except AttributeError as e:
    print(type(e))
    print("Error ", str(e))