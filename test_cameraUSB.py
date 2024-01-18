import cv2

# 初始化摄像头，0通常是内置摄像头，如果你有多个摄像头可以尝试1, 2, 3...
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("无法打开摄像头")
    exit()

while True:
    # 读取摄像头帧
    ret, frame = cap.read()

    # 如果正确读取帧，ret为True
    if not ret:
        print("无法从摄像头读取帧。")
        break

    # 显示结果帧
    cv2.imshow('摄像头实时画面', frame)

    # 按 'q' 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头资源
cap.release()
cv2.destroyAllWindows()
