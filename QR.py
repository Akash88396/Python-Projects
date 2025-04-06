# import qrcode

# data = input("Enter the text or URL :").strip()
# filename = input("Enter file name with extension (.jpg) :").strip()

# qr = qrcode.QRCode(box_size=20, border = 4)
# qr.add_data(data)
# image = qr.make_image(fill_color='red',back_color='white')
# image.save(filename)

# print(f'QR code is saved in {filename}')



#                              my code

import qrcode

data = input("Enter Url :")
fileName = input("Enter file name with .jpg extension:")

qr = qrcode.QRCode(border=5,box_size= 10)
qr.add_data(data)

image = qr.make_image(fill_color ='black',back_color='white')
image.save(fileName)

print(f' Image is saved in {fileName}')