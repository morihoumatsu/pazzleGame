import pygame
import configparser
import sys
from PygameBase import PygameBase


class Menu(PygameBase):

    def run_game(self):

        # 画面のサイズ
        screen_width = 800
        screen_height = 600

        # 画面の作成
        screen = pygame.display.set_mode((screen_width, screen_height))

        # ボタンの設定
        button_width = 400
        button_height = 100
        button_spacing = 50

        # 「ゲーム開始」のボタンの設定
        start_button, start_text, start_rect = self.create_button(
            self.font
            , "ゲーム開始"
            , button_width
            , button_height
            , (screen_width - button_width) // 2
            , (screen_height - button_height * 3 - button_spacing * 2) // 2
            , (255, 255, 255)
        )

        # 「スコア表示」のボタンの設定
        score_button, score_text, score_rect = self.create_button(
            self.font
            , "スコア表示"
            , button_width
            , button_height
            , (screen_width - button_width) // 2
            , start_button.bottom + button_spacing
            , (255, 255, 255)
        )

        # 「ランキング表示」のボタンの設定
        ranking_button, ranking_text, ranking_rect = self.create_button(
            self.font
            , "スコア表示"
            , button_width
            , button_height
            , (screen_width - button_width) // 2
            , score_button.bottom + button_spacing
            , (255, 255, 255)
        )

        mouse_x = 0
        mouse_y = 0

        # ゲームループ
        while True:
            # イベントの処理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # クリックされた座標を取得する
                    mouse_x, mouse_y = event.pos
                    if start_button.collidepoint(mouse_x, mouse_y):
                        import search
                        search.run(); # type: ignore
                    # 「スコア表示」のテキストがクリックされたら、スコア画面に遷移する
                    elif score_button.collidepoint(mouse_x, mouse_y):
                        # TODO: スコア画面への遷移
                        pass
                    # 「ランキング表示」のテキストがクリックされたら、ランキング画面に遷移する
                    elif ranking_button.collidepoint(mouse_x, mouse_y):
                        # TODO: ランキング画面への遷移
                        pass

            # 画面の塗りつぶし
            self.set_background_color(self.background_color, self.screen)

            # 「ゲーム開始」のボタン
            start_rect = start_text.get_rect(center=start_button.center) # type: ignore
            self.draw_button(screen, start_button, start_text, mouse_x, mouse_y, start_rect)

            # 「スコア表示」のボタン
            score_rect = score_text.get_rect(center=score_button.center) # type: ignore
            self.draw_button(screen, score_button, score_text, mouse_x, mouse_y, score_rect)

            # 「ランキング表示」のボタン
            ranking_rect = ranking_text.get_rect(center=ranking_button.center) # type: ignore
            self.draw_button(screen, ranking_button, ranking_text, mouse_x, mouse_y, ranking_rect)

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
            game_config.get('menu_caption')
        )

        # 背景色の設定
        self.background_color = tuple(map(int, game_config.get('background_color').split(',')))
        # フォントの設定
        self.font = self.set_font(game_config.get('font_path'), 48)
        # クリック音の設定
        self.click_sound = self.set_click_sound(game_config.get('click_sound_path'))
        self.run_game()

if __name__ == '__main__':
    main2_instance = Menu()