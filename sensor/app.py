import json
from qr_reader import QrCodeReader as QrReader
from iot_communication import SendLog
from thermometer import TempControl
from control_led import LedControl 
from control_buzzer import BuzzerControl
from time import sleep
def init():
    global rasp_id
    with open('./config/rasp_config.json','r') as f:
        config = json.load(f)
    rasp_id = config["rasp_id"]

def test_buzzer():
	buzzerControl = BuzzerControl()
	buzzerControl.turn_on_buzzer()
	del buzzerControl

def test_led():
	ledControl = LedControl()
	ledControl.turn_on_green()
	sleep(0.6)
	ledControl.turn_on_red()
	sleep(0.6)
	ledControl.turn_off_green()
	sleep(0.6)
	ledControl.turn_off_red()
	del ledControl

def test_qrReader():
	qrReader = QrReader()
	print(qrReader.getQrCode())

def test_temp():
	tempControl = TempControl()
	print(tempControl.get_temp())

def run():
	sendLog = SendLog()
	tempControl = TempControl()
	ledControl = LedControl()

	while True:
		print("start")
		qrReader = QrReader()
		buzzerControl = BuzzerControl()
		ledControl.turn_off_green()
		ledControl.turn_off_red()
		send_temp = tempControl.get_temp()
		print(send_temp)
		if float(send_temp) < 30:
			continue

		if float(send_temp) < 37.5:
			ledControl.turn_on_green()
		else:
			ledControl.turn_on_red()
		
		send_person_id = qrReader.getQrCode()
		qrReader.release()
		if send_person_id == "False":
			ledControl.turn_off_green()
			ledControl.turn_off_red()
			sleep(0.6)
			ledControl.turn_on_red()
			sleep(0.6)
			ledControl.turn_off_red()
			continue
		print(send_person_id)
		buzzerControl.turn_on_buzzer()
		sendLog.send_log(rasp_id, send_person_id, send_temp)
	del ledControl

if __name__ == '__main__':
    init()
    run()
