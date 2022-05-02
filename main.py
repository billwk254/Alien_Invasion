import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    #initialize the game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Space Invasion")
    #Make the Play button
    play_button = Button(ai_settings,screen, "Play")
    #make a ship
    ship = Ship(ai_settings, screen)
    #make a group to store bullets in
    bullets = Group()
    #make a roup to store aliens in
    aliens = Group()
    #make an alien
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #create an instance to store game statistics and create a scorecard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    #start the main loop for the game
    while True:
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats,sb, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings,screen,stats,sb, ship,aliens,bullets,play_button)


run_game()





