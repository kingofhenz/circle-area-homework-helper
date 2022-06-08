print("A program for calculate the Area,Diameter and Circumference of a circle if Radius, diameter, or circumference is known")
print("******************************************************************************************")
while True:
    pi = 3.14
    crd = input("do you have the circumfrence, radius, or diameter: ")
    irf = float(input("Enter the " + crd  + " " + "of the circle: "))
    if crd == "radius":
        crd = float(irf)
        area = pi * irf * irf
        print("The area of the circle is: " + str(area))
        diameter = 2 * irf
        print("The diameter of the circle is: " + str(diameter))
        circumference = 2 * pi * irf
        print("The circumference of the circle is: " + str(circumference))
        print("******************************************************************************************")
    if crd == "diameter":
        irf = float(irf)
        area = (irf / 2 * 2 ) * pi
        print("The area of the circle is: " + str(area))
        radius = irf / 2
        circumference = 2 * pi * radius
        print("The circumference of the circle is: " + str(circumference))
        print("******************************************************************************************")
    if crd == "circumfrence":
        irf = float(irf)
        area = irf / pi / 2 * pi 
        print("The area of the circle is: " + str(area))
        radius = irf / (2 * pi)
        diameter = 2 * radius
        print("The diameter of the circle is: " + str(diameter))
        print("******************************************************************************************")
