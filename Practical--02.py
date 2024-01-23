fh = open('Output.txt', 'w')

Choice = int(input("""Select:
1. For Area of Rectangle,
2. For Perimeter of Rectangle:
Enter your choice (1 or 2): """))

if Choice == 1:
    length = int(input("Enter the length of Rectangle: "))
    breadth = int(input("Enter the Breadth of Rectangle: "))
    area = length * breadth
    fh.write(f'Area of Rectangle is: {area}')

elif Choice == 2:
    length = int(input("Enter the length of Rectangle: "))
    breadth = int(input("Enter the Breadth of Rectangle: "))
    perimeter = 2 * (length + breadth)
    fh.write(f'Perimeter of Rectangle is: {perimeter}')

else:
    print("Invalid choice")

fh.close()
