🔐💐 Steganography: Hide Secret Messages in Images
A minimal Python project to embed and extract hidden messages inside images with password protection




🌟 Features
✨ Hide your secret messages inside a .jpg image
🔑 Password-protected encryption and decryption
🧠 Simple character-to-pixel value mapping using RGB
📁 Auto-saves encrypted image and secret info
📤 Launches the encrypted image for instant preview

🖼️ Demo Preview
Enter secret message: Hello GitHub!
Enter a passcode: mySecret123

✅ Message hidden in 'encryptedImage.jpg'
📁 Saved secret_info.txt with your data

Enter passcode for Decryption: mySecret123
🔓 Decrypted Message: Hello GitHub!
🚀 Quick Start
🔧 Requirements
Python 3.x

OpenCV (pip install opencv-python)

📥 Clone & Run
git clone https://github.com/your-username/steganography-image-hider.git
cd steganography-image-hider
python steganography.py
🖼 Make sure you have an image named flower.jpg in the same folder.

🧠 How It Works
🔢 Converts characters to ASCII values
🎨 Embeds them into RGB values of image pixels
🔐 Verifies using a password
🧾 Saves the original message and password in secret_info.txt (for reference only)

📂 Files Generated
File	Description
encryptedImage.jpg	Image with hidden message
secret_info.txt	Stores your secret message + passcode

🤔 Why Use This?
✍️ Simple yet powerful for beginners learning image processing

🔒 Great base for learning secure data hiding

💡 You can extend this into a full GUI app or integrate AES encryption

📌 To-Do (Next Steps)
 Add support for larger messages

 Implement better password encryption (hashing or AES)

 Build a GUI using Tkinter or PyQt

 Embed message length inside the image

🪄 Like It?
If you find this project helpful or fun:
⭐ Star this repo
🍴 Fork it to build your own version
📣 Share with other Python enthusiasts!
