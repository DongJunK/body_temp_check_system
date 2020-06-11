import pyzbar.pyzbar as pyzbar
import cv2
import threading
from time import sleep

class QrCodeReader:
    end_check = False
    
    def release(self):
        cap.release()
        cv2.destroyAllWindows()
    
    def countSec(self):
        now_time = 0
        while True:
            now_time+=1
            sleep(1)
            if now_time == 10:
                self.end_check = True
                break
    def checkTime(self):
        time_check = threading.Thread(target=self.countSec)
       
        time_check.start()

    def getQrCode(self):
        global cap
        cap = cv2.VideoCapture(0)
        self.checkTime()
        while(cap.isOpened()):
            ret, img = cap.read()
            if self.end_check == True:
                self.release()
                return "False"
            if not ret:
                continue
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            decoded = pyzbar.decode(gray)
            for d in decoded:
                barcode_data = d.data.decode("utf-8")
                barcode_type = d.type
                if barcode_type == "QRCODE":
                    return barcode_data[0:7]

