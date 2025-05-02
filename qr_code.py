# import qrcode

# data = input("Enter the data you want to encode: ")
# dest = input(
#     "Enter the full path destination of where you want your qrcode to be saved"
# )
# qr_name = input("Enter the name to save the image: ")
# dest = dest.replace("\\", "/")
# dest = dest + "/" + qr_name + ".png"
# img = qrcode.make(data)
# img.save(dest)
# print("Success! You can check the folder for the QR Code")

import pandas as pd

data = ['Steve', '35', 'Male', '3.5']
series = pd.Series(data, index=['Name', 'Age', 'Gender', 'Rating'])
print(series)

data = {
    'Name': ['Steve', 'Lia', 'Vin', 'katie'],
    'Age': [32, 28, 45, 38],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Rating': [3.45, 4.6, 3.9, 2.78]
}

