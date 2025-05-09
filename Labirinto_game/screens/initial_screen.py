import pygame
import sys
import math
from constants import LARGURA_TELA, ALTURA_TELA, FPS, AZUL_CLARO, background_img
from utils.drawing import resize, desenhar_texto_textura

def tela_inicial(tela):
    """Tela inicial do jogo com texto animado."""
    clock = pygame.time.Clock()
    rodando = True

    # Texto e fonte
    mensagem = "A FURIA DO MINOTAURO"
    mensagem2 = "Aperte qualquer tecla para continuar"
    fonte = pygame.font.Font("Labirinto_game/assets/fonts/Odyssey.otf", resize(140, eh_X=True))
    fonte2 = pygame.font.Font("Labirinto_game/assets/fonts/Odyssey.otf", resize(50, eh_X=True))

    # Posição base (fixa) e parâmetros de movimento
    base_x = LARGURA_TELA // 2
    base_y = ALTURA_TELA // 2 - resize(20)
    amplitude = resize(20)   # até onde o texto "sobe e desce"
    frequencia = 0.4   # quantas "oscilações" por segundo

    tempo_acumulado = 0.0
    texture_image = pygame.image.load("Labirinto_game/assets/images/marmore2.jpg").convert_alpha()
    while rodando:
        dt = clock.tick(FPS)  # tempo em ms desde o último frame
        tempo_acumulado += dt / 1000.0  # converte para segundos

        # Trata eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Ao apertar qualquer tecla ou clicar, sai desta tela
                rodando = False

        # Desenha fundo
        if background_img:
            tela.blit(background_img, (0, 0))
        else:
            tela.fill(AZUL_CLARO)

        # Cálculo do offset em Y usando sin
        offset_y = amplitude * math.sin(2 * math.pi * frequencia * tempo_acumulado)
        # Posição final do texto
        pos_x = base_x
        pos_y = base_y + offset_y

        # Renderiza e desenha
        
        
        # text_surface = fonte.render(mensagem, True, AZUL_CLARO)
        
        text_surface = desenhar_texto_textura(mensagem, fonte, texture_image)
        text_surface2 = desenhar_texto_textura(mensagem2, fonte2, texture_image)
        text_rect = text_surface.get_rect(center=(pos_x, pos_y))
        text_rect2 = text_surface2.get_rect(center=(pos_x, pos_y + resize(80)))
        tela.blit(text_surface, text_rect)
        tela.blit(text_surface2, text_rect2)

        pygame.display.update()