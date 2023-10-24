import math

# Write a function that generates the area of a circle
# Given the centre of the circle and a point on the perimeter


def calculateDistance(x1,y1,x2,y2):
    # Calculates the 2D distance of two coordinates
    dx = (x2-x1)**2;
    dy = (y2-y1)**2;
    return (dx + dy)**(1/2)


def calculateAreaCircle(r):
    return math.pi * r**2;  

def generateArea(cx,cy,px,py):
    r = calculateDistance(cx,cy,px,py);
    area = calculateAreaCircle(r);
    return area;

print(generateArea(12,10,0,0));
