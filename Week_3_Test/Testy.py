import math
pi = math.pi

def biscuitCutting():
    diameter = int(input("Please enter the diameter of each biscuit (cm): "))
    width = int(input("Please enter the number of biscuits along the width of the mixture: "))
    length = int(input("Please enter the number of biscuits along the length of the mixture: "))
    
    radius = diameter / 2
    print("The radius of each biscuit is " +str(radius) + " (cm)")
    
    biscuit_area = pi * (radius**2)
    print("The area of each biscuit is " + str(biscuit_area)[:5] +" (cm^2)")
    
    length_cm = diameter * width # work out length of all batter
    width_cm = diameter * length
    total_area = width_cm * length_cm
    print("The total area of the mixture is " + str(total_area) + " (cm)")
    
    biscuit_count = width * length
    current_biscuit_area = biscuit_count * biscuit_area
    leftover_area = total_area - current_biscuit_area
    leftover_biscuits = leftover_area / biscuit_area 
    print("With the leftover batter "+ str(int(leftover_biscuits)) + " biscuit's could be made")
    

biscuitCutting()