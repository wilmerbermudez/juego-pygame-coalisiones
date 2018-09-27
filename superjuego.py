import pygame
import random
Ancho=1200
Alto=600
verde=[0,255,0]
rojo=[255,0,0]
blanco=[255,255,255]
azul=[0,0,255]
negro=[0,0,0]
imagen=[150,150]
salu=100
bubu=0


class Bloques(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(azul)
        self.rect=self.image.get_rect()
        self.vel_x=0
        self.click=False


    def update(self):
        if self.click:
            self.rect.center=pygame.mouse.get_pos()
        self.rect.x+=self.vel_x

class Rival(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([80,50])
        self.image.fill(blanco)
        self.rect=self.image.get_rect()
        self.tmp=random.randrange(80)

    def update(self):
        self.tmp-=1

class Obstaculos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([40,100])
        self.image.fill(verde)
        self.rect=self.image.get_rect()
        self.vel_y=-4


    def update(self):
        if self.rect.bottom > 550:
            self.vel_y=-4
        if self.rect.y<50:
            self.vel_y=4
        self.rect.y+=self.vel_y

class Bala(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([10,15])
        self.image.fill(rojo)
        self.rect=self.image.get_rect()
        self.vel_y=9

    def update(self):
        self.rect.y+=self.vel_y
        '''
class Salud(pygame.sprite.Sprite):
    def __init__(self,sal,nob):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([sal,nob])
        self.image.fill(verde)
        self.rect=self.image.get_rect()

    def update(self):
        pass
        '''
if __name__ == '__main__':

    pygame.init()
    pantalla=pygame.display.set_mode([Ancho,Alto])

    #Creacion de los bloques
    bloques=pygame.sprite.Group()
    b1=Bloques(60,60)
    b1.rect.x=random.randrange(0,100)
    b1.rect.y=random.randrange(50,400)
    bloques.add(b1)

    obstaculos=pygame.sprite.Group()
    rivales=pygame.sprite.Group()
    for i in range(1,5):
        r=Rival()
        r.rect.x=i*200
        r.rect.y=500
        rivales.add(r)
        o=Obstaculos()
        o.rect.x=r.rect.right
        o.rect.y=random.randrange(100,500)
        obstaculos.add(o)

    balas=pygame.sprite.Group()
    '''
    salud=pygame.sprite.Group()
    s=Salud(100,15)
    s.rect.x=20
    s.rect.y=570
    salud.add(s)
    '''
    reloj=pygame.time.Clock()
    fin=False

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.rect.collidepoint(event.pos):
                    b1.click=True
            if event.type == pygame.MOUSEBUTTONUP:
                b1.click=False
                if b1.click==False:
                    b1.vel_x=+2

        for r in rivales:
            if r.tmp <0:
                b=Bala()
                b.rect.x=r.rect.x+(r.rect.width)/2
                b.rect.y=r.rect.y
                b.vel_y=-7
                balas.add(b)
                r.tmp=80

        for b in balas:
            col_j1=pygame.sprite.spritecollide(b,bloques,True)
            for r in col_j1:
                balas.remove(b)
            if b.rect.y<(50):
                balas.remove(b)
            bloques.add(b1)

        ls_col=pygame.sprite.spritecollide(b1,obstaculos,False)
        for b in ls_col:
            b1.rect.right=b.rect.left

        if b1.rect.right>1150:
            bloques.remove(b1)

        bloques.update()
        rivales.update()
        balas.update()
        #salud.update()
        obstaculos.update()
        pantalla.fill(negro)
        obstaculos.draw(pantalla)
        bloques.draw(pantalla)
        rivales.draw(pantalla)
        balas.draw(pantalla)
        #salud.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)
