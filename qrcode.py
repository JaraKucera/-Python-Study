import pyqrcode

url = input("Enter data you iwsh to store inside the QRCode: ")

big_code = pyqrcode.create(url, error='L', version=27, mode='binary')
big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
big_code.show()