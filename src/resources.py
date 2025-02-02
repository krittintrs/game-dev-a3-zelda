from enum import Enum
import pygame
from src.Util import SpriteManager, Animation
import src.Util as Util
from src.StateMachine import *

g_state_manager = StateMachine()

sprite_collection = SpriteManager().spriteCollection


gPlayer_animation_list = {
    "down": sprite_collection["character_walk_down"].animation,
    "right": sprite_collection["character_walk_right"].animation,
    "up": sprite_collection["character_walk_up"].animation,
    "left": sprite_collection["character_walk_left"].animation,
    "attack_down": sprite_collection["character_attack_down"].animation,
    "attack_right": sprite_collection["character_attack_right"].animation,
    "attack_up": sprite_collection["character_attack_up"].animation,
    "attack_left": sprite_collection["character_attack_left"].animation,
    "pot_lift_down": sprite_collection["character_pot_lift_down"].animation,
    "pot_lift_right": sprite_collection["character_pot_lift_right"].animation,
    "pot_lift_up": sprite_collection["character_pot_lift_up"].animation,
    "pot_lift_left": sprite_collection["character_pot_lift_left"].animation,
    "pot_walk_down": sprite_collection["character_pot_walk_down"].animation,
    "pot_walk_right": sprite_collection["character_pot_walk_right"].animation,
    "pot_walk_up": sprite_collection["character_pot_walk_up"].animation,
    "pot_walk_left": sprite_collection["character_pot_walk_left"].animation,
    "ghost_down": sprite_collection["ghost_walk_down"].animation,
    "ghost_right": sprite_collection["ghost_walk_right"].animation,
    "ghost_up": sprite_collection["ghost_walk_up"].animation,
    "ghost_left": sprite_collection["ghost_walk_left"].animation,
}

gSkeleton_animation_list = {
    "down": sprite_collection["skeleton_walk_down"].animation,
    "right": sprite_collection["skeleton_walk_right"].animation,
    "up": sprite_collection["skeleton_walk_up"].animation,
    "left": sprite_collection["skeleton_walk_left"].animation,
}

gHeart_image_list = [sprite_collection["heart_0"].image,sprite_collection["heart_2"].image,
                    sprite_collection["heart_4"].image]

gRoom_image_list = Util.GenerateTiles("./graphics/tilesheet.png", 16, 16)
gDoor_image_list = Util.GenerateTiles("./graphics/tilesheet.png", 16, 16, colorkey=(13, 7, 17, 255))
gSwitch_image_list = Util.GenerateTiles("./graphics/switches.png", 16, 18)
gPot_image_list = Util.GenerateTiles("./graphics/tilesheet.png", 16, 16, colorkey=(0, 0, 0))

gSounds = {
    'music': pygame.mixer.Sound('sounds/music.mp3'),
    'sword':  pygame.mixer.Sound('sounds/sword.wav'),
    'hit_enemy':  pygame.mixer.Sound('sounds/hit_enemy.wav'),
    'hit_enemy_2':  pygame.mixer.Sound('sounds/hit_enemy_2.wav'),
    'hit_player':  pygame.mixer.Sound('sounds/hit_player.wav'),
    'door':  pygame.mixer.Sound('sounds/door.wav'),
    'pot_bomb': pygame.mixer.Sound('sounds/pot_bomb.wav'),
    'pot_pickup': pygame.mixer.Sound('sounds/pot_pickup.wav'),
    'ghost_eat': pygame.mixer.Sound('sounds/ghost_eat.wav'),
    'powerup_ghost': pygame.mixer.Sound('sounds/powerup_ghost.wav'),
    'powerup_damage': pygame.mixer.Sound('sounds/powerup_damage.wav'),
    'powerup_heal': pygame.mixer.Sound('sounds/powerup_heal.wav'),
    'powerup_deactive': pygame.mixer.Sound('sounds/powerup_deactive.wav')
}

gFonts = {
    'small': pygame.font.Font('fonts/font.ttf', 24),
    'medium': pygame.font.Font('fonts/font.ttf', 48),
    'large': pygame.font.Font('fonts/font.ttf', 96),
    'zelda_small': pygame.font.Font('fonts/zelda.otf', 96),
    'zelda': pygame.font.Font('fonts/zelda.otf', 192),
    'gothic_medium': pygame.font.Font('fonts/GothicPixels.ttf', 48),
    'gothic_large': pygame.font.Font('fonts/GothicPixels.ttf', 96),
}

class PowerUpType(Enum):
    GHOST = 0
    DAMAGE = 1
    HEAL = 2

powerups_image_list = [
    sprite_collection['powerup_ghost'].image,
    sprite_collection['powerup_damage'].image,
    sprite_collection['powerup_heal'].image
]