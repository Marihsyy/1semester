import qrcode

def demo_qrcode():
    img = qrcode.make("Hello Python")
    img.save("qrcode.png")
    print("[qrcode] QR code created")