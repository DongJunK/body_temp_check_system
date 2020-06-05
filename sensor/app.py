import json
from qr_reader import QrCodeReader as QrReader
from iot_communication import SendLog

def init():
    global rasp_id
    with open('./config/rasp_config.json','r') as f:
        config = json.load(f)
    rasp_id = config["rasp_id"]

def run():
	#qrReader = QrReader()
	#tmp = qrReader.getQrCode()
	#print(tmp)
	sendLog = SendLog()
	sendLog.send_log(rasp_id,"5293291","35.7")
                


if __name__ == '__main__':
    init()
    run()
