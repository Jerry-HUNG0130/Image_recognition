import cv2

#1
#YOLO 模型通常要求輸入固定大小的影像（例如 640X640)，調整照片大小
def resize_image(image_path, output_path, size=(640, 640)):
    img = cv2.imread(image_path)
    if img is not None:
        # 使用 INTER_AREA 對縮小影像效果較好，INTER_CUBIC 對放大較好
        resized = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
        cv2.imwrite(output_path, resized)