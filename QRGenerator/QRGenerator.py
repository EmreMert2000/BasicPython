import qrcode

# QR kodu için URL veya metin
data = "https://www.Nizamyap.com"

# QR kodu oluşturma
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# QR kodu görselini oluşturma ve kaydetme
img = qr.make_image(fill="black", back_color="white")
img.save("NizamYapiQRCode.png")
