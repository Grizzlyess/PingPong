# 🏓 Ping Pong - Clássico em Pygame

Uma recriação do clássico jogo de arcade Ping Pong, desenvolvida inteiramente em Python utilizando a biblioteca **Pygame**. Este projeto prático explora os fundamentos do desenvolvimento de jogos 2D, como a estruturação do *game loop*, detecção de colisões, renderização na tela e manipulação de estados do jogo.

## 📂 Estrutura do Projeto

O repositório mantém uma arquitetura simples e direta, separando a lógica dos recursos visuais:

*   **`/assets`**: Diretório responsável por armazenar os recursos do jogo, como fontes utilizadas na interface ou possíveis efeitos sonoros e visuais.
*   **`main.py`**: O arquivo principal que contém o núcleo do jogo. É aqui que o Pygame é inicializado, as entidades (bola e raquetes) são desenhadas e a física de movimentação é calculada quadro a quadro.

## ✨ Funcionalidades e Mecânicas

A partir do histórico de desenvolvimento, as seguintes implementações se destacam:
*   **Mecânica Base:** Controle fluido das raquetes e física de rebatida da bola nos limites da tela.
*   **Sistema de Placar:** Pontuação dinâmica renderizada na tela, atualizada sempre que um jogador pontua.
*   **Gerenciamento de Estado (Reset):** Lógica estruturada para reiniciar o posicionamento da bola e das raquetes entre rodadas de forma limpa, sem interromper o loop principal.

## 🚀 Como Jogar

Para rodar o jogo na sua máquina, é necessário ter o ambiente Python configurado com a biblioteca do Pygame.

### Pré-requisitos
*   Python 3.x instalado.
*   Gerenciador de pacotes `pip`.
