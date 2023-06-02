import cv2
import os

def divide_image(image_path, rows, cols, folder_name):
    # 画像を読み込む
    image = cv2.imread(image_path)

    # 画像の高さと幅を取得
    height, width = image.shape[:2]

    # 分割する画像の高さと幅を計算
    piece_height = height // rows
    piece_width = width // cols

    # 分割された画像を保存するフォルダを作成
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    # 画像を分割して保存
    for i in range(rows):
        for j in range(cols):
            y = i * piece_height
            x = j * piece_width
            piece = image[y:y+piece_height, x:x+piece_width]
            cv2.imwrite(f"{folder_name}/piece_{i}_{j}.jpg", piece)