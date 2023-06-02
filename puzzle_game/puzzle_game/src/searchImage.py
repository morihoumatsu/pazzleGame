import os
import requests
import random
from bs4 import BeautifulSoup
from PIL import Image

def get_image(keyword, download_path):
    # 検索クエリを作成
    url = 'https://www.google.com/search?q={}&source=lnms&tbm=isch'.format(keyword)

    # 検索結果ページを取得
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # 画像を取得
    images = soup.find_all('img')
    for i, image in enumerate(images): # type: ignore
        try:
            # 画像のURLを取得
            url = image.get('src')

            # 画像をダウンロード
            res = requests.get(url, timeout=10)
            if res.status_code != 200:
                continue

            # ファイル名を作成
            _, ext = os.path.splitext(url)
            filename = '{}{}.png'.format(i, ext)

            # ダウンロードした画像を保存するパスを作成
            image_path = os.path.join(download_path, filename)

            # 画像を開く
            with open(image_path, 'wb') as f:
                f.write(res.content)

            # リサイズする
            with Image.open(image_path) as img:
                # 画像をリサイズ
                resized_image = img.resize((800, 600))

                # 画像を保存
                resized_image.save(image_path)

        except Exception as e:
            print(e)

def searchImg(text):
    keyword = text
    download_path = 'images'
    delete_folder_contents('images')
    delete_folder_contents('pazzle')
    get_image(keyword, download_path)
    changeFileName('images')

def delete_folder_contents(path):
    # フォルダ内のファイルとサブフォルダのリストを取得
    files = os.listdir(path)

    # ファイルを削除
    for file in files:
        file_path = os.path.join(path, file)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                delete_folder_contents(file_path)
        except Exception as e:
            print(e)

def changeFileName(path):
    folder_path = path
    files = os.listdir(folder_path)
    random_file = random.choice(files)
    os.rename(path +'/'+ random_file, 'images/puzzle.png' )