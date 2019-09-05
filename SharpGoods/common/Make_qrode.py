import qrcode
img = qrcode.make("")
img.save("./test.png")