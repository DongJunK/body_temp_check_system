import os

class SendLog:
	def send_log(self, rasp_id, person_id, temp):
		os.system("sudo ./back/request_iot {} {} {}".format(rasp_id, person_id, temp))
