import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
	
	#инициализирует pygame, settings и объект экрана
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	
	#созание кнопки Play
	play_button = Button(ai_settings, screen, 'Play')
	
	#создание экземпляра для хранения статистики и выводв счета
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings, screen, stats)
	
	#создание корабля, группы пуль и группы пришельцев
	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	
	#создание флота пришельцев
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	#Запуск основного цикла игры
	while True:
		gf.check_events(ai_settings, screen, stats, play_button, ship, bullets, aliens, sb)
		if stats.game_active:
			ship.update()
			gf.update_bullets(aliens, bullets, ai_settings, screen, ship, stats, sb)
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb)
		
run_game()
