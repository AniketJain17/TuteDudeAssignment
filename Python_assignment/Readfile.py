file = open("example.txt", "r")  # Open in read mode
content = file.read()            # Read the entire content
print("File content:\n")
print(content)
file.close()                     # Close the file