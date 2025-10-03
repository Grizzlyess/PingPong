import pygame

# --- INICIALIZAÇÃO ---
pygame.init()
pygame.font.init()

# --- CONFIGURAÇÕES DA TELA ---
display = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Pong Simples")
clock = pygame.time.Clock()

# --- OBJETOS DO JOGO ---
player1 = pygame.Rect(10, 300, 20, 140)
player1_score = 0
player1_speed = 0

player2 = pygame.Rect(1250, 300, 20, 140)
player2_score = 0
player2_speed = 0

ball = pygame.Rect(632, 352, 16, 16)
ball_speed_x = 4
ball_speed_y = 4

# --- FONTES E SOM (CARREGADOS UMA VEZ) ---
fonte = pygame.font.Font(None, 50)
try:
    # Tenta carregar o som. Se o arquivo não existir, o jogo não vai quebrar.
    hit_sound = pygame.mixer.Sound("assets/pong.wav")
except pygame.error:
    hit_sound = None
    print("Aviso: Arquivo de som 'assets/pong.wav' não encontrado.")

win = False
cena = "menu"
jogando = True # Esta variável não é mais necessária para o controle de cena, mas mantive como pediu.
loop = True

while loop:
    if cena == "jogo":
        # --- PROCESSAMENTO DE EVENTOS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
                
            # Quando uma tecla é PRESSIONADA
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_speed = -5  # Velocidade para cima
                elif event.key == pygame.K_s:
                    player1_speed = 5   # Velocidade para baixo
                elif event.key == pygame.K_UP:   # Seta para cima
                    player2_speed = -5 # Velocidade para cima
                elif event.key == pygame.K_DOWN: # Seta para baixo
                    player2_speed = 5
                    
            # Quando uma tecla é SOLTA
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    player1_speed = 0  # Para o movimento
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    player2_speed = 0

        if player1_score >=3 :
            win = True
            cena = "gameover" # MUDA A CENA PARA A TELA DE VITÓRIA
        if player2_score >=3 :
            win = False # Define que o Player 2 venceu
            cena = "gameover" 
        
        
        # Movimento do Jogador 1 e colisão com as paredes
        player1.y += player1_speed
        if player1.top <= 0:
            player1.top = 0
        if player1.bottom >= 720:
            player1.bottom = 720
            
        # Movimento da Bola
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        
        # Ricochete da Bola (paredes de cima e de baixo)
        if ball.top <= 0 or ball.bottom >= 720:
            ball_speed_y *= -1
        
        # Verificação de Ponto (bola sai pelas laterais)
        if ball.left <= 0:  # Bola passou pelo Player 1
            player2_score += 1
            ball.center = (640, 360)
            ball_speed_x *= -1  # Inicia na direção oposta
            
        if ball.right >= 1280:  # Bola passou pelo Player 2
            player1_score += 1
            ball.center = (640, 360)
            ball_speed_x *= -1  # Inicia na direção oposta

        # Colisão da bola com os jogadores
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_speed_x *= -1
            if hit_sound:
                hit_sound.play()
            
        # Movimento do Jogador 2
        player2.y += player2_speed
            
        # Colisão do Jogador 2 com as paredes
        if player2.top <= 0:
            player2.top = 0
        if player2.bottom >= 720:
            player2.bottom = 720

        # --- SEÇÃO DE DESENHO ---
        display.fill((10, 10, 10))
        pygame.draw.rect(display, (255, 0, 255), player1)
        pygame.draw.rect(display, (0, 255, 0), player2)
        pygame.draw.ellipse(display, (255, 255, 255), ball)
        pygame.draw.aaline(display, (200, 200, 200), (640, 0), (640, 720))  # Linha no meio
        
        # Renderiza e desenha os placares a cada frame
        placar_player1 = fonte.render(str(player1_score), True, "white")
        display.blit(placar_player1, (580 - placar_player1.get_width(), 50))
        
        placar_player2 = fonte.render(str(player2_score), True, "white")
        display.blit(placar_player2, (680, 50))
    
    elif cena == "gameover":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = "menu"
                    player1_score=0
                    player2_score=0
                    
                
        display.fill((10, 10, 10))
        if win:
            text_win = fonte.render("VICTORY Player 1 !!!", True, (255,255,0))
        else: 
            text_win = fonte.render("VICTORY Player 2 !!!", True, (255,255,0))
        display.blit(text_win, [500,360])
        
    elif cena == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    cena = "jogo"
                    player1.y = 0
                    player2.y = 0
                    ball.x = 632
                    ball.y = 352
                    
        display.fill((10, 10, 10))
        title = fonte.render("Ping Pong", True, (255,255,0))
        text = fonte.render("Press start to play.", True, (255,255,0)) # "start" deve ser "Enter"
        display.blit(title, [550,310])
        display.blit(text, [490,410])
        

    # --- ATUALIZAÇÃO DA TELA ---
    pygame.display.flip()
    clock.tick(60)  # Limita o jogo a 60 FPS

# --- FINALIZAÇÃO ---
pygame.quit()