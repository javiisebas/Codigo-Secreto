import contextlib
with contextlib.redirect_stdout(None):
    import pygame
    from pygame.locals import *

import time
import numpy as np




def cuadroTexto(win,tam,color,pos,tamRect,text,colorText,posText):
        fontPal = pygame.font.SysFont('calibri', tam)
        pygame.draw.rect(win,color,pygame.Rect(pos,tamRect))

        textPal = fontPal.render(text, True, colorText)
        textRectPal = textPal.get_rect(center=(posText))
        win.blit(textPal, textRectPal)



class malla(object):
    def __init__(self, res):

        self.xRes = res[0]
        self.yRes = 9 * res[1]//10
        self.x = self.xRes//5
        self.y = self.yRes//5
        self.velx = self.xRes//5
        self.vely = self.yRes//5

    def draw(self,win):

        while self.x <= self.xRes:

            pygame.draw.line(win,(0,0,0),(self.x,0),(self.x, self.yRes))
            pygame.draw.line(win,(0,0,0),(0,self.y),(self.xRes, self.y))

            self.x += self.velx
            self.y += self.vely

        self.x = self.xRes//5
        self.y = self.yRes//5



class palabras(object):
    def __init__(self, res):

        self.xRes = res[0]
        self.yRes = 9 * res[1]//10
        self.x = self.xRes//10
        self.y = self.yRes//10
        self.velx = self.xRes//5
        self.vely = self.yRes//5
        self.cont = 0

    def draw(self,win,Victoria,original_matrix,palabras_juego):

        self.muertePal = np.where(original_matrix == 4)
        font = pygame.font.SysFont('calibri', 40)

        while self.x < self.xRes:
            while self.y < self.yRes: 

                if self.cont == (5 * self.muertePal[0][0] 
                                 + self.muertePal[1][0]) and Victoria.verPalabras == True:
                    self.color = (245,222,179)
                else:
                    self.color = (0,0,0)

                text = font.render(palabras_juego[self.cont], True, self.color)
                textRect = text.get_rect()
                textRect.center = (self.x,self.y)
                win.blit(text, textRect)

                self.y += self.vely
                self.cont += 1

            self.y = self.yRes//10
            self.x += self.velx

        self.x = self.xRes//10
        self.cont = 0



class ColoresMatriz(object):
    def __init__(self, res):

        self.xRes = res[0]
        self.yRes = 9 * res[1]//10
        self.velx = self.xRes//5
        self.vely = self.yRes//5
        self.matriz = np.zeros([5,5])
        self.x = 0
        self.y = 0
        self.paso = 1
        self.color = (255,239,219)

    def draw(self,win,Muerto):

        while self.x < 5:
            while self.y < 5:

                if self.matriz[self.x,self.y] == 1:
                    self.color = (153,163,164)
                elif self.matriz[self.x,self.y] == 2:
                    self.color = (220,20,60)
                elif self.matriz[self.x,self.y] == 3:
                    self.color = (0,178,238)
                elif self.matriz[self.x,self.y] == 4:
                    self.color = (0,0,0)
                    Muerto.vivo = False
                else:
                    self.color = (245,222,179) 

                pygame.draw.rect(win,self.color,pygame.Rect((self.x * self.velx,self.y * self.vely),(self.velx, self.vely)))

                self.y += self.paso

            self.y = 0
            self.x += self.paso

        self.x = 0

    def posicion(self,win,Muerto,original_matrix):

        if pygame.mouse.get_pressed()[0]:

            self.ratonX = pygame.mouse.get_pos()[0]
            self.ratonY = pygame.mouse.get_pos()[1]
            self.posx = self.ratonX // self.velx
            self.posy = self.ratonY // self.vely
            self.matriz[self.posx,self.posy] = original_matrix[self.posx,self.posy]

        self.draw(win,Muerto)



class muerto(object):
    def __init__(self, res):

        self.vivo = True
        self.res = res
        self.xRes = res[0]
        self.yRes = 9 * res[1]//10
        self.xRes1 = self.xRes//2
        self.yRes1 = 2*self.yRes//5
        self.yRes2 = 2*self.yRes//3

    def draw(self,win,Victoria,Matriz,original_matrix):

        if self.vivo == False and Victoria.verPalabras == False:

            cuadroTexto(win,100,(153,163,164),(0,0),self.res
                ,'GAME OVER',(0,0,0),(self.xRes1,self.yRes1))
            cuadroTexto(win,60,(153,163,164),(0,self.yRes//2),(self.xRes, self.yRes//2)
                ,'PALABRAS',(0,0,0),(self.xRes1,self.yRes2))

            Matriz.matriz = original_matrix

            self.ratonX = pygame.mouse.get_pos()[0]
            self.ratonY = pygame.mouse.get_pos()[1]

            if self.ratonX > self.xRes1-115 and self.ratonX < self.xRes1+115:
                if self.ratonY > self.yRes2-25 and self.ratonY < self.yRes2+25:
                    cuadroTexto(win,60,(153,163,164),(0,self.yRes//2),(self.xRes, self.yRes//2)
                        ,'PALABRAS',(245,222,179),(self.xRes1,self.yRes2))

                    if pygame.mouse.get_pressed()[0]:
                        Victoria.verPalabras = True



class victoria(object):
    def __init__(self, res):

        self.fin = False
        self.res = res
        self.xRes = res[0]
        self.yRes = 9 * res[1]//10
        self.xRes1 = self.xRes//2
        self.yRes1 = 2*self.yRes//5
        self.yRes2 = 2*self.yRes//3
        self.verPalabras = False

    def draw(self,win,Matriz,original_matrix,Muerto):

        if Muerto.vivo:
            self.unique, self.counts = np.unique(Matriz.matriz,return_counts=True)
            self.valores = dict(zip(self.unique,self.counts))

        if not(self.fin):
            if 2 in self.valores.keys():
                if self.valores[2] == 9:
                    self.fin = True
                    self.colorFin = (220,20,60)

            if 3 in self.valores.keys():
                if self.valores[3] == 8:
                    self.fin = True
                    self.colorFin = (0,178,238)

        if self.fin == True and self.verPalabras == False: 

            cuadroTexto(win,100,self.colorFin,(0,0),self.res
                ,'GANADOR',(0,0,0),(self.xRes1,self.yRes1))
            cuadroTexto(win,60,self.colorFin,(0,self.yRes//2),(self.xRes, self.yRes//2)
                ,'PALABRAS',(0,0,0),(self.xRes1,self.yRes2))

            Matriz.matriz = original_matrix

            self.ratonX = pygame.mouse.get_pos()[0]
            self.ratonY = pygame.mouse.get_pos()[1]

            if self.ratonX > self.xRes1-115 and self.ratonX < self.xRes1+115:
                if self.ratonY > self.yRes2-25 and self.ratonY < self.yRes2+25:
                    cuadroTexto(win,60,self.colorFin,(0,self.yRes//2),(self.xRes, self.yRes//2)
                        ,'PALABRAS',(245,222,179),(self.xRes1,self.yRes2))

                    if pygame.mouse.get_pressed()[0]:
                        self.verPalabras = True




class salir(object):
    def __init__(self, res):
        self.xRes = res[0]
        self.yRes = res[1]
        self.xRes1 = self.xRes//2
        self.yRes1 = 19*self.yRes//20
        self.run = True
        self.decision = True

    def draw(self, win):
        cuadroTexto(win,50,(0,0,0),(0,self.yRes*0.895),(self.xRes1,0.15*self.yRes)
                ,'NUEVO JUEGO',(245,222,179),(self.xRes1//2,self.yRes1))
        cuadroTexto(win,50,(0,0,0),(self.xRes1,self.yRes*0.895),(self.xRes1,0.15*self.yRes)
                ,'SALIR',(245,222,179),(3*self.xRes1//2,self.yRes1))

        self.ratonX = pygame.mouse.get_pos()[0]
        self.ratonY = pygame.mouse.get_pos()[1]

        if self.ratonY > 0.895*self.yRes and self.ratonY < self.yRes:
            if self.ratonX < self.xRes1:

                cuadroTexto(win,50,(153,163,164),(0,self.yRes*0.895),(self.xRes1,0.15*self.yRes)
                    ,'NUEVO JUEGO',(0,0,0),(self.xRes1//2,self.yRes1))
                if pygame.mouse.get_pressed()[0]:
                    self.run = False


        if self.ratonY > 0.895*self.yRes and self.ratonY < self.yRes:
            if self.ratonX > self.xRes1:

                cuadroTexto(win,50,(153,163,164),(self.xRes1,self.yRes*0.895),(self.xRes1,0.15*self.yRes)
                    ,'SALIR',(0,0,0),(3*self.xRes1//2,self.yRes1))
                if pygame.mouse.get_pressed()[0]:
                    self.run = False
                    self.decision = False

        pygame.draw.rect(win,(0,0,0),pygame.Rect((0,0.895*self.yRes),(self.xRes,0.002*self.yRes)))
