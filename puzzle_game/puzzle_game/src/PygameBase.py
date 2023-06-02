import pygame
import configparser

class PygameBase:


    def create_screen(self, width, height, caption):

        # 画面の作成
        screen = pygame.display.set_mode((width, height))

        # ウィンドウのタイトル
        pygame.display.set_caption(caption)

        # 画面の作成
        return screen

    def set_font(self, font_path, font_size):
        # フォントの設定
        return pygame.font.Font(font_path, font_size)

    def set_click_sound(self, sound_path):
        # クリック音を設定
        return pygame.mixer.Sound(sound_path)

    def set_background_color(self, background_color, screen):
        # 背景色
        screen.fill(background_color)

    def render_text(self, text, font, text_color):
        # テキストのレンダリング
        return font.render(text, True, text_color)

    def set_music(self, sound_path):
        # BGMの読み込み
        pygame.mixer.music.stop()
        pygame.mixer.music.load(sound_path)
        # BGMの再生（ループ再生）
        pygame.mixer.music.play(-1)

    def stop_music(self):
        pygame.mixer.music.stop()

    def draw_text(self, screen, text, rect):
        # テキストの描画
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    def draw_text_center(self, screen, text, x: int, y: int):
        # テキストを画面の中央に描画する
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)
    
    def create_button(self, font, text: str, button_width: int, button_height: int, center_x: int, center_y: int, color):
        button = pygame.Rect(center_x, center_y, button_width, button_height)
        text = font.render(text, True, color)
        rect = text.get_rect(center=button.center) # type: ignore
        return button, text, rect
    
    def draw_button(self, screen, button, text, mouse_x, mouse_y, text_rect):
        # マウスカーソルの位置によって色を変える
        if button.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, (100, 100, 255), button)
            pygame.draw.rect(screen, (255, 255, 255), button, 2)
        else:
            pygame.draw.rect(screen, (0, 0, 255), button)
            pygame.draw.rect(screen, (255, 255, 255), button, 2)
        screen.blit(text, text_rect)