# pip install qrcode[pil]

import qrcode
import json

def generate_qrcode():

  data = ('''"posição": A1,
  "código": 31364,
  "Descrição": Placa Evaporativa,
  "Metragem": 500,
  "Lote": 12345678,
  "Data": 11/10/2024
  ''')

  qr = qrcode.QRCode(
      version=1,
      box_size=10,
      border=2
  )

  qr.add_data(data)
  qr.make(fit=True)


  img = qr.make_image(fill_color="black", back_color="white")
  img.save("teste.png")
  print("QR code gerado com sucesso!")

  return data

# Converter String em Json
def convert_to_Json():
    json_string_teste = input("Enter the JSON data: ")
    json_string = f'{{{json_string_teste}}}'

    try:
        data = json.loads(json_string)

        for key, value in data.items():
            print(f"{key}: {value}")

    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        
if __name__ == "__main__":
  generate_qrcode()
  