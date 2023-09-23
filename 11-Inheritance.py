class Phone:
    IMEI = None
    producer ="XiaoMi"
    def call_by_4g(self):
        print("4g通话")
class Phone2023(Phone):
    face_id = "10001"#面部识别ID
    def call_by_5g(self):
        print("2023年新功能：5g通话")

phone=Phone2023()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()
class NFCReader:
    nfc_type="第五代"
    producer="HW"
    def read_card(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")
class RomoteControl:
    rc_type="红外遥控"
    def control(self):
        print("红外遥控开启了")
class MyPhone(Phone,NFCReader,RomoteControl):
    #不想添加新功能，可以用pass补全语法
    pass
phone=MyPhone()
phone.call_by_4g()
phone.read_card()
phone.write_card()
phone.control()
#多继承时谁先继承，谁的优先级最高
print(phone.producer)