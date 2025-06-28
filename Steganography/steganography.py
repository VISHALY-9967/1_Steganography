import cv2
import os
import string

# This is use to read the file
img = cv2.imread("flower.jpg")
# Taking input from user
msg = input("Enter secret message : ")
password = input("Enter a passcode : ")

# To store key and message
with open("secret_info.txt", "w") as file:
    file.write(f"Secret Message: {msg}\n")
    file.write(f"Password: {password}\n")
print("Secret message and password saved to 'secret_info.txt'")

# Encryption Process start and dictionaries for char to num mapping
d = {}
c = {}
# Fill the dictionaries with ASCII values
for i in range (255):
    d[chr(i)] = i
    c[i]=chr(i)

# initial positions for pixel
n=0;
m=0;
z=0;
# Embed each msg into img
for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=m+1
    m=m+1
    z=(z+1)%3    


cv2.imwrite("encryptedImage.jpg" , img)
os.startfile("encryptedImage.jpg")

# Decryption process
message = ""
n=0
m=0
z=0

pas=input("Enter passcode for Decryption : ")

if(password==pas):
    for i in range(len(msg)):
        message=message+c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1)%3
    print("Decryted message =",message)
else:
    print("You are not Authenticated ")