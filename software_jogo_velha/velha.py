import pygame
import sys

#o a cada clique muda a letra de X para O 

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura = 300
altura = 300
tamanho_celula = 100
cor_fundo = (255, 255, 255)
cor_linhas = (0, 0, 0)

# Configurações dos jogadores
jogador1 = 'X'
jogador2 = 'O'
jogador_atual = jogador1

# Criação da janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo do Novo')

# Criação do tabuleiro
tabuleiro = [[None, None, None],
             [None, None, None],
             [None, None, None]]


def desenhar_tabuleiro():
    janela.fill(cor_fundo)

    # Desenha as linhas verticais
    pygame.draw.line(janela, (0, 0, 255), (tamanho_celula, 0), (tamanho_celula, altura), 19)
    pygame.draw.line(janela, (165, 42, 42), (tamanho_celula * 2, 0), (tamanho_celula * 2, altura), 19)

    # Desenha as linhas horizontais
    pygame.draw.line(janela, (255, 255, 0), (0, tamanho_celula), (largura, tamanho_celula), 17)
    pygame.draw.line(janela, (0, 255, 0), (0, tamanho_celula * 2), (largura, tamanho_celula * 2), 17)

    # Desenha os símbolos no tabuleiro
    for linha in range(3):
        for coluna in range(3):
            simbolo = tabuleiro[linha][coluna]
            if simbolo:
                pos_x = coluna * tamanho_celula + tamanho_celula // 2
                pos_y = linha * tamanho_celula + tamanho_celula // 2
                fonte = pygame.font.SysFont(None, 80)
                texto = fonte.render(simbolo, True, cor_linhas)
                texto_rect = texto.get_rect(center=(pos_x, pos_y))
                janela.blit(texto, texto_rect)

    pygame.display.flip()


def verificar_vitoria():
    # Verifica as linhas
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != None:
            return True

    # Verifica as colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != None:
            return True

    # Verifica as diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != None:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != None:
        return True

    return False


def verificar_empate():
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] is None:
                return False
    return True


def reiniciar_jogo():
    global tabuleiro, jogador_atual
    tabuleiro = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]
    jogador_atual = jogador1


# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not verificar_vitoria() and not verificar_empate():
                pos_x, pos_y = pygame.mouse.get_pos()
                linha = pos_y // tamanho_celula
                coluna = pos_x // tamanho_celula

                if tabuleiro[linha][coluna] is None:
                    tabuleiro[linha][coluna] = jogador_atual
                    if jogador_atual == jogador1:
                        jogador_atual = jogador2
                    else:
                        jogador_atual = jogador1

    desenhar_tabuleiro()

    if verificar_vitoria():
        if jogador_atual == jogador1:
            vencedor = jogador2
        else:
            vencedor = jogador1
        fonte = pygame.font.SysFont(None, 60)
        texto = fonte.render(f"Jogador {vencedor} venceu!", True, (255, 165, 0))
        texto_rect = texto.get_rect(center=(largura // 2, altura // 2))
        janela.blit(texto, texto_rect)
        pygame.display.update()
        pygame.time.wait(1000)  # Aguarda 1 segundos
        reiniciar_jogo()

    elif verificar_empate():
        fonte = pygame.font.SysFont(None, 60)
        texto = fonte.render("Empate!", True, (255, 165, 0))
        texto_rect = texto.get_rect(center=(largura // 2, altura // 2))
        janela.blit(texto, texto_rect)
        pygame.display.update()
        pygame.time.wait(1000)  # Aguarda 1 segundos
        reiniciar_jogo()

    pygame.display.update()
