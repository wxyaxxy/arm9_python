#! /usr/bin/python3
import serial
import threading
import time


def SendDate():
    while True:
        # print("hello")
        # data = [1,2,3]
        # ser.write(data)
        # time.sleep(1)
        count = ser.inWaiting()
        if count != 0:
            # 读取内容并回显
            recv = ser.read(count)
            ser.write(recv)
        # 清空接收缓冲区
        ser.flushInput()
        # 必要的软件延时
        time.sleep(0.1)


data = [1, 2, 3]
# ser = serial.Serial(port="COM1")
ser = serial.Serial("/dev/ttyO4", 9600)
# ser.write(data)
a = threading.Timer(1, SendDate)
a.start()
