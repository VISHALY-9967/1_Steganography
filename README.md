<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Steganography: Hide Secret Messages in Images</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background-color: #f5f7fa;
      color: #222;
      line-height: 1.6;
      max-width: 900px;
      margin: auto;
      padding: 2em;
    }
    h1, h2 {
      color: #3a3a3a;
    }
    code {
      background: #eee;
      padding: 0.2em 0.4em;
      border-radius: 4px;
      font-family: monospace;
    }
    pre {
      background-color: #272822;
      color: #f8f8f2;
      padding: 1em;
      border-radius: 6px;
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1em 0;
    }
    th, td {
      padding: 10px;
      border: 1px solid #ddd;
      text-align: left;
    }
    ul {
      padding-left: 1.2em;
    }
    .emoji {
      font-size: 1.2em;
    }
  </style>
</head>
<body>

  <h1>🔐💐 Steganography: Hide Secret Messages in Images</h1>
  <p><em>A minimal Python project to embed and extract hidden messages inside images with password protection</em></p>

  <hr>

  <h2>🌟 Features</h2>
  <ul>
    <li>✨ Hide your secret messages inside a <code>.jpg</code> image</li>
    <li>🔑 Password-protected encryption and decryption</li>
    <li>🧠 Simple character-to-pixel value mapping using RGB</li>
    <li>📁 Auto-saves encrypted image and secret info</li>
    <li>📤 Launches the encrypted image for instant preview</li>
  </ul>

  <h2>🖼️ Demo Preview</h2>
  <pre>
Enter secret message: Hello GitHub!
Enter a passcode: mySecret123

✅ Message hidden in 'encryptedImage.jpg'
📁 Saved secret_info.txt with your data

Enter passcode for Decryption: mySecret123
🔓 Decrypted Message: Hello GitHub!
  </pre>

  <h2>🚀 Quick Start</h2>

  <h3>🔧 Requirements</h3>
  <ul>
    <li>Python 3.x</li>
    <li>OpenCV (<code>pip install opencv-python</code>)</li>
  </ul>

  <h3>📥 Run</h3>
  <pre>python steganography.py</pre>
  <p>🖼️ <strong>Note:</strong> Make sure you have an image named <code>flower.jpg</code> in the same folder as the script.</p>

  <h2>🧠 How It Works</h2>
  <ul>
    <li>🔢 Converts characters to ASCII values</li>
    <li>🎨 Embeds them into RGB values of image pixels</li>
    <li>🔐 Verifies using a password</li>
    <li>🧾 Saves the original message and password in <code>secret_info.txt</code> (for reference only)</li>
  </ul>

  <h2>📂 Files Generated</h2>
  <table>
    <tr>
      <th>File</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>encryptedImage.jpg</code></td>
      <td>Image with hidden message</td>
    </tr>
    <tr>
      <td><code>secret_info.txt</code></td>
      <td>Stores your secret message + passcode</td>
    </tr>
  </table>

  <h2>🤔 Why Use This?</h2>
  <ul>
    <li>✍️ Simple yet powerful for beginners learning <strong>image processing</strong></li>
    <li>🔒 Great base for learning <strong>secure data hiding</strong></li>
    <li>💡 Can be extended to a GUI or integrated with <strong>AES encryption</strong></li>
  </ul>

  <h2>📌 To-Do (Next Steps)</h2>
  <ul>
    <li>[ ] Add support for larger messages</li>
    <li>[ ] Implement better password encryption (hashing or AES)</li>
    <li>[ ] Build a GUI using Tkinter or PyQt</li>
    <li>[ ] Embed message length inside the image</li>
  </ul>

  <h2>🪄 Like It?</h2>
  <p>If you find this project helpful or fun:</p>
  <ul>
    <li>⭐ Star this repo</li>
    <li>🍴 Fork it to build your own version</li>
    <li>📣 Share it with other Python enthusiasts!</li>
  </ul>
</body>
</html>
