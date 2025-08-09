import pygame
import random

pygame.init()
# interface 
width = 600
height = 500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('CATCH THE FALLING BLOCKS')

# color 
white = (255,255,255)   
black = (0,0,0)
blue = (0,150,255)
red = (155,0,0)

# player in game
player_width = 80
player_height = 20
player_x = width//2 - player_width//2
player_y = height - player_height - 10
player_speed = 3 # speed for playing a game

#block
block_width = 30
block_height = 30
block_x = random.randint(0,width - block_width)
block_y = 0
block_speed = 3

#score and lives 
score = 0
lives = 3
font = pygame.font.SysFont(None,36)

clock = pygame.time.Clock() # frame 60 fps

# loop for game
running = True
game_over = False
while running:

    screen.fill(white)

    # quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if not game_over:
        # keys for controling        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_width:
            player_x += player_speed

        block_y += block_speed

        player_rect = pygame.draw.rect(screen,blue,(player_x,player_y,player_width,player_height))
        block_rect = pygame.draw.rect(screen,red,(block_x,block_y,block_width,block_height))

        # collision detection 
        if player_rect.colliderect(block_rect):
            score += 1
            block_y = 0
            block_x = random.randint(0,width - block_width)
        if block_y > height:
            block_y = 0
            block_x = random.randint(0,width - block_width)
            lives -= 1
            if lives == 0:
                game_over = True

        pygame.draw.rect(screen,blue,player_rect)
        pygame.draw.rect(screen,red,block_rect)

        score_text = font.render("Score: " + str(score), True, black)
        lives_text = font.render('Lives: '+ str(lives),True,black)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10,35))
    
    else:
        # Show Game Over
        over_text = font.render("GAME OVER", True, red)
        screen.blit(over_text, (width // 2 - 80, height // 2 - 20))

    pygame.display.update() # show new positions
    clock.tick(60)

pygame.quit()
