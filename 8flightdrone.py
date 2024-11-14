from djitellopy import Tello
import time

# สร้างตัวแปร Tello
tello = Tello()

# เชื่อมต่อกับโดรน
tello.connect()

# ตั้งความเร็วเป็น 100 cm/s (ความเร็วสูงสุด)
tello.set_speed(100)

# ตรวจสอบสถานะแบตเตอรี่
print(f"Battery level: {tello.get_battery()}%")

# บินขึ้น
tello.takeoff()
tello.move_up(50)
#takeoff
#loop

setting = {
    't_2': 300,
    't_3': 165,
    't_4': 250,
    't_5': 165,
    't_6': 250,
    't_7': 165,
    't_8': 300,
    't_1': 165,
}
for count in range(10):
    print(setting)
    if count == 5 or count == 6 or count == 7:
        setting['t_8'] += 5
        setting['t_2'] += 5

    # 2
    tello.move_forward(setting['t_2'])
    # 3
    tello.move_left(setting['t_3'])
    # 4
    tello.move_forward(setting['t_4'])
    # 5
    tello.move_right(setting['t_5'])
    # 6
    tello.move_back(setting['t_6'])
    # 7
    tello.move_left(setting['t_7'])
    # 8
    tello.move_back(setting['t_8'])
    # 1
    tello.move_right(setting['t_1'])

tello.move_back(50)

tello.land()
tello.end()