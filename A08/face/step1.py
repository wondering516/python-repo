'''
1. opencv
    图像处理

2. dlib
    1) 人脸检测, 训练数据
        从图片中提取人脸所在的区域
        提取68个特征点
    2) 人脸识别, 训练数据
        由特征点生成128D向量
        对比两张图片生成的向量, 欧氏距离
'''

# 调用摄像头, 拍照
import cv2

def get_photo():
    # 加载摄像头
    cap = cv2.VideoCapture(0)  # 获取默认的摄像头

    while True:
        # 拍照
        flag, photo = cap.read()

        # 在图片上绘制一行文字
        cv2.putText(photo,
                    'Press space to take photos',
                    (10, 60),
                    cv2.FONT_HERSHEY_COMPLEX,
                    1,
                    (0, 0, 255))    # 常规(R, G, B)  (B, G, R)

        # 将照片显示出来
        cv2.imshow('Camera', photo)

        # 等待一个键盘事件
        key = cv2.waitKey(1)
        print(key)

        # 按下空格键时, 跳出循环
        if key == ord(' '):

            # 关闭摄像头
            cap.release()

            # 关闭显示窗口
            cv2.destroyAllWindows()

            return photo

if __name__ == '__main__':
    photo = get_photo()

    print(type(photo))
    print(photo)