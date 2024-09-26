import pygame
import random

# Initialize pygame
pygame.init()

# Game Variables
WIDTH = 400
HEIGHT = 600
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_SPEED = 5
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # In milliseconds
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
pipe_color = (0, 255, 0)

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load Bird Image
bird_img = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
bird_img.fill((255, 255, 0))

# Define Bird class
class Bird:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0
        self.rect = bird_img.get_rect(topleft=(self.x, self.y))

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.topleft = (self.x, self.y)
        if self.rect.top < 0:
            self.rect.top = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH

    def draw(self, screen):
        screen.blit(bird_img, self.rect.topleft)

# Define Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(100, 400)
        self.top_pipe = pygame.Rect(self.x, 0, 50, self.height)
        self.bottom_pipe = pygame.Rect(self.x, self.height + PIPE_GAP, 50, HEIGHT - self.height - PIPE_GAP)

    def update(self):
        self.x -= PIPE_SPEED
        self.top_pipe.x = self.x
        self.bottom_pipe.x = self.x

    def draw(self, screen):
        pygame.draw.rect(screen, pipe_color, self.top_pipe)
        pygame.draw.rect(screen, pipe_color, self.bottom_pipe)

    def is_off_screen(self):
        return self.x + 50 < 0

# Function to check for collisions
def check_collision(bird, pipes):
    for pipe in pipes:
        if bird.rect.colliderect(pipe.top_pipe) or bird.rect.colliderect(pipe.bottom_pipe):
            return True
    if bird.rect.bottom >= HEIGHT:
        return True
    return False

# Main game loop
def game_loop():
    bird = Bird()
    pipes = []
    pygame.time.set_timer(pygame.USEREVENT, PIPE_FREQUENCY)
    score = 0
    font = pygame.font.SysFont(None, 36)

    running = True
    while running:
        screen.fill((135, 206, 250))  # Sky blue background

        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap()
            if event.type == pygame.USEREVENT:
                pipes.append(Pipe())

        # Update Bird and Pipes
        bird.update()
        for pipe in pipes:
            pipe.update()

        # Remove pipes that go off-screen
        pipes = [pipe for pipe in pipes if not pipe.is_off_screen()]

        # Check for collisions
        if check_collision(bird, pipes):
            print("Game Over! Your Score: ", score)
            running = False

        # Draw Bird and Pipes
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        # Draw score
        score += 1 / 100  # Score increases gradually
        score_text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update the screen and set frame rate
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
