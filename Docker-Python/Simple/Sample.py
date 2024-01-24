import os

print("Hello World!")

# Print the Current Directory the program is running in.
# 
# This helps one to see how the program directory changes when 
# it is ran on a container vs on the system.
print("Current Directory:", os.getcwd())
