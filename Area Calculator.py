print("Hello world")

# This program will ask the use to pick a shape and then we'll calculate the area of the shape and print that shape
print ("The Area Calculator program is running!")

option = input("Enter C for Circle or T for Triangle: ")

if option == 'C':
  # do something
  radius = float(input("Input the radius: "))
  area = 3.14159 * (radius ** 2)
  print (str(area))
elif option == 'T':
  base = float(input("Input the base: "))
  height = float(input("Input the height: "))
  area = (base /2) * height
  print (str(area))
else:
  print ("You entered an invalid shape")

print ("The program is now exiting.")