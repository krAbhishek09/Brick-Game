import pygame

# Initialize Pygame
pygame.init()

WHITE = (255, 255, 255)
DARKBLUE = (36, 90, 190)
LIGHTBLUE = (0, 176, 240)
RED = (255, 0, 0)

# Bricks
brick1 = [pygame.Rect(10 + i * 100, 60, 80, 30) for i in range(6)]
brick2 = [pygame.Rect(10 + i * 100, 100, 80, 30) for i in range(6)]
brick3 = [pygame.Rect(10 + i * 100, 140, 80, 30) for i in range(6)]

# Brick draw on screen


def draw_brick(brick):
    for i in brick:
        pygame.draw.rect(screen, RED, i)


score = 0
velocity = [1, 1]

size = (600, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My First Game")

paddle = pygame.Rect(100, 550, 200, 10)
ball = pygame.Rect(50, 250, 10, 10)

game_continue = True

while game_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_continue = False

    screen.fill(DARKBLUE)

    pygame.draw.rect(screen, LIGHTBLUE, paddle)

    font = pygame.font.Font(None, 34)
    text = font.render("SCORE " + str(score), 1, WHITE)
    screen.blit(text, (20, 10))

    # Paddle move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.x > 0:
        paddle.x -= 5
    if keys[pygame.K_RIGHT] and paddle.x < 540:
        paddle.x += 5

    # Creating bricks
    draw_brick(brick1)
    draw_brick(brick2)
    draw_brick(brick3)

    # Ball movement
    ball.x += velocity[0]
    ball.y += velocity[1]

    if ball.x > 590 or ball.x < 0:
        velocity[0] = -velocity[0]

    if paddle.collidepoint(ball.x, ball.y):
        velocity[1] = -velocity[1]

    if ball.y >= 590:
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", 1, RED)
        screen.blit(text, (150, 350))
        pygame.display.flip()
        pygame.time.wait(2000)
        break

    pygame.draw.rect(screen, WHITE, ball)

    for brick in [brick1, brick2, brick3]:
        for i in brick:
            if i.collidepoint(ball.x, ball.y):
                brick.remove(i)
                velocity[0] = -velocity[0]
                velocity[1] = -velocity[1]
                score += 1

    if score == 18:
        font = pygame.font.Font(None, 74)
        text = font.render("You Won", 1, RED)
        screen.blit(text, (150, 350))
        pygame.display.flip()
        pygame.time.wait(3000)
        break

    pygame.time.wait(10)
    pygame.display.flip()

pygame.quit()
