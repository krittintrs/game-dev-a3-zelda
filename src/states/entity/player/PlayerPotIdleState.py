from src.states.entity.EntityIdleState import EntityIdleState
import pygame

class PlayerPotIdleState(EntityIdleState):
    def __init__(self, player):
        super(PlayerPotIdleState, self).__init__(player)
        self.player = player

    def Enter(self, params):
        self.player.offset_x = 0
        self.player.offset_y = 15
        
        self.player.ChangeAnimation('pot_walk_' + self.player.direction)

    def Exit(self):
        pass

    def update(self, dt, events):
        pressedKeys = pygame.key.get_pressed()
        if pressedKeys[pygame.K_LEFT] or pressedKeys [pygame.K_RIGHT] or pressedKeys [pygame.K_UP] or pressedKeys [pygame.K_DOWN]:
            self.entity.ChangeState('pot_walk')

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    # TODO - Throw Pot
                    self.player.ChangeState('idle')