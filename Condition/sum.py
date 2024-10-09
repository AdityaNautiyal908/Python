import pygame
from pygame.locals import *
import sys
import time
import random

class Game:
    def __init__(self):
        self.w = 750
        self.h = 500
        self.reset = True
        self.active = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.accuracy = '0%'
        self.results = 'Time: 0 Accuracy: 0% Wpm: 0'
        self.wpm = 0
        self.end = False
        self.HEAD_C = (255, 213, 102)
        self.TEXT_C = (240, 240, 240)
        self.RESULT_C = (255, 70, 70)
        
        pygame.init()
        self.open_img = pygame.image.load('type-speed-open.png')
        self.open_img = pygame.transform.scale(self.open_img, (self.w, self.h))
        self.bg = pygame.image.load('background.jpg')
        self.bg = pygame.transform.scale(self.bg, (self.w, self.h))
        self.screen = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Type Speed Test')

    def draw_text(self, msg, y, fsize, color):
        font = pygame.font.Font(None, fsize)
        text = font.render(msg, 1, color)
        text_rect = text.get_rect(center=(self.w / 2, y))
        self.screen.blit(text, text_rect)
        pygame.display.update()

    def get_sentence(self):
        with open('sentences.txt') as f:
            sentences = f.read().splitlines()
        return random.choice(sentences) if sentences else ''

    def show_results(self):
        if not self.end:
            # Calculate time
            self.total_time = time.time() - self.time_start
            
            # Calculate accuracy
            count = 0
            for i, c in enumerate(self.word):
                try:
                    if self.input_text[i] == c:
                        count += 1
                except IndexError:
                    pass
            
            self.accuracy = count / len(self.word) * 100 if self.word else 0
            
            # Calculate words per minute
            self.wpm = len(self.input_text) * 60 / (5 * self.total_time) if self.total_time > 0 else 0
            
            self.end = True
            self.results = f'Time: {round(self.total_time)} secs Accuracy: {round(self.accuracy)}% Wpm: {round(self.wpm)}'
            
            # Draw icon image
            self.time_img = pygame.image.load('icon.png')
            self.time_img = pygame.transform.scale(self.time_img, (150, 150))
            self.screen.blit(self.time_img, (self.w / 2 - 75, self.h - 140))
            self.draw_text("Reset", self.h - 70, 26, (100, 100, 100))
            print(self.results)
            pygame.display.update()

    def run(self):
        self.reset_game()
        self.running = True
        clock = pygame.time.Clock()

        while self.running:
            self.screen.fill((0, 0, 0), (50, 250, 650, 50))
            pygame.draw.rect(self.screen, self.HEAD_C, (50, 250, 650, 50), 2)
            # Update the text of user input
            self.draw_text(self.input_text, 274, 26, (250, 250, 250))

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    # Position of input box
                    if 50 <= x <= 650 and 250 <= y <= 300:
                        self.active = True
                        self.input_text = ''
                        self.time_start = time.time()
                    # Position of reset box
                    if 310 <= x <= 510 and 390 <= y and self.end:
                        self.reset_game()

                elif event.type == pygame.KEYDOWN:
                    if self.active and not self.end:
                        if event.key == pygame.K_RETURN:
                            self.show_results()
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:-1]
                        else:
                            try:
                                self.input_text += event.unicode
                            except Exception:
                                pass
            
            pygame.display.update()
            clock.tick(60)

    def reset_game(self):
        self.screen.blit(self.open_img, (0, 0))
        pygame.display.update()
        time.sleep(1)
        self.reset = False
        self.end = False
        self.input_text = ''
        self.word = ''
        self.time_start = 0
        self.total_time = 0
        self.wpm = 0
        # Get random sentence 
        self.word = self.get_sentence()
        if not self.word:
            self.reset_game()

        self.screen.fill((0, 0, 0))
        self.screen.blit(self.bg, (0, 0))
        msg = "Typing Speed Test"
        self.draw_text(msg, 80, 80, self.HEAD_C)
        # Draw the rectangle for input box
        pygame.draw.rect(self.screen, (255, 192, 25), (50, 250, 650, 50), 2)
        # Draw the sentence string
        self.draw_text(self.word, 200, 28, self.TEXT_C)
        pygame.display.update()

if __name__ == "__main__":
    Game().run()
