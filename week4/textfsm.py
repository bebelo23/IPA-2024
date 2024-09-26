import textfsm
from netmiko import ConnectHandler
import argparse

# ตั้งค่าการเชื่อมต่อกับเราเตอร์ R2-P
router = {
    "device_type": "cisco_ios",
    "host": "172.31.101.4",
    "username": "admin",
    "password": "cisco",
}

# ฟังก์ชันแปลงชื่ออินเทอร์เฟซให้เป็นชื่อเต็ม
def normalize_output(interface_name):
    interface_name = interface_name.lower()
    if interface_name.startswith("g"):
        return "gigabitethernet" + interface_name[1:]
    elif interface_name.startswith("f"):
        return "fastethernet" + interface_name[1:]
    return interface_name

# รับอินพุตชื่ออินเทอร์เฟซจากผู้ใช้ผ่าน command line argument
parser = argparse.ArgumentParser(description="Interface name")
parser.add_argument("interfacename", help="Interface name")
args = parser.parse_args()

# ปรับชื่ออินเทอร์เฟซที่รับเข้ามา
interfacename = normalize_output(args.interfacename)

# เชื่อมต่อกับเราเตอร์และรันคำสั่ง show ip int brief
Connection = ConnectHandler(**router)
Connection.enable()
output = Connection.send_command("show ip int brief")
Connection.disconnect()

# โหลดเทมเพลต TextFSM
with open("templates/router-textfsm.tpl") as template:
    fsm = textfsm.TextFSM(template)
    result = fsm.ParseText(output)

# ค้นหาอินเทอร์เฟซที่ตรงกับพารามิเตอร์ที่รับเข้ามา
found = False
for entry in result:
    if entry[0].lower() == interfacename:
        print(f"Interface: {entry[0]}, IP address = {entry[1]}, Status = {entry[2]}")
        found = True
        break

# แสดงผลหากไม่พบอินเทอร์เฟซที่ค้นหา
if not found:
    print(f"Interface {interfacename} not found")
