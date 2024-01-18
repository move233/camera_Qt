import serial
import binascii
import cv2
import time

# 初始化串口
ser = serial.Serial(
    port='COM5',     # 串口号
    baudrate=115200, # 波特率
    bytesize=8,      # 字节大小
    parity='N',      # 奇偶校验
    stopbits=1,      # 停止位
)

# 十六进制字符串，正转60度
hex_string1 = " 01 64 01 00 00 0a aa 00 00 15 55 00 00 00 31 8f"
fk1 = b'\x01d\x01\x00\x00\n\xaa\x00\x00\x15U\x00\x00\x001\x8f'
# 十六进制字符串，反转60度
hex_string2 = " 01 64 01 00 00 0a aa ff ff ea ab 00 00 00 0f 73"
fk2 = b'\x01d\x01\x00\x00\n\xaa\xff\xff\xea\xab\x00\x00\x00\x0fs'
# 将十六进制字符串转换为字节
bytes_to_send1 = binascii.unhexlify(hex_string1.replace(" ", ""))
bytes_to_send2 = binascii.unhexlify(hex_string2.replace(" ", ""))

# 打开摄像头
cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("无法打开摄像头")
    ser.close()
    exit()

def take_photo(frame, count):
    photo_name = f"photo_{count}.jpg"
    cv2.imwrite(photo_name, frame)
    print(f"拍照成功，图片保存为: {photo_name}")

count = 0
try:
    # 向串口发送6次数据
    for _ in range(6):
        ser.write(bytes_to_send1)
        time.sleep(0.1)  #每次间隔0.1秒

        # 检查是否接收到特定的拍照信号
        if ser.in_waiting:
            data = ser.read(ser.in_waiting)
            if data == fk1:
                time.sleep(0.07)  # 接收到信号后等待0.1秒
                count += 1
                ret, frame = cap.read()
                if ret:
                    take_photo(frame, count)
                else:
                    print("无法读取摄像头帧")

except KeyboardInterrupt:
    print("程序中断")

finally:
    # 释放摄像头并关闭所有窗口
    cap.release()
    cv2.destroyAllWindows()
    ser.close()
