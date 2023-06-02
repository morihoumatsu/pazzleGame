import pygame
import tkinter as tk
from tkinter import ttk
from searchImage import searchImg
from Game import Game

# tkinterのテキスト入力ウィジェットとSubmitボタンを作成
root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", lambda: None)
text = tk.StringVar()
entry = ttk.Entry(root, textvariable=text)
entry.pack()
button = ttk.Button(root, text="確認", command=lambda: submit(text.get()))
button.pack()

# Pygameの描画領域を作成
pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)

# フォントの設定
font_path = "fonts/ipaexg.ttf"
font = pygame.font.Font(font_path, 32)
text_surface = font.render(text.get(), True, (0, 0, 0))
search_text = font.render("画像を検索しています。", True, (0, 0, 0))
inputFlg = True
searchFlg = False

def submit(value):
    # Submitボタンが押下されたときに呼ばれる関数
    # Pygame側に値を渡す
    global text_surface
    global searchFlg
    global inputFlg
    searchFlg = True
    inputFlg = False
    text_surface = font.render(value, True, (0, 0, 0))
    root.destroy()

# ゲームループ
while True:
    if inputFlg:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # tkinterのイベントを処理
        root.update()

        # 入力ボックスを表示する
        screen.fill((255, 255, 255))
        screen.blit(text_surface, (10, 10))
        pygame.display.flip()

    if searchFlg:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # 入力ボックスを表示する
        screen.fill((255, 255, 255))
        screen.blit(search_text, (10, 10))
        searchImg(text.get())
        pygame.display.flip()
        Game()