import pygame
import configparser
from PygameBase import PygameBase
from menu import Menu


class Main(PygameBase):

    def run_game(self):
        # 「パズルゲーム」のテキストの設定
        text = self.font.render("パズルゲーム", True, (0, 0, 0))
        # テキストを画面の中央より少し上に描画する
        text_rect = text.get_rect(center=(
              self.screen.get_width() // 2
            , self.screen.get_height() // 2 - 50))
        self.screen.blit(text, text_rect)
        # 「ゲームスタート」のテキストの設定
        start_text = self.font.render("画面クリックでゲームスタート", True, (0, 0, 0))
        # テキストを画面の下中央に描画する
        start_rect = start_text.get_rect(center=(
            self.screen.get_width() // 2, self.screen.get_height() - 100))
        self.screen.blit(start_text, start_rect)

        # ゲームループ
        running = True
        while running:
            # イベントの処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.click_sound.play()
                    Menu()

            # 画面の塗りつぶし
            self.set_background_color(self.background_color, self.screen)

            # 「パズルゲーム」と「ゲームスタート」のテキストを描画する
            self.draw_text(self.screen, text, text_rect)
            self.draw_text(self.screen, start_text, start_rect)

            # 画面の更新
            pygame.display.flip()

        # Pygameの終了
        pygame.quit()

    def __init__(self):
        super()
        pygame.init()
        # 設定ファイルの読み込み
        config = configparser.ConfigParser()
        config.read('config.ini')

        # [game] セクションから値を取得する
        game_config = config['game']

        # 画面の作成
        self.screen = self.create_screen(
            game_config.getint('screen_width'),
            game_config.getint('screen_height'),
            game_config.get('main_caption')
        )

        # 背景色の設定
        self.background_color = tuple(map(int, game_config.get('background_color').split(',')))
        # フォントの設定
        self.font = self.set_font(game_config.get('font_path'), 48)
        # クリック音の設定
        self.click_sound = self.set_click_sound(game_config.get('click_sound_path'))
        # BGMの設定
        self.set_music(game_config.get('music_path'))
        self.run_game()

if __name__ == '__main__':
    main2_instance = Main()