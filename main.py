import pygame

pygame.init()

display = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Pong Simples")
clock = pygame.time.Clock()


player1 = pygame.Rect(10, 300, 20, 140)
player1_speed = 0

player2 = pygame.Rect(1250, 300, 20, 140)

ball = pygame.Rect(632, 352, 16, 16)
ball_speed_x = 4 
ball_speed_y = 4 


loop = True
while(loop):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            
        # Quando uma tecla é PRESSIONADA
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1_speed = -5 # Velocidade para cima
            elif event.key == pygame.K_s:
                player1_speed = 5  # Velocidade para baixo
                
        # Quando uma tecla é SOLTA
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1_speed = 0 # Para o movimento

    
    # Movimento do Jogador 1
    player1.y += player1_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= 720:
        player1.bottom = 720
        
    # Movimento da Bola
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ricochete da Bola (paredes)
    if ball.top <= 0 or ball.bottom >= 720:
        ball_speed_y *= -1
    
    # Ponto (resetar bola)
    if ball.left <= 0 or ball.right >= 1280:
        ball.center = (640, 360)
        ball_speed_x *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1
        hit = pygame.mixer.Sound("assets/pong.wav")
        hit.play()
        
   
    if player2.centery < ball.centery:
        player2.y += 3
    if player2.centery > ball.centery:
        player2.y -= 3
        
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= 720:
        player2.bottom = 720

    
    display.fill((10, 10, 10)) 
    pygame.draw.rect(display, (255, 0, 255), player1)
    pygame.draw.rect(display, (0, 255, 0), player2)
    pygame.draw.ellipse(display, (255, 255, 255), ball) 
    pygame.draw.aaline(display, (200,200,200), (640,0), (640,720)) # Linha no meio

    pygame.display.flip()
    clock.tick(60) # Limita o jogo a 60 FPS

pygame.quit()