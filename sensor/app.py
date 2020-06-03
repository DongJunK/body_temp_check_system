import json
from qr_reader import QrCodeReader as QrReader

def init():
    global rasp_id
    with open('./config/rasp_config.json','r') as f:
        config = json.load(f)
    rasp_id = config["rasp_id"]

def run():
    qrReader = QrReader()
    tmp = qrReader.getQrCode()
    print(tmp)
                


if __name__ == '__main__':
    init()
    run()
