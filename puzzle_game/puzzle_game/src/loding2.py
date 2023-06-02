import pygame

# 画面の幅と高さ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 背景色
BACKGROUND_COLOR = (255, 255, 255)

# フォントの設定
FONT_PATH = "fonts/ipaexg.ttf"
FONT_SIZE = 48
FONT_COLOR = (0, 0, 0)
pygame.font.init()  # フォントを初期化
FONT = pygame.font.Font(FONT_PATH, FONT_SIZE)

def draw_loading(screen, x, y, radius, thickness, color, angle):
    # ぐるぐるを回転させる
    image = pygame.Surface((radius * 2, radius * 2))
    image.set_colorkey((0, 0, 0))
    rect = pygame.draw.circle(image, color, (radius, radius), radius, thickness)
    pygame.draw.circle(image, color, (radius, radius), radius * 2 // 3, thickness)
    pygame.draw.circle(image, color, (radius, radius), radius // 3, thickness)
    image = pygame.transform.rotate(image, angle)
    rect = image.get_rect(center=(x, y))
    screen.blit(image, rect)

# Pygameの初期化
pygame.init()

# 画面の作成
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ウィンドウのタイトル
pygame.display.set_caption("Loading")

# ゲームループ
running = True
angle = 0  # ぐるぐるの角度
clock = pygame.time.Clock()  # クロックオブジェクトを作成
while running:
    # イベントの処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 画面の塗りつぶし
    screen.fill(BACKGROUND_COLOR)

    # テキストの描画
    text = FONT.render("画像を取得中", True, FONT_COLOR)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    screen.blit(text, text_rect)

    # ぐるぐるの描画
    draw_loading(screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, 50, 5, (0, 0, 0), angle)
    angle += 5  # 角度を5度ずつ増やす

    # 画面の更新
    pygame.display.flip()

    # 60 FPSになるように待つ
    clock.tick(60)

# Pygameの終了
pygame.quit()