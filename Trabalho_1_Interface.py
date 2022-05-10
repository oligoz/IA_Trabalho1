import pygame
from colour import Color

pygame.init()
font = pygame.font.SysFont(pygame.font.get_fonts()[0], 30)

WHITE = (255, 255, 255)
LIGHT = (244, 236, 195)
BROWN = (123, 100, 25)
BLUE = (82, 185, 240)
GRAY = (125, 125, 125)
GREEN = (94, 150, 70)
PINK = (193, 95, 190)
RED = (200, 0, 0)
PURPLE = (44, 7, 53)
BLACK = (0, 0, 0)
GRADIENT1 = Color("red")
GRADIENT2 = Color("green")

SPEED = 40

BORDER_BOTTOM = 160

class Interface:
    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h+BORDER_BOTTOM
        self.blockW = w/300
        self.blockH = h/82

        #init display
        self.display= pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Trabalho 1')
        self.clock = pygame.time.Clock()
        #self.reset()
    
    def add_map(self, map):
        self.map = map
    
    def add_percorreu(self, percorreu):
        self.percorreu = percorreu
    
    def add_andou(self, path):
        self.andou = path
    
    def update(self,percorreu, path, step, custos):
        self.add_percorreu(percorreu)
        self.add_andou(path)
        self._update_ui(step, custos)
        self.clock.tick(SPEED)
    
    def _update_ui(self, step, custos):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        self.display.fill(WHITE)
        
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                if self.percorreu[i][j] != 0:
                    pygame.draw.rect(self.display, RED, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                else:
                    #print(i,len(self.map),j,len(self.map[i]))
                    terrain = self.map[i][j]
                    if terrain == ".":
                        pygame.draw.rect(self.display, LIGHT, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                    elif terrain == "R":
                        pygame.draw.rect(self.display, BROWN, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                    elif terrain == "F":
                        pygame.draw.rect(self.display, GREEN, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                    elif terrain == "A":
                        pygame.draw.rect(self.display, BLUE, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                    elif terrain == "M":
                        pygame.draw.rect(self.display, GRAY, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                    else:
                        pygame.draw.rect(self.display, PINK, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
        for ponto in self.andou:
            pygame.draw.rect(self.display, PURPLE, pygame.Rect(ponto[1]*self.blockW, ponto[0]*self.blockH, self.blockW, self.blockH))
        text = font.render('Etapa: ' + str(step+1), True, BLACK)
        self.display.blit(text, [0, 0])
        s = "CUSTOS\n"
        for i in range(31):
            if i != 0 and i%8 == 0:
                s += "\n"
            if i < len(custos):
                custo = custos[i]
                s += "Etapa "+ str(i+1).zfill(2)+": "+ str(int(custo)).zfill(3)+"  "
            else:
                s += "Etapa "+ str(i+1).zfill(2)+": 000  "
        s = s.split("\n")
        linhas = []
        for linha in s:
            linhas.append(font.render(linha, True, BLACK))
        for i in range(len(linhas)):
            self.display.blit(linhas[i], [0, self.h-BORDER_BOTTOM+i*30])
        pygame.display.flip()
    
    def finish(self, path):
        #print(path)
        self.add_andou(path)
        count = 0
        for etapa in self.andou:
            count += len(etapa)
        for i in range(count):
            self._update_finish(self.andou,count)
            self.clock.tick(SPEED)
    
    def _update_finish(self, path, steps):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        colors = list(GRADIENT1.range_to(GRADIENT2,steps))
        self.display.fill(WHITE)
        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                terrain = self.map[i][j]
                if terrain == ".":
                    pygame.draw.rect(self.display, LIGHT, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                elif terrain == "R":
                    pygame.draw.rect(self.display, BROWN, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                elif terrain == "F":
                    pygame.draw.rect(self.display, GREEN, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                elif terrain == "A":
                    pygame.draw.rect(self.display, BLUE, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                elif terrain == "M":
                    pygame.draw.rect(self.display, GRAY, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
                else:
                    pygame.draw.rect(self.display, PINK, pygame.Rect(j*self.blockW, i*self.blockH, self.blockW, self.blockH))
        count = 0
        for etapa in path:
            for ponto in etapa:
                
                pygame.draw.rect(self.display, (Color(colors[count]).red*255,Color(colors[count]).green*255,Color(colors[count]).blue*255), pygame.Rect(ponto[1]*self.blockW, ponto[0]*self.blockH, self.blockW, self.blockH))
                count += 1
        pygame.display.flip()
