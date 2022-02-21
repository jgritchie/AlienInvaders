import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        rounded_score = round(self.stats.score, -1)
        score = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score, True, self.text_color, self.settings.background_color)

        # display score on top right of screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highscore_image, self.highscore_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_highscore(self):
        rounded_score = round(self.stats.high_score, -1)
        score = "{:,}".format(rounded_score)
        self.highscore_image = self.font.render(score, True, self.text_color, self.settings.background_color)

        # display score on top right of screen
        self.highscore_rect = self.score_image.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.score_rect.top

    def check_highscore(self):
        if self.stats.high_score < self.stats.score:
            self.stats.high_score = self.stats.score
            self.prep_highscore()

    def prep_level(self):
        level = str(self.stats.level)
        self.level_image = self.font.render(level, True, self.text_color, self.settings.background_color)

        # display level on top right of screen
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

