import numpy as np
def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return np.pi * (radius ** 2)
def area_of_rectangle(length, width):
    """Calculate the area of a rectangle given its length and width."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width
if __name__ == "__main__":
    radius = input("Enter the radius of the circle: ")
    circle_radius = float(radius)
    length = input("Enter the length of the rectangle: ")
    rectangle_length = float(length)
    width = input("Enter the width of the rectangle: ")
    rectangle_width = float(width)

    
    circle_area = area_of_circle(circle_radius)
    rectangle_area = area_of_rectangle(rectangle_length, rectangle_width)
    
    print(f"Area of circle with radius {circle_radius}: {circle_area}")
    print(f"Area of rectangle with length {rectangle_length} and width {rectangle_width}: {rectangle_area}")