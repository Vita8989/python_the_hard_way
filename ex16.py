from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you dont want that, hit CTRL -C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("Now im going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close    

#close - closes the file 
#read reads the contests
#readline reads just oneline
#truncate empties the file
#write writes to file
#seek(0) moves the read/write location to the beginning

#target/filename set in initial call in terminal if not one is created with the name we entered. 