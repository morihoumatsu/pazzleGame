import pygame
import sys
import os
import random
import copy
import configparser
from menu import Menu
from util import divide_image
from PygameBase import PygameBase

class Game(PygameBase):

    def run_game(self):
        # 画像の読み込み
        divide_image(self.image_path, self.rows, self.cols, self.folder_name)
        image_files = os.listdir(self.pazzle_path)
        image_list = [pygame.image.load(os.path.join(self.pazzle_path, file)) for file in image_files]

        # 画像の分割サイズ
        piece_width = image_list[0].get_width()
        piece_height = image_list[0].get_height()

        # キャンバスの作成
        canvas_width = piece_width * self.cols + 10 * (self.cols - 1)  # 10は空白部分の幅
        canvas_height = piece_height * self.rows + 10 * (self.rows - 1)  # 10は空白部分の高さ
        canvas = pygame.Surface((canvas_width, canvas_height))

        # ピースの描画座標をランダムに並び替える
        pieces = [(i, j) for i in range(self.rows) for j in range(self.cols)]
        random.shuffle(pieces)

        # 画像の描画
        for i, image_piece in enumerate(image_list): # type: ignore
            row, col = pieces[i]
            x = col * (piece_width + 10)  # 10は空白部分の幅
            y = row * (piece_height + 10)  # 10は空白部分の高さ
            canvas.blit(image_piece, (x, y))

        clear_font = pygame.font.Font(None, 100)
        clear_text = clear_font.render("ゲームクリア！", True, (255, 255, 0))
        clear_rect = clear_text.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
        start_ticks = 0

        selected_piece = None
        first_selected_piece = None
        game_clear = False
        gameStart = True
        imageSearch = True

        while True:
            # ゲームスタート
            if gameStart:
                # イベントの処理
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.click_sound.play()
                        x, y = event.pos
                        row = (y - (self.screen_height // 2 - canvas_height // 2)) // (piece_height + 11)
                        col = (x - (self.screen_width // 2 - canvas_width // 2)) // (piece_width + 10)
                        if selected_piece is None:
                            selected_piece = (row, col)
                            first_selected_piece = selected_piece
                        else:
                            # ここで、pieces_copy を操作するように変更する
                            pieces_copy = copy.deepcopy(pieces)
                            pieces_copy[pieces.index(selected_piece)] = pieces_copy[pieces.index((row, col))]
                            pieces_copy[pieces.index((row, col))] = first_selected_piece # type: ignore
                            pieces = pieces_copy
                            selected_piece = None
                            first_selected_piece = None
                            canvas.fill(self.background_color)
                            for i, image_piece in enumerate(image_list):
                                row, col = pieces[i]
                                x = col * (piece_width + 10)  # 10は空白部分の幅
                                y = row * (piece_height + 10)  # 10は空白部分の高さ
                                canvas.blit(image_piece, (x, y))

            # 画面の塗りつぶし
            self.screen.fill(self.background_color)

            # キャンバスの描画
            self.screen.blit(canvas, (self.screen_width // 2 - canvas_width // 2, self.screen_height // 2 - canvas_height // 2))

            # 青い枠線の描画
            if selected_piece is not None:
                row, col = selected_piece
                x = col * (piece_width + 10)  # 10は空白部分の幅
                y = row * (piece_height + 10)  # 10は空白部分の高さ
                pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(x + self.screen_width // 2 - canvas_width // 2, y + self.screen_height // 2 - canvas_height // 2, piece_width, piece_height), 5)

            # 画面の更新
            pygame.display.flip()

            # ゲームクリアの判定
            if pieces == [(i, j) for i in range(self.rows) for j in range(self.cols)]:
                if game_clear == False:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("sound/clear.mp3")
                    pygame.mixer.music.play(-1)
                    start_ticks = pygame.time.get_ticks()
                game_clear = True
            # ゲームクリア時の処理
            if game_clear:
                self.screen.blit(clear_text, clear_rect)
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000
                if seconds > 3:
                    pygame.mixer.music.stop()
                    Menu()


    def __init__(self):
        super()
        pygame.init()
        # 設定ファイルの読み込み
        config = configparser.ConfigParser()
        config.read('config.ini')

        # [game] セクションから値を取得する
        game_config = config['game']

        self.screen_width = game_config.getint('screen_width')
        self.screen_height = game_config.getint('screen_height')
        config = game_config.get('game_caption')
        # 画面の作成
        self.screen = self.create_screen(
            self.screen_width,
            self.screen_height,
            config
        )

        # 背景色の設定
        self.background_color = tuple(map(int, game_config.get('background_color').split(',')))
        # フォントの設定
        self.font = self.set_font(game_config.get('font_path'), 48)
        # クリック音の設定
        self.click_sound = self.set_click_sound(game_config.get('click_sound_path'))
        self.image_path = game_config.get('image_path')
        # BGMの設定
        self.stop_music()
        self.set_music(game_config.get('music_path2'))
        self.rows = 3
        self.cols = 3
        self.folder_name = 'pazzle'
        self.pazzle_path = game_config.get('pazzle_path')
        self.run_game()

if __name__ == '__main__':
    Game_instance = Game()