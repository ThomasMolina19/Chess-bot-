import pygame
import chess

# Configura los parámetros de Pygame
pygame.init()
WIDTH, HEIGHT = 480, 480
SQUARE_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (200, 200, 200)
GREY = (200, 200, 200)
TEXT_COLOR = (0, 0, 0)

# Inicializa la pantalla
screen = pygame.display.set_mode((WIDTH + 40, HEIGHT + 40))
pygame.display.set_caption("Tablero de Ajedrez")

# Fuente para los números y letras
font = pygame.font.Font(None, 36)

# Dibuja el tablero de ajedrez
def draw_board(board):
    for row in range(8):
        for col in range(8):
            rect = pygame.Rect(20 + col * SQUARE_SIZE, 20 + row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, WHITE, rect)
            else:
                pygame.draw.rect(screen, BLACK, rect)

            piece = board.piece_at(row * 8 + col)
            if piece:
                piece_image = pygame.image.load(f'images/{piece.symbol()}.png')
                piece_image = pygame.transform.scale(piece_image, (SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(piece_image, rect.topleft)

    # Dibuja los números y letras
    for i in range(8):
        num_text = font.render(str(8 - i), True, TEXT_COLOR)
        screen.blit(num_text, (5, 20 + i * SQUARE_SIZE + (SQUARE_SIZE - num_text.get_height()) // 2))

        letter_text = font.render(chr(ord('a') + i), True, TEXT_COLOR)
        screen.blit(letter_text, (5 + i * SQUARE_SIZE + (SQUARE_SIZE - letter_text.get_width()) // 4, 5))

def main():
    board = chess.Board()
    board.push_san("e4")
    board.push_san("e5")
    board.push_san("Qh5")
    board.push_san("Bb4")
    board.push_san("Qe4")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(GREY)
        draw_board(board)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()