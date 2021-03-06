"""
image.py

Input a binary file.  Since the file is not a text file, we cannot say
for line in lines:
"""

import sys
import tkinter

#macOS
filename = "/Users/myname/Desktop/escalus.gif"
#Microsoft Windows
#filename = "C:\\Users\\Myname\\Desktop\\escalus.gif"

try:
    binaryFile = open(filename, "rb")          #read binary
except FileNotFoundError:
    print("Sorry, could not find file \"", filename, "\".", sep = "")
    sys.exit(1)
except PermissionError:
    print("Sorry, no permission to open file \"", filename, "\".", sep = "")
    sys.exit(1)

sequenceOfBytes = binaryFile.read()            #not string of characters
binaryFile.close()
print("len(sequenceOfBytes) =", len(sequenceOfBytes))

root = tkinter.Tk()

try:
    #The following statement cannot come before the tkinter.Tk().
    photoImage = tkinter.PhotoImage(data = sequenceOfBytes)
except tkinter.TclError as error:
    print(error)   #"couldn't recognize image data" when image is jpg or png.
    sys.exit(1)

root.geometry("720x480")
root.title("Price Escalus")

label = tkinter.Label(root, image = photoImage)
label.pack()

root.mainloop()
