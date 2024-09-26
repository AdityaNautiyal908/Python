import pygame
import random
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Set the window dimensions
screen_width = 400
screen_height = 600

# Create the display window
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Flappy Bird")

# Game Variables
WIDTH = 450
HEIGHT = 600
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_SPEED = 5
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # In milliseconds
BIRD_WIDTH = 40
BIRD_HEIGHT = 30
pipe_color_day = (0, 255, 0)
pipe_color_night = (100, 100, 100)  # Darker color for night
volume = 0.5  # Default volume
game_speed = 60  # Default game speed
day_duration = 5000  # Duration of day in milliseconds
night_duration = 5000  # Duration of night in milliseconds

# Load cloud image
cloud_img = pygame.image.load('cloud.png')
cloud_img = pygame.transform.scale(cloud_img, (100, 60))  # Resize if necessary

# Load new background music and noon creature image
noon_background_music = 'noon_background_music.mp3'
star_img = pygame.image.load('star.png')  # Load your star image
star_img = pygame.transform.scale(star_img, (20, 20))  # Resize if necessary

# Load pipe images
pipe_top_img = pygame.image.load('pipe_top.png')
pipe_bottom_img = pygame.image.load('pipe_bottom.png')

bomb_img = pygame.image.load('bomb.png')  # Load your bomb image
bomb_img = pygame.transform.scale(bomb_img, (30, 30))  # Resize it to match the bomb dimensions

bird_skins = {
    'default': pygame.image.load('bird.png'),
    'skin1': pygame.image.load('bird_skin1.png'),
    'skin2': pygame.image.load('bird_skin2.png'),
}
# Scale the images
for key in bird_skins:
    bird_skins[key] = pygame.transform.scale(bird_skins[key], (BIRD_WIDTH, BIRD_HEIGHT))

# Resize pipe images if necessary
pipe_width = 50
pipe_top_img = pygame.transform.scale(pipe_top_img, (pipe_width, HEIGHT))
pipe_bottom_img = pygame.transform.scale(pipe_bottom_img, (pipe_width, HEIGHT))

# Load sound files
flap_sound = pygame.mixer.Sound('flap_sound.mp3')
cross_pipe_sound = pygame.mixer.Sound('cross_pipe.mp3')
death_sound = pygame.mixer.Sound('death.mp3')
high_score_sound = pygame.mixer.Sound('high_score.mp3')
background_music = 'background_music.mp3'

# Set volume for each sound
flap_sound.set_volume(volume)
cross_pipe_sound.set_volume(volume)
death_sound.set_volume(volume)
high_score_sound.set_volume(volume)
pygame.mixer.music.set_volume(volume)

# High Score File
HIGH_SCORE_FILE = "highscore.txt"

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Load Bird Image
bird_img = pygame.image.load('bird.png')
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))

# Start playing background music (loop infinitely)
pygame.mixer.music.load(background_music)
pygame.mixer.music.play(-1)

# Define Bird class
class Bird:
    def __init__(self, shop):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0
        self.rect = bird_img.get_rect(center=(self.x, self.y)).inflate(-10, -10)
        self.invincible = False
        self.is_dead = False
        self.shop = shop

    def update(self):
        if self.is_dead:
            # If the bird is dead, just let it fall to the bottom of the screen
            self.velocity += GRAVITY
            self.y += self.velocity
            self.rect.topleft = (self.x, self.y)
            if self.rect.top > HEIGHT:  # Ensure it stays off-screen
                self.rect.top = HEIGHT
            return

        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.topleft = (self.x, self.y)

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def flap(self):
        if not self.is_dead:
            self.velocity = FLAP_STRENGTH
            flap_sound.play()

    def draw(self, screen):
        screen.blit(bird_skins[self.shop.selected_skin], self.rect.topleft)


# Define Pipe class
class Pipe:
    def __init__(self, score):
        self.x = WIDTH
        self.pipe_gap = PIPE_GAP
        self.height = self.calculate_height(score)
        self.crossed = False
        self.single_pipe = False

        self.top_pipe = pygame.Rect(self.x, 0, pipe_width, self.height)
        self.bottom_pipe = None

        if random.random() < 0.2:  # 20% chance to create a single pipe
            self.single_pipe = True
        else:
            self.bottom_pipe = pygame.Rect(self.x, self.height + self.pipe_gap, pipe_width, HEIGHT - self.height - self.pipe_gap)

    def calculate_height(self, score):
        base_height = random.randint(100, 400)
        if score > 5:
            return max(base_height - (score - 5) * 10, 100)
        return base_height

    def update(self):
        self.x -= PIPE_SPEED
        self.top_pipe.x = self.x
        if self.bottom_pipe:
            self.bottom_pipe.x = self.x

    def draw(self, screen, is_day):
        pipe_color = pipe_color_day if is_day else pipe_color_night
        pygame.draw.rect(screen, pipe_color, self.top_pipe)
        if self.bottom_pipe:
            pygame.draw.rect(screen, pipe_color, self.bottom_pipe)

    def is_off_screen(self):
        return self.x + pipe_width < 0

    def check_crossed(self, bird):
        if self.x + pipe_width < bird.x and not self.crossed:
            self.crossed = True
            cross_pipe_sound.play()
            return True  # Indicate that the bird crossed the pipe
        return False

class Cloud:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(20, 150)  # Random vertical position for clouds
        self.speed = 1 + random.random()  # Random speed for some variation

    def update(self):
        self.x -= self.speed
        if self.x < -100:  # Reset position when it goes off-screen
            self.x = WIDTH + random.randint(0, 100)

    def draw(self, screen):
        screen.blit(cloud_img, (self.x, self.y))

class Star:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT // 2)  # Stars appear in the upper half of the screen
        self.size = random.randint(2, 5)  # Random size for stars

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), self.size)  # White stars

def check_collision(bird, pipes):
    if bird.rect.bottom >= HEIGHT:
        return True
    for pipe in pipes:
        if pipe.single_pipe:  # Only top pipe exists
            if bird.rect.colliderect(pipe.top_pipe.inflate(10, 0)):
                return True
        else:  # Both pipes exist
            if bird.rect.colliderect(pipe.top_pipe.inflate(10, 0)) or bird.rect.colliderect(pipe.bottom_pipe.inflate(10, 0)):
                return True
    return False

def load_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        with open(HIGH_SCORE_FILE, 'r') as file:
            return int(file.read())
    return 0

def save_high_score(high_score):
    with open(HIGH_SCORE_FILE, 'w') as file:
        file.write(str(high_score))

class Shop:
    def __init__(self):
        self.skins = {
            'default': {'price': 0, 'unlocked': True},
            'skin1': {'price': 10, 'unlocked': False},
            'skin2': {'price': 20, 'unlocked': False},
        }
        self.selected_skin = 'default'

    def draw(self, screen, score):
        font = pygame.font.SysFont(None, 30)
        screen.fill((173, 220, 250))
        y_offset = 100

        for skin, info in self.skins.items():
            if info['unlocked']:
                status = "Unlocked"
            else:
                status = f"Price: {info['price']} points"
            
            # Format the text to reduce space
            text_color = (0, 255, 0) if info['unlocked'] else (255, 0, 0)
            text = font.render(f"{skin}: {status}", True, text_color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, y_offset))
            y_offset += 30  # Adjusted to reduce vertical space

        current_skin_text = font.render(f"Current Skin: {self.selected_skin}", True, (255, 255, 255))
        screen.blit(current_skin_text, (WIDTH // 2 - current_skin_text.get_width() // 2, HEIGHT - 100))

        pygame.display.update()

    def buy_skin(self, skin, score):
        if skin in self.skins and not self.skins[skin]['unlocked']:
            if score >= self.skins[skin]['price']:
                score -= self.skins[skin]['price']
                self.skins[skin]['unlocked'] = True
                return score  # Return updated score after purchase
        return score  # Return unchanged score if purchase failed

    def select_skin(self, skin):
        if skin in self.skins and self.skins[skin]['unlocked']:
            self.selected_skin = skin

shop = Shop()

# Define Credit class
class Credit:
    def __init__(self):
        self.font = pygame.font.SysFont(None, 50)
        self.text = [
            "Developed by:",
            "Aditya Nautiyal",
            "Press any key to return"
        ]

    def draw(self, screen):
        screen.fill((173, 220, 250))
        for i, line in enumerate(self.text):
            color = (255, 255, 255)
            rendered_text = self.font.render(line, True, color)
            screen.blit(rendered_text, (WIDTH // 2 - rendered_text.get_width() // 2, 200 + i * 60))

        pygame.display.update()

    def run(self):
        while True:
            self.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return 'quit'
                if event.type == pygame.KEYDOWN:
                    return 'menu'

# Function to display the menu
def menu():
    font = pygame.font.SysFont(None, 50)
    menu_items = ['1. Play', '2. Options', '3. Credit', '4. Quit']
    selected = 0

    while True:
        screen.fill((173, 220, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu_items)
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu_items)
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        return 'play'
                    elif selected == 1:
                        return 'options'
                    elif selected == 2:
                        return 'credit'
                    elif selected == 3:
                        return 'quit'

        for i, item in enumerate(menu_items):
            color = (255, 0, 0) if i == selected else (255, 255, 255)
            text = font.render(item, True, color)
            screen.blit(text, (100, 200 + i * 60))

        pygame.display.update()

def reset_high_score():
    if os.path.exists(HIGH_SCORE_FILE):
        os.remove(HIGH_SCORE_FILE)

def options_menu(score):
    global volume, game_speed
    font = pygame.font.SysFont(None, 50)
    options_items = ['1. Volume', '2. Speed', '3. Reset High Score', '4. Shop', '5. Back']    
    selected = 0

    while True:
        screen.fill((173, 220, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options_items)
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options_items)
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        volume = (volume + 0.1) % 1.1
                        pygame.mixer.music.set_volume(volume)
                        cross_pipe_sound.set_volume(volume)
                        death_sound.set_volume(volume)
                        high_score_sound.set_volume(volume)
                    elif selected == 3:  # Enter shop
                        score = shop_menu(score)  # Use the passed score
                    elif selected == 1:
                        game_speed = (game_speed + 10) % 121
                    elif selected == 2:
                        reset_high_score()
                    elif selected == 4:
                        return

        for i, item in enumerate(options_items):
            color = (255, 0, 0) if i == selected else (255, 255, 255)
            text = font.render(item, True, color)
            screen.blit(text, (100, 200 + i * 50))

        volume_text = font.render(f"Volume: {volume:.1f}", True, (255, 255, 255))
        speed_text = font.render(f"Speed: {game_speed}", True, (255, 255, 255))
        screen.blit(volume_text, (100, 500))
        screen.blit(speed_text, (100, 460))

        pygame.display.update()

def shop_menu(score):
    selected = 0 
    options = ['Buy Skin 1', 'Buy Skin 2', 'Select Default Skin', 'Select Skin 1', 'Select Skin 2', 'Back']
    font = pygame.font.SysFont(None, 40)

    while True:
        shop.draw(screen, score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return score
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(options)
                elif event.key == pygame.K_UP:
                    selected = (selected - 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    if selected == 0:
                        score = shop.buy_skin('skin1', score)
                    elif selected == 1:
                        score = shop.buy_skin('skin2', score)
                    elif selected == 2:
                        shop.select_skin('default')
                    elif selected == 3:
                        shop.select_skin('skin1')
                    elif selected == 4:
                        shop.select_skin('skin2')
                    elif selected == 5:
                        return score

        # Drawing the options after event handling
        shop.draw(screen, score)  # Draw the shop with current score
        for i, item in enumerate(options):
            color = (255, 0, 0) if i == selected else (255, 255, 255)
            text = font.render(item, True, color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200 + i * 40))

        pygame.display.update()
        clock.tick(30)  # Limit the frame rate for smoother rendering

def pause_game():
    font = pygame.font.SysFont(None, 30)
    paused_text = font.render("Game Paused. Press ESC to Resume", True, (255, 255, 255))
    screen.blit(paused_text, (WIDTH // 2 - paused_text.get_width() // 2, HEIGHT // 2))
    
    pygame.display.update()

    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False

        clock.tick(5)

def game_over_menu(score, high_score):
    font = pygame.font.SysFont(None, 50)
    menu_items = ['Play Again', 'Quit']
    selected = 0
    
    while True:
        screen.fill((173, 220, 250))

        score_text = font.render(f"Your Score: {int(score)}", True, (255, 255, 255))
        high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 150))
        screen.blit(high_score_text, (WIDTH // 2 - high_score_text.get_width() // 2, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected = (selected + 1) % len(menu_items)
                if event.key == pygame.K_UP:
                    selected = (selected - 1) % len(menu_items)
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        return 'play'
                    elif selected == 1:
                        return 'quit'

        for i, item in enumerate(menu_items):
            color = (255, 0, 0) if i == selected else (255, 255, 255)
            text = font.render(item, True, color)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 300 + i * 60))

        pygame.display.update()

class Bomb:
    def __init__(self):
        self.x = WIDTH
        self.y = random.randint(100, HEIGHT - 100)  # Random vertical position
        self.width = 30
        self.height = 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.x -= PIPE_SPEED
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(bomb_img, self.rect.topleft)  # Draw the bomb image at its position

    def is_off_screen(self):
        return self.x + self.width < 0

def game_loop():
    global countdown, countdown_active, game_speed
    bird = Bird(shop)
    pipes = []
    bombs = []
    noon_creatures = []  # List to hold noon creatures
    stars = [Star() for _ in range(20)]  
    clouds = [Cloud() for _ in range(5)]
    pygame.time.set_timer(pygame.USEREVENT, PIPE_FREQUENCY)
    pygame.time.set_timer(pygame.USEREVENT + 1, 3000)
    
    score = 0
    high_score = load_high_score()
    font = pygame.font.SysFont(None, 36)

    running = True
    game_started = False
    countdown = 3
    countdown_active = False

    time_elapsed = 0
    is_day = True
    music_played = False  # To track if noon music has started
    frame_count = 0

    while running:
        frame_count += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_started:
                        game_started = True
                    else:
                        bird.flap()
                if event.key == pygame.K_ESCAPE:
                    pause_game()
            if event.type == pygame.USEREVENT and game_started:
                pipes.append(Pipe(score))
            if event.type == pygame.USEREVENT + 1 and game_started:
                bombs.append(Bomb())

        if countdown_active:
            if countdown > 0:
                countdown_text = font.render(f"Resume in: {int(countdown)}", True, (255, 255, 255))
                screen.blit(countdown_text, (WIDTH // 2 - countdown_text.get_width() // 2, HEIGHT // 2))
                countdown -= 0.1
                if countdown <= 0:
                    countdown = 0
                    countdown_active = False
            else:
                countdown_active = False
        else:
            if not game_started:
                prompt_text = font.render("Press SPACE to start", True, (255, 255, 255))
                screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGHT // 2))
            else:
                bird.update()
                for pipe in pipes:
                    pipe.update()
                    if pipe.check_crossed(bird):
                        score += 1
                for bomb in bombs:
                    bomb.update()
                for cloud in clouds:
                    cloud.update()

                if is_day and not music_played:  # Check for music switch
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(noon_background_music)
                    pygame.mixer.music.play(-1)
                    music_played = True  # Prevent reloading music

                if check_collision(bird, pipes) or any(bird.rect.colliderect(bomb.rect) for bomb in bombs):
                    bird.is_dead = True
                    death_sound.play()
                    pygame.time.delay(100)
                    result = handle_game_over(score, high_score)
                    if result == 'play':
                        return 0
                    elif result == 'quit':
                        return score

        time_elapsed += clock.get_time()
        if time_elapsed >= day_duration + night_duration:
            time_elapsed = 0
        is_day = time_elapsed < day_duration

        # Draw everything
        draw_game(screen, bird, pipes, bombs, clouds, stars, noon_creatures, score, high_score, is_day, font)        
        pygame.display.update()
        clock.tick(game_speed)

def draw_game(screen, bird, pipes, bombs, clouds, stars, noon_creatures, score, high_score, is_day, font):
    background_color = (135, 206, 250) if is_day else (0, 0, 50)
    screen.fill(background_color)
    bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen, is_day)
    for bomb in bombs:
        bomb.draw(screen)
    for cloud in clouds:
        cloud.draw(screen)
    for noon_creature in noon_creatures:
        noon_creature.draw(screen)  # Draw noon creatures

    if not is_day:
        for star in stars:
            star.draw(screen)

    score_text = font.render(f"Score: {int(score)}", True, (255, 255, 255))
    high_score_text = font.render(f"High Score: {high_score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    screen.blit(high_score_text, (10, 40))

def handle_game_over(score, high_score):
    if score > high_score:
        high_score = score
        save_high_score(high_score)
        high_score_sound.play()  # Play the high score sound here
    
    # Show the game over menu
    result = game_over_menu(score, high_score)
    return result  # Return the result of the game over menu

if __name__ == "__main__":
    current_score = 0  # Initialize current_score here
    while True:
        choice = menu()
        if choice == 'play':
            current_score = game_loop()  # Capture the score from game_loop
        elif choice == 'options':
            options_menu(current_score)  # Use current_score here
        elif choice == 'credit':
            credit = Credit()
            choice = credit.run()
            if choice == 'menu':
                continue
        elif choice == 'quit':
            pygame.quit()
            break


