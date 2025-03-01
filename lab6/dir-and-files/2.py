import os

path = '/Users/darynnursadyk/Desktop/c++'

print(f"existence: {os.path.exists(path)}")

print(f"readability: {os.access(path, os.R_OK)}")

print(f"writability: {os.access(path, os.W_OK)}")

print(f"executability: {os.access(path, os.X_OK)}")

#Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path