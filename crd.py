print("A program for calculate the Area,Diameter and Circumference of a circle if Radius is known")
print("******************************************************************************************")
while True:
    pi = 3.141592653589793238462643383279
    crd = input("do you have the circumfrence, radius, or diameter: ")
    radius = (input("Enter the " + crd  + " " + "of the circle: "))
    if crd == "radius":
        radius = float(radius)
        area = pi * radius * radius
        print("The area of the circle is: " + str(area))
        diameter = 2 * radius
        print("The diameter of the circle is: " + str(diameter))
        circumference = 2 * pi * radius
        print("The circumference of the circle is: " + str(circumference))
        print("******************************************************************************************")
