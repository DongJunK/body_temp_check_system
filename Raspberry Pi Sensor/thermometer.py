import ctypes

class TempControl:
	def __init__(self):
		global getTemp
		getTemp = ctypes.CDLL("./get_temp")
		getTemp.get_temp.restype = ctypes.c_char_p
	def get_temp(self):
		_temp = getTemp.get_temp()
		temp = ctypes.c_char_p(_temp).value
		return temp[0:5].decode('utf-8')

