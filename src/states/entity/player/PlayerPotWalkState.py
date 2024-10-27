from src.constants import *
from src.states.entity.EntityWalkState import EntityWalkState
import pygame

class PlayerPotWalkState(EntityWalkState):
    def __init__(self, player, dungeon):
        super(PlayerPotWalkState, self).__init__(player, dungeon)
        self.player = player
        self.dungeon = dungeon

    def Exit(self):
        pass

    def Enter(self, params):
        print('<<<<<<< ENTER POT WALK STATE >>>>>>>>>')
        self.player.ChangeAnimation("pot_walk_"+self.player.direction)
        self.pot = params['pot']

    def update(self, dt, events):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_LEFT]:
            self.player.direction = 'left'
            self.player.ChangeAnimation("pot_walk_"+self.player.direction)
        elif pressedKeys[pygame.K_RIGHT]:
            self.player.direction = 'right'
            self.player.ChangeAnimation("pot_walk_"+self.player.direction)
        elif pressedKeys[pygame.K_DOWN]:
            self.player.direction = 'down'
            self.player.ChangeAnimation("pot_walk_"+self.player.direction)
        elif pressedKeys[pygame.K_UP]:
            self.player.direction = 'up'
            self.player.ChangeAnimation("pot_walk_"+self.player.direction)
        else:
            self.player.ChangeState('pot_idle', {'pot': self.pot})  

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.pot.Throw(self.player.direction)
                    self.player.ChangeState('idle')
                
        # move and bump to the wall check
        super().update(dt, events)

        #temporal move to the wall (bumping effect)
        if self.bumped:
            if self.entity.direction == 'left':
                self.entity.x = self.entity.x - PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.y + 12
                        self.dungeon.BeginShifting(-WIDTH, 0)

                self.entity.x = self.entity.x + PLAYER_WALK_SPEED * dt

            elif self.entity.direction == 'right':
                self.entity.x = self.entity.x + PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.y + 12
                        self.dungeon.BeginShifting(WIDTH, 0)

                self.entity.x = self.entity.x - PLAYER_WALK_SPEED * dt

            elif self.entity.direction == 'up':
                self.entity.y = self.entity.y - PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.x + 24
                        self.dungeon.BeginShifting(0,  -HEIGHT)

                self.entity.y = self.entity.y + PLAYER_WALK_SPEED * dt

            else:
                self.entity.y = self.entity.y + PLAYER_WALK_SPEED * dt

                for doorway in self.dungeon.current_room.doorways:
                    if self.entity.Collides(doorway) and doorway.open:
                        self.entity.y = doorway.x + 24
                        self.dungeon.BeginShifting(0,  HEIGHT)

                self.entity.y = self.entity.y - PLAYER_WALK_SPEED * dt
        # If not bumped, move the pot along with player
        else:
            self.pot.x = self.player.x - POT_OFFSET_X
            self.pot.y = self.player.y - POT_OFFSET_Y