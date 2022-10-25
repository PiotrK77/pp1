x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))
quadrant = None
axis = None
origin = False

if x == 0:
    if y == 0:
        origin = True
    else:
        axis = "y"

if x > 0:
    if y > 0:
        quadrant = "first"
    if y < 0:
        quadrant = "fourth"
    if y == 0:
        axis = "x"
if x < 0:
    if y > 0:
        quadrant = "second"
    if y < 0:
        quadrant = "third"
    if y == 0:
        axis = "x"

print(f"Point ({x}, {y}) is ", end = "")

if origin:
    print("in the origin ")

if quadrant != None:
    print(f"in the {quadrant} quadrant ", end = "")

else:
    print(f"on the {axis} axis ", end = "")

print("of the coordinate system")