# Open a file in write mode ('w') - it will create the file if it doesn't exist
file = open("example.txt", "w")

# Write some content
file.write("Hello, this is a sample text written to a file.\n")
file.write("Python makes file handling easy!\n")

# Close the file
file.close()

print("Content written to 'example.txt' successfully.")
