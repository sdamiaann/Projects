import qrcode

import qrcode

# Replace with your custom domain URL
url = "http://www.meltingpotfebruarymenu.com"

# Create the QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(url)
qr.make(fit=True)

# Save the QR code as an image
img = qr.make_image(fill="black", back_color="white")
img.save("valentine_menu_qr.png")

print("QR Code saved as valentine_menu_qr.png")
