
x = 10
y = 2

try:
    z = x/y
    print(z)

except ZeroDivisionError:
    print("Error: Cannot divide zero number")

except NameError as e:
    print(f"Error : {e}")

else:
    print("No exception is raised")