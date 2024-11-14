import qrcode
site_name = input("site web link : ")  
save_path = input("path : ")  

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=100,
                   border=2)

qr.add_data(site_name)  
qr.make(fit=True)
img = qr.make_image(fill_color="black")
img.save(save_path)  