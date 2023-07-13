import base
import urllib.parse

def compute_crc8_simple_onebyte_shiftreg(byteVal):
    generator = 0x1D
    crc = 0
    inputstream = bytearray([byteVal, 0x00])

    for b in inputstream:
        for i in range(7, -1, -1):
            if crc & 0x80 != 0:
                crc = crc << 1
                crc = ((b & (1 << i)) != 0) and (crc | 0x01) or (crc & 0xFE)
                crc = crc ^ generator
            else:
                crc = crc << 1
                crc = ((b & (1 << i)) != 0) and (crc | 0x01) or (crc & 0xFE)

    return crc
byte_val = 0xAB
crc = compute_crc8_simple_onebyte_shiftreg(byte_val)
print(hex(crc))  # Выводит значение CRC в шестнадцатеричной форме


data = b"Hello, World!"  # Данные для кодирования

# Кодирование в URL-кодированную неполную Base64
encoded_data = base64.urlsafe_b64encode(data).rstrip(b'=').decode()
url_encoded_data = urllib.parse.quote(encoded_data)

print("URL-кодированные данные:", url_encoded_data)



decoded_url_encoded_data = urllib.parse.unquote(url_encoded_data)
decoded_data = base64.urlsafe_b64decode(decoded_url_encoded_data + '==')

print("Декодированные данные:", decoded_data.decode())