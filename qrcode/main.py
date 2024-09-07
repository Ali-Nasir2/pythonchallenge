import qrcode

data= "link of whatever you want to generate qr code for"

img= qrcode.make(data)

img.save("qrcode.png")

img.show()

