
import qrcode
from PIL import Image

# Data to encode
url_data = 'https://github.com/dev1virtuoso/Documentation/blob/main/dev1virtuoso/Attachment/dev1virtuoso/carson-wu.md#Contact'

# Path to the image you want to embed
image_path = 'avatar1.png'

# Open and prepare the embedded image (adjust size as needed)
logo = Image.open(image_path)
basewidth = 100 # example base width
wpercent = (basewidth / float(logo.size[0]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.Resampling.LANCZOS) # Use a suitable resampling filter

# Create the QRCode object with the required ERROR_CORRECT_H level
qr = qrcode.QRCode(
    version=None, # Automatically determines the version
    error_correction=qrcode.constants.ERROR_CORRECT_H, # Set to High error correction
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(url_data)
qr.make(fit=True) # Make the QR code fit the data

# Generate the QR code image
img = qr.make_image(fill_color="purple", back_color="white").convert('RGB')

# Calculate position to paste the embedded image (center of QR code)
pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

# Paste the image
img.paste(logo, pos)

# Save the final QR code with the embedded image
img.save('v2_qrcode.png')

print('QR code generated successfully with embedded image!')
