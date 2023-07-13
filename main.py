import requests

class Packer:
    def __init__(self):
        pass


def compute_crc8_simple_onebyte_shiftreg(byte_val):
    generator = 0x1D
    crc = 0

    input_stream = [byte_val, 0x00]

    for b in input_stream:
        for i in range(7, -1, -1):
            if crc & 0x80 != 0:
                crc = (crc << 1) & 0xFF
                crc |= 0x01 if (b & (1 << i)) != 0 else 0xFE
                crc ^= generator
            else:
                crc = (crc << 1) & 0xFF
                crc |= 0x01 if (b & (1 << i)) != 0 else 0xFE

    return crc

if __name__ == '__main__':
    r = requests.post('http://localhost:9998', 'BQEEDQQDqw')
    # Декодирование содержимого ответа с помощью метода content.decode()
    # URL - encoded
    # Base64
    # CRC8
    import base
    a = 'eW91ciB0ZXh0'
    #print(base64.b64decode(r.text))
    print(base.urlsafe_b64decode(r.text))
    import base64, json

    #b = b'DbMG_38BBgaI0Kv6kzGK'
    #a = base64.urlsafe_b64decode(r.text +'=')
    # c = json.loads(a)
    #
    # print(c)

    # Кодирование в URL-кодированную непропущенную Base64
    # encoded_data = base64.urlsafe_b64encode(data).decode()
    # print("Кодированные данные:", encoded_data)

    # Декодирование из URL-кодированной непропущенной Base64
    # decoded_data = base64.urlsafe_b64decode(r.text.encode())
    # #print("Декодированные данные:", decoded_data.decode())
    #
    # # Или декодирование с помощью атрибута text
    # decoded_text = r.text
    # print(decoded_text)
    # print(r.text)
    #
    #
    # def calculate_crc8(data):
    #     crc = 0x00
    #     polynomial = 0x8C
    #
    #     for byte in data:
    #         crc ^= byte
    #         for _ in range(8):
    #             if crc & 0x80:
    #                 crc = (crc << 1) ^ polynomial
    #             else:
    #                 crc <<= 1
    #
    #     return crc
    #
    #
    # calculated_crc = calculate_crc8(base64.urlsafe_b64decode(r.text.encode()))

