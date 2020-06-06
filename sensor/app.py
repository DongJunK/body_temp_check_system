import json
from qr_reader import QrCodeReader as QrReader
from iot_communication import SendLog
from thermometer import TempControl
from control_led import LedControl 
from control_buzzer import BuzzerControl

def init():
    global rasp_id
    with open('./config/rasp_config.json','r') as f:
        config = json.load(f)
    rasp_id = config["rasp_id"]

def run():
	qrReader = QrReader()
	sendLog = SendLog()
	tempControl = TempControl()
	ledControl = LedControl()
	buzzerControl = BuzzerControl()
	
	sendLog.send_log(rasp_id,"5293291","35.7")
	
	while True:
		send_temp = tempControl.get_temp()
		
		if sned_temp < 30:
			continue

		if send_temp < 37.5:
			ledControl.turn_on_green()
		else:
			ledControl.turn_on_red()
		
		send_person_id = qrReader.getQrCode()
		
		if send_person_id == "False":
			ledControl.turn_off_green()
			ledControl.turn_off_red()
			
			continue

        buzzerControl.turn_on_buzzer()
		sendLog.send_log(rasp_id, send_person_id, send_temp)
	
	del ledControl
	del buzzerControl

if __name__ == '__main__':
    init()
    run()
