import pygame
from pygame import *
import math
import sys

#house, zombie <--,  zombie -->,   baloon <--,  baloon -->,  wheelchair <--,   wheelchair -->
levels = [
            [[0,1,0,0,0,0,0],[0,1,1,0,0,0,0],[0,1,1,0,0,1,0],[0,2,1,0,0,1,1],[0,2,2,1,0,1,0]],
            [[1,1,2,0,0,0,0],[0,2,0,0,0,0,1],[0,2,1,0,0,1,1],[0,2,2,0,0,2,2],[0,2,3,1,0,2,1]],            
            [[0,2,2,0,0,1,0],[0,2,1,0,1,0,1],[1,3,1,1,0,2,1],[0,2,2,0,0,2,2],[0,3,3,1,1,2,2]],
            [[0,2,2,1,0,1,0],[0,0,3,2,1,0,1],[0,3,1,1,0,2,1],[1,2,2,1,1,1,1],[0,3,1,2,2,2,2]],
            [[0,2,4,1,0,4,0],[0,4,4,3,1,1,1],[0,3,9,2,2,8,1],[1,2,3,13,1,4,1],[0,3,3,3,3,3,3]],
            [[0,18,0,0,0,0,0],[0,9,3,2,1,4,1],[0,7,7,9,0,2,1],[1,2,2,12,1,18,1],[0,11,1,2,13,2,19]],
            [[0,9,9,9,9,9,0],[0,14,3,14,1,0,1],[0,0,0,10,10,2,1],[1,10,2,10,10,19,1],[0,13,12,20,2,2,2]],
            [[0,30,2,3,3,1,0],[0,0,3,20,20,20,20],[0,3,14,17,15,2,16],[1,22,21,1,4,15,12],[0,30,30,30,30,2,2]],
            [[0,45,4,1,40,1,0],[0,23,23,2,44,0,1],[0,34,43,21,33,2,13],[1,25,25,19,50,3,1],[0,34,13,27,27,27,52]],
            [[0,60,0,0,0,0,0],[0,45,54,25,53,32,19],[0,35,1,52,0,52,1],[1,100,2,100,1,100,1],[0,100,100,100,100,100,100]],

         ]


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("man1.png")
        self.image2 = pygame.image.load("man2.png")
        self.image3 = pygame.image.load("man3.png")
        self.image4 = pygame.image.load("man4.png")
        self.image5 = pygame.image.load("man5.png")
        self.pistolImage = pygame.image.load("pistol.png")
        self.ak47Image = pygame.image.load("ak47.png")
        self.rpgImage = pygame.image.load("rpg.png")
        self.sniperImage = pygame.image.load("sniper.png")
        self.gunInfo = [20,10,-10,10,-10,1,10,-5,0]
        self.gunNum = 0
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.y = 400
        self.counter = 0
        self.imagenum = 1
        self.visible = True
        self.direction = 1
        self.health = 100
        self.score = 0
        self.gun = self.pistolImage
        self.gunxchange = 20
        self.gunychange = 10
        self.dchanged = False
        self.akAmmo = 'x'
        self.rpgAmmo = 'x'
        self.snipAmmo = 'x'
        

    def addremove(self):
        if house.wrecked == False:
            self.rect.x = house.rect.x + 80
            self.visible = not self.visible
    
        
    def gunControl(self):
        if self.gunNum == 0:
            self.gun = self.pistolImage
            self.gunInfo = [20,10,-10,10,-10,1,10,-5,0,1]
        if self.gunNum == 1:
            self.gun = self.ak47Image
            self.gunInfo = [0,10,-10,10,-10,0.75, 35,0,8,0]
            
        if self.gunNum == 2:
            self.gun = self.rpgImage
            self.gunInfo = [-7,2,-17,2,-7,10, 40,-12,8,0]
        if self.gunNum == 3:
            self.gun = self.sniperImage
            self.gunInfo = [5,13,-20,13,-15,8, 35,5,5,0]
        if self.direction == 0:
            self.gunxchange = self.gunInfo[2]
            self.gunychange = self.gunInfo[3]
        else:
            self.gunxchange = self.gunInfo[0]
            self.gunychange = self.gunInfo[1]
        if self.direction == 0:
            self.gun = pygame.transform.flip(self.gun, True, False)
            
            
            
        
    def update(self):
        if self.gunNum >= 4:
            self.gunNum = 0
            self.gunControl()
        if self.dchanged == True:
            self.dchanged = False
            self.image = pygame.transform.flip(self.image, True, False)
            
        if self.counter >= 8:
            self.imagenum +=1
            if self.imagenum >= 6:
                self.imagenum = 1
                
            if self.imagenum == 1:
                self.image = self.image1
            elif self.imagenum == 2:
                self.image = self.image2
            elif self.imagenum == 3:
                self.image = self.image3
            elif self.imagenum == 4:
                self.image = self.image4
            elif self.imagenum == 5:
                self.image = self.image5

            if self.direction == 0:
                self.image = pygame.transform.flip(self.image, True, False)
            self.counter = 0
        


class Bullet(pygame.sprite.Sprite):

    def __init__(self, mouse, theplayer):
        pygame.sprite.Sprite.__init__(self)
        if player.gunNum == 0:
            x = 4
            y = 4
        elif player.gunNum == 1:
            x = 2
            y = 2
        elif player.gunNum == 2:
            x = 12
            y = 5
        elif player.gunNum == 3:
            x = 4
            y = 2
        
        self.image = pygame.Surface([x, y])
        self.image.fill(( 0, 0, 0))

        self.mouse_x, self.mouse_y = mouse[0], mouse[1]
        self.player = theplayer

        self.rect = self.image.get_rect()
        
        
        
    def update(self):

        speed = player.gunInfo[4]
        range = 200
        distance = [self.mouse_x - self.player[0], self.mouse_y - (self.player[1])]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        direction = [distance[0] / norm, distance[1 ] / norm]
        bullet_vector = [direction[0] * speed, direction[1] * speed]


        self.rect.x -= bullet_vector[0]
        self.rect.y -= bullet_vector[1]

class Terrain(pygame.sprite.Sprite):
    

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("terrain.png")
        self.rect = self.image.get_rect()
        self.rect.y = 380

class House(pygame.sprite.Sprite):

    
    def __init__(self):
        self.enterimage = pygame.image.load("opening.png")
        self.normalimage = pygame.image.load("shelter.png")
        self.wreckimage = pygame.image.load("wreck.png")
        self.image = self.normalimage
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 330
        self.timer = 0
        self.wrecked = False

    def wreck(self):
        self.wrecked = True
        self.image = self.wreckimage
        player.visible = True
        

    def enter(self):
        if self.wrecked == False:
            self.timer = 10
            self.image = self.enterimage

    def close(self):
        if self.wrecked == False:
            self.image = self.normalimage

    def doorwait(self):
        if self.timer == 5:
            player.addremove()
        if  self.timer < 0:
            self.close()
        self.timer -= 1

class Baloon(pygame.sprite.Sprite):
    
    def __init__(self, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("baloon.png")
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.y = 50
        self.fired = False
        self.rect.x = 600
        self.health = 10;
        self.counter = 0
        self.direction = direction

    def getType(self):
        return 1
    
        
    def update(self):
        if self.direction == 0:
            self.rect.x -= 1
            if self.rect.x < player.rect.x -50:
                if self.fired == False:
                    bomb = Bomb(self.rect.x, self.rect.y)
                    bomb_list.add(bomb)
                    all_sprites_list.add(bomb)
                    self.fired = True

        elif self.direction == 1:
            self.rect.x += 1
            if self.rect.x > player.rect.x -50:
                if self.fired == False:
                    bomb = Bomb(self.rect.x, self.rect.y)
                    bomb_list.add(bomb)
                    all_sprites_list.add(bomb)
                    self.fired = True
                    
class Bomb(pygame.sprite.Sprite):
    def __init__(self, xposit, yposit):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bomb.png")
        self.bombimage = pygame.image.load("mushroom.png")
        self.rect = self.image.get_rect()
        self.rect.x = xposit + 50
        self.rect.y = yposit + 80
        self.detonated = False;
        self.counter = 0;
               
    def update(self):
        if self.rect.y > 415 and self.detonated == False:
            self.rect.x -= 50
            self.rect.y -= 110
            self.image = self.bombimage
            if houseAvail == True:
                house.wreck()
            elif player.rect.x > self.rect.x -150 and player.rect.x < self.rect.x +150:
                player.health -= 50
            self.detonated = True
            
        elif self.detonated == False:
            self.rect.y += 3

        elif self.detonated == True:
            self.counter +=1;
        if self.counter > 30:
            all_sprites_list.remove(self)
            
class Zombie(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("Zombie1.png")
        self.image2 = pygame.image.load("Zombie2.png")
        self.image3 = pygame.image.load("Zombie3.png")
        self.image4 = pygame.image.load("Zombie4.png")
        self.image5 = pygame.image.load("Zombie5.png")
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.y = 390
        self.rect.x = 600
        self.health = 5
        self.counter = 0
        self.direction = 0
        self.imagenum = 1

    def getType(self):
        return 0

    def update(self):  
        self.counter += 1
        if player.visible:
            if self.rect.x < player.rect.x -100 and self.direction == 0:
                self.direction = 1
            elif self.rect.x > player.rect.x +100 and self.direction == 1:
                self.direction = 0
        else:
            if self.rect.x < player.rect.x -400 and self.direction == 0:
                self.direction = 1
            elif self.rect.x > player.rect.x +400 and self.direction == 1:
                self.direction = 0

        if self.direction == 1:
            self.rect.x += 1
        else:
            self.rect.x -= 1
            
        if self.counter == 8:
            if self.imagenum == 6:
                self.imagenum = 1
            if self.imagenum == 1:
                self.image = self.image1
            elif self.imagenum == 2:
                self.image = self.image2
            elif self.imagenum == 3:
                self.image = self.image3
            elif self.imagenum == 4:
                self.image = self.image4
            elif self.imagenum == 5:
                self.image = self.image5
            if self.direction == 1:
                self.image = pygame.transform.flip(self.image, True, False)
            self.imagenum += 1
            self.counter = 0

class Wheelchair(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("timmYYYY1.png")
        self.image2 = pygame.image.load("timmYYYY2.png")
        self.image3 = pygame.image.load("timmYYYY3.png")
        self.image4 = pygame.image.load("timmYYYY4.png")
        self.image = self.image1
        self.rect = self.image.get_rect()
        self.rect.y = 380
        self.rect.x = 600
        self.health = 8
        self.counter = 0
        self.direction = 0
        self.imagenum = 1



    def getType(self):
        return 2
    
    def update(self):
    
        self.counter += 1
        if player.visible:
            if self.rect.x < player.rect.x -100 and self.direction == 0:
                self.direction = 1
            elif self.rect.x > player.rect.x +100 and self.direction == 1:
                self.direction = 0
        else:
            if self.rect.x < player.rect.x -400 and self.direction == 0:
                self.direction = 1
            elif self.rect.x > player.rect.x +400 and self.direction == 1:
                self.direction = 0

        if self.direction == 1:
            self.rect.x += 1
        else:
            self.rect.x -= 1
            
        if self.counter == 8:
            if self.imagenum == 5:
                self.imagenum = 1
            if self.imagenum == 1:
                self.image = self.image1
            elif self.imagenum == 2:
                self.image = self.image2
            elif self.imagenum == 3:
                self.image = self.image3
            elif self.imagenum == 4:

                self.image = self.image4
            elif self.imagenum == 5:
                self.image = self.image5
            if self.direction == 0:
                self.image = pygame.transform.flip(self.image, True, False)


            self.imagenum += 1
            self.counter = 0
        

def Menu():
    menuPosition = 0
    menu = True
    menuzombie = Zombie()
    player.rect.x = 0
    terrain.rect.x = 0
    terrain2.rect.x = 800
    house.rect.x = 600
    while menu: 
           for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        menuPosition -= 1
                        if menuPosition == -1:
                            menuPosition = 2
                    if event.key == K_DOWN:
                        menuPosition += 1
                        if menuPosition == 2:
                            menuPosition = 0
                    if event.key == K_RETURN:
                        if menuPosition == 1:#here is the Menu class function
                            pygame.display.quit()
                            sys.exit()
                        menu = False

           myfont = pygame.font.SysFont("monospace", 40)
           menuzombie.update()
           Startlabel = myfont.render("Start", 1, (0,0,0))
           OptionLabel = myfont.render("High Score: " + str(getHighScore()), 1, (0,0,0))
           QuitLabel = myfont.render("Quit", 1, (0,0,0))
           myfont = pygame.font.SysFont("monospace", 20)
           screen.fill((176, 226, 255))
           screen.blit(terrain.image, terrain.rect)
           screen.blit(house.image, house.rect)
           screen.blit(menuzombie.image, menuzombie.rect)
           if menuPosition == 0:
               pygame.draw.rect(screen,(153,102,255),(100,100,120,50))
           else:
               pygame.draw.rect(screen,(153,102,255),(100,200,100,50))

           screen.blit(Startlabel, (100, 100))
           screen.blit(OptionLabel, (100, 150))
           screen.blit(QuitLabel, (100, 200))
           pygame.display.flip()
           if menuzombie.rect.x == -10:
               menuzombie.rect.x = 810
    return menuPosition

def letsPlay():
    ltimer = 0
    wtimer = 0
    wave = 0
    level = 1;
    daylabel = True;
    playing = True
    player.rect.x = 0
    player.health = 100
    terrain.rect.x = 0
    terrain2.rect.x = 800
    house.rect.x = 600
    house.wrecked = False
    mgSlower = 0
    snipSlower = 30
    rpgSlower = 100
    player.score = 0
    global mainScore
    global firstGun
    mainScore = 0
    global houseAvail
    while playing == True:
            if snipSlower > 0:
                snipSlower -= 1
            elif rpgSlower > 0:
                rpgSlower -= 1
            if pygame.mouse.get_pressed()[0] and player.gunNum == 1:
                mgSlower +=1
                if mgSlower > 4:
                    mgSlower = 0
                if player.visible == True and mgSlower == 0 and player.akAmmo > 0:
                                if player.akAmmo >= 0:
                                    player.akAmmo -= 1
                                bullet = Bullet(pygame.mouse.get_pos(), [player.rect.x, player.rect.y])
                                if player.direction == 0:
                                    bullet.rect.x = player.rect.x + player.gunxchange + player.gunInfo[7]
                                else:
                                    bullet.rect.x = player.rect.x + player.gunxchange + player.gunInfo[6]
                                bullet.rect.y = player.rect.y + player.gunychange  + player.gunInfo[8]
                                all_sprites_list.add(bullet)
                                bullet_list.add(bullet)
            
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                            done = True

                    elif event.type == KEYDOWN:
                        if event.key == K_w:
                            found = False
                            player.gunNum += 1
                            while found == False:
                                if (player.gunNum == 1 and player.akAmmo == 'x') or (player.gunNum == 2 and player.rpgAmmo == 'x') or (player.gunNum == 3 and player.snipAmmo == 'x'):
                                    player.gunNum += 1
                                else:
                                    found = True
                            player.gunControl()
                    
                    elif event.type == pygame.MOUSEBUTTONDOWN and player.gunNum != 1:
                            if player.visible == True and (player.gunNum == 0 or (snipSlower == 0 and player.gunNum == 3 and player.snipAmmo > 0)or (rpgSlower == 0 and player.gunNum == 2 and player.rpgAmmo > 0)):
                                if player.gunNum == 2:
                                    player.rpgAmmo -= 1
                                if player.gunNum == 3:
                                    player.snipAmmo -= 1                                    
                                snipSlower = 30
                                rpgSlower = 100
                                bullet = Bullet(pygame.mouse.get_pos(), [player.rect.x, player.rect.y])
                                if player.direction == 0:
                                    bullet.rect.x = player.rect.x + player.gunxchange + player.gunInfo[7]
                                else:
                                    bullet.rect.x = player.rect.x + player.gunxchange + player.gunInfo[6]
                                bullet.rect.y = player.rect.y + player.gunychange  + player.gunInfo[8]
                                all_sprites_list.add(bullet)
                                bullet_list.add(bullet)
                                
            if player.rect.x < house.rect.x + 100 and player.rect.x > house.rect.x + 60:
                houseAvail = True
            else:
                houseAvail = False
                    

            pressed = pygame.key.get_pressed()
            all_sprites_list.update()
            player.update()
            if pressed[pygame.K_a] and player.rect.x > 0 and player.visible == True:
                    if player.direction == 2:
                        player.dchanged = True
                        player.gun = pygame.transform.flip(player.gun, True, False)
                        player.gunxchange = player.gunInfo[2]
                        player.gunychange = player.gunInfo[3]
                    player.rect.x -= 2
                    player.counter += 1
                    player.direction = 0
                    ltimer -=1
                    wtimer -=1
                
            if pressed[pygame.K_d] and player.visible == True:
                    if player.direction == 0:
                        player.dchanged = True
                        player.gun = pygame.transform.flip(player.gun, True, False)
                        player.gunxchange = player.gunInfo[0]
                        player.gunychange = player.gunInfo[1]
                    ltimer +=1
                    wtimer +=1
                    if player.rect.x > 400:
                            terrain.rect.x -= 2
                            terrain2.rect.x -= 2
                            house.rect.x -= 2
                            for bomb in bomb_list:
                                bomb.rect.x -= 2;
                            for bullet in bullet_list:
                                bullet.rect.x -= 2;
                            for zombie in zombie_list:
                                zombie.rect.x -=2
                    else:
                            player.rect.x += 2
                
                    player.counter += 1
                    player.direction = 2
                
            if terrain.rect.x < -800:
                    terrain.rect.x = 800
            if terrain2.rect.x < -800:
                    terrain2.rect.x = 800

            if pressed[pygame.K_SPACE] and houseAvail == True:
               house.enter()

            house.doorwait()

            for zombie in zombie_list:
                if pygame.sprite.collide_rect(player, zombie) == True and player.visible == True:
                    player.health -= 0.5
                
            if wtimer == 200:
                wtimer = 0
                if levels[level -1][wave][0] == 1:
                    house.rect.x = 850
                    house.wrecked = False
                nzombies = levels[level -1][wave][1]
                xpos = 810
                for x in range(0,nzombies):
                    zombie = Zombie()
                    all_sprites_list.add(zombie)
                    zombie_list.add(zombie)
                    zombie.rect.x = xpos
                    xpos = xpos + 50
                nchair = levels[level -1][wave][5]
                for x in range(0,nchair):
                    chair = Wheelchair()
                    all_sprites_list.add(chair)
                    zombie_list.add(chair)
                    chair.rect.x = xpos
                    xpos = xpos + 80
                xpos = 810
                rzombies = levels[level -1][wave][2]
                xpos = -10
                for x in range(0,rzombies):
                    zombie = Zombie()
                    all_sprites_list.add(zombie)
                    zombie_list.add(zombie)
                    zombie.rect.x = xpos
                    xpos = xpos - 50
                rchair = levels[level -1][wave][6]
                for x in range(0,rchair):
                    chair = Wheelchair()
                    all_sprites_list.add(chair)
                    zombie_list.add(chair)
                    chair.rect.x = xpos
                    xpos = xpos - 80
                xpos = -10
                nballoons = levels[level -1][wave][3]
                xpos = 810
                for x in range(0,nballoons):
                    zombie = Baloon(0)
                    all_sprites_list.add(zombie)
                    zombie_list.add(zombie)
                    zombie.rect.x = xpos
                    xpos = xpos + 50
                xpos = 810
                rballoons = levels[level -1][wave][4]
                xpos = -20
                for x in range(0,rballoons):
                    zombie = Baloon(1)
                    all_sprites_list.add(zombie)
                    zombie_list.add(zombie)
                    zombie.rect.x = xpos
                    xpos = xpos + 50
                xpos = -20

                wave += 1
                if wave == 1:
                    daylabel = True;
                    if level != 1:
                        Upgrades()
                if wave == 2:
                    daylabel = False;
                if wave == 5:
                    level += 1
                    wave = 0
            


            
    
            for bullet in bullet_list:
                for zombie in zombie_list:   
                    if pygame.sprite.collide_rect(bullet, zombie) == True:
                        
                        bullet_list.remove(bullet)
                        all_sprites_list.remove(bullet)
                        zombie.health -= player.gunInfo[5]
                        if zombie.health < 1:
                            zombieType = zombie.getType()
                            if zombie.getType() == 0:
                                player.score += 10
                                mainScore += 10
                            if zombie.getType() == 1:
                                player.score += 30
                                mainScore += 30
                            if zombie.getType() == 2:
                                player.score += 15
                                mainScore += 15
                            zombie_list.remove(zombie)
                            all_sprites_list.remove(zombie)

                

    
                if bullet.rect.y < -10 or bullet.rect.y > 480 or bullet.rect.x < 0 or bullet.rect.x > 800:
                    bullet_list.remove(bullet)
                    all_sprites_list.remove(bullet)

    
            if player.health < 0:
                playing = False
                
            
            
            screen.fill((176, 226, 255))
            screen.blit(terrain.image, terrain.rect)
            screen.blit(terrain2.image, terrain2.rect)
            screen.blit(house.image, house.rect)
            if player.visible == True:
                screen.blit(player.image, player.rect)
            for zombie in zombie_list:
                screen.blit(zombie.image, zombie.rect)
            all_sprites_list.draw(screen)
            if player.visible == True:
                screen.blit(player.gun, (player.rect.x + player.gunxchange, player.rect.y +player.gunychange))

            pygame.draw.rect(screen,(255,0,0),(650,30,100,15))
            if player.health > 0:
                pygame.draw.rect(screen,(26,255,0),(650,30,player.health,15))
            myfont = pygame.font.SysFont("monospace", 15)
            healthLabel = myfont.render("Health:", 1, (0,0,0))
            screen.blit(healthLabel, (580, 30))
            scoreLabel = myfont.render("Score: $ "+str(player.score), 1, (0,0,0))
            screen.blit(scoreLabel, (330, 30))
            ammoLabel = myfont.render("Ammo:  ", 1, (0,0,0))
            screen.blit(ammoLabel, (50, 30))
            screen.blit(ammoImage, (20, 25))
            ammoLabel = myfont.render('', 1, (0,0,0))
            if player.gunNum == 0:
                screen.blit(infinityImage, (105, 34))
            elif player.gunNum == 1:
                ammoLabel = myfont.render(str(player.akAmmo), 1, (0,0,0))
            elif player.gunNum == 2:
                ammoLabel = myfont.render(str(player.rpgAmmo), 1, (0,0,0))
            elif player.gunNum == 3:
                ammoLabel = myfont.render(str(player.snipAmmo), 1, (0,0,0))
            wfont = pygame.font.SysFont("monospace", 15)
            if daylabel == True:
                myfont = pygame.font.SysFont("monospace", 40)
                dayLabel = myfont.render("Day " + str(level), 1, (0,0,0))
                screen.blit(dayLabel, (340, 150))
                if firstGun == 1:
                    screen.blit(ammoLabel, (105, 30))
                    screen.blit(wkey, (10, 60))
                    wLabel = wfont.render("To Change weapon", 1, (0,0,0))
                    screen.blit(wLabel, (75, 70))
                    
                if level == 1:
                    hLabel = wfont.render("To enter a shelter", 1, (0,0,0))
                    screen.blit(hLabel, (house.rect.x - 160, 390))
                    screen.blit(spacekey, (house.rect.x - 150, 360))

                    screen.blit(wdimage, (330, 190))

             
            screen.blit(crosshair, (pygame.mouse.get_pos()[0]-15,pygame.mouse.get_pos()[1] -15))
            pygame.display.flip()
            clock.tick(60)

def gameOver():
        global mainScore
        for zombie in zombie_list:
                zombie_list.remove(zombie)
        for bullet in bullet_list:
                bullet_list.remove(bullet)
        for bomb in bomb_list:
                bomb_list.remove(bomb)
        for sprite in all_sprites_list:
            all_sprites_list.remove(sprite)
            
        x = True
        menuPosition = 0
        setHighScore(mainScore)
        hscore = getHighScore()
        while x: 
            screen.fill((176, 226, 255))
            screen.blit(terrain.image, terrain.rect)
            screen.blit(terrain2.image, terrain2.rect)
            screen.blit(house.image, house.rect)
            pygame.draw.rect(screen,(255,0,0),(650,30,100,15))
            pygame.draw.rect(screen,(26,255,0),(650,30,player.health,15))
            myfont = pygame.font.SysFont("monospace", 15)
            healthLabel = myfont.render("Health:", 1, (0,0,0))
            screen.blit(healthLabel, (580, 30))
            myfont = pygame.font.SysFont("monospace", 60)
            OverLabel = myfont.render("Game Over!", 1, (0,0,0))
            screen.blit(OverLabel, (230, 100))

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        menuPosition -= 1
                        if menuPosition == -1:
                            menuPosition = 1
                    if event.key == K_DOWN:
                        menuPosition += 1
                        if menuPosition == 2:
                            menuPosition = 0
                     if event.key == K_RETURN:
                        x = False

            myfont = pygame.font.SysFont("monospace", 20)
            Retrylabel = myfont.render("Retry", 1, (0,0,0))
            MMLabel = myfont.render("Main Menu", 1, (0,0,0))
            HSLabel = myfont.render("High Score: " + str(hscore), 1, (0,0,0))
            YSLabel = myfont.render("Your Score: " + str(player.score), 1, (0,0,0))
            if menuPosition == 0:
                pygame.draw.rect(screen,(153,102,255),(150,250,70,30))
            elif menuPosition == 1:
                pygame.draw.rect(screen,(153,102,255),(150,280,110,30))
            screen.blit(Retrylabel, (150, 250))
            screen.blit(MMLabel, (150, 280))
            screen.blit(YSLabel, (450, 250))
            screen.blit(HSLabel, (450, 280))


            pygame.display.flip()
        house.wrecked = False
        player.score = 0

        return menuPosition


def Upgrades():
    global firstGun
    u = True
    menuPosition = [0,0]
    while u:
        screen.fill((176, 226, 255))
        screen.blit(terrain.image, terrain.rect)
        screen.blit(terrain2.image, terrain2.rect)
        screen.blit(house.image, house.rect)
        pygame.draw.rect(screen,(255,0,0),(650,30,100,15))
        pygame.draw.rect(screen,(26,255,0),(650,30,player.health,15))
        myfont = pygame.font.SysFont("monospace", 15)
        healthLabel = myfont.render("Health:", 1, (0,0,0))
        screen.blit(healthLabel, (580, 30))
        scoreLabel = myfont.render("Score: $ "+str(player.score), 1, (0,0,0))
        screen.blit(scoreLabel, (330, 30))
        ammoLabel = myfont.render("Ammo:  ", 1, (0,0,0))
        screen.blit(ammoLabel, (50, 30))
        screen.blit(ammoImage, (20, 25))
        ammoLabel = myfont.render('', 1, (0,0,0))
        if player.gunNum == 0:
            screen.blit(infinityImage, (105, 30))
        elif player.gunNum == 1:
            ammoLabel = myfont.render(str(player.akAmmo), 1, (0,0,0))
        elif player.gunNum == 2:
            ammoLabel = myfont.render(str(player.rpgAmmo), 1, (0,0,0))
        elif player.gunNum == 3:
             ammoLabel = myfont.render(str(player.snipAmmo), 1, (0,0,0))
        screen.blit(ammoLabel, (105, 30))
 
        for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        menuPosition[1] -= 1

                    if event.key == K_DOWN:
                        menuPosition[1] += 1

                    if event.key == K_LEFT:
                        menuPosition[0] -= 1

                    if event.key == K_RIGHT:
                        menuPosition[0] += 1

                    if event.key == K_RETURN:
                        if menuPosition[1] == 3:   
                            u = False
                        elif menuPosition == [0,0]:
                            if player.akAmmo == 'x':
                                if (player.score - 400 ) >= 0:
                                    player.score -= 400
                                    player.akAmmo = 80
                                    firstGun += 1
                        elif menuPosition == [0,1]:
                            if player.rpgAmmo == 'x':
                                if (player.score - 800) >= 0:
                                    player.score -= 800
                                    player.rpgAmmo = 25
                                    firstGun += 1

                        elif menuPosition == [0,2]:
                            if player.snipAmmo == 'x':
                                if (player.score - 1000) >= 0:
                                    player.score -= 1000
                                    player.snipAmmo = 50
                                    firstGun += 1

                        elif menuPosition == [1,0]:
                            if player.akAmmo != 'x':
                                if (player.score - 100) >= 0:
                                    player.score -= 100
                                    player.akAmmo += 40
                        elif menuPosition == [1,1]:
                            if player.rpgAmmo != 'x':
                                if (player.score - 100) >= 0:
                                    player.score -= 100
                                    player.rpgAmmo += 30
                        elif menuPosition == [1,2]:
                            if player.snipAmmo != 'x':
                                if (player.score - 100) >= 0:
                                    player.score -= 100
                                    player.snipAmmo += 40
    
                            
        if menuPosition[0] > 1:
            menuPosition[0]= 0
        elif menuPosition[0] < 0:
            menuPosition[0]= 1
        if menuPosition[1] > 3:
            menuPosition[1]= 0
        elif menuPosition[1] < 0:
            menuPosition[1]= 3
            
        if menuPosition[0] == 0:
            x = 100
        elif menuPosition[0] == 1:
            x = 400
        if menuPosition[1] == 0:
            y = 100
        elif menuPosition[1] == 1:
            y = 130
        elif menuPosition[1] == 2:
            y = 160
        elif menuPosition[1] == 3:
            y = 190

        if menuPosition[1] != 3:
            if menuPosition[0] == 0:
                pygame.draw.rect(screen,(153,102,255),(x,y,150,30))
            else:
                pygame.draw.rect(screen,(153,102,255),(x,y,210,30))
        else:
            pygame.draw.rect(screen,(153,102,255),(330,210,130,30))
            
        myfont = pygame.font.SysFont("monospace", 20)
        if player.akAmmo == 'x':
            if (player.score - 400) >= 0:
                Label = myfont.render("Machine Gun  $400", 1, (0,0,0))
            else:
                Label = myfont.render("Machine Gun  $400", 1, (162,149,149))
            screen.blit(Label, (100, 100))
            Label = myfont.render("Machine Gun Ammo  $100", 1, (162,149,149))
            screen.blit(Label, (400, 100))
        else:
            Label = myfont.render("Machine Gun  $400", 1, (162,149,149))
            screen.blit(Label, (100, 100))
            if (player.score - 100) >= 0:
                Label = myfont.render("Machine Gun Ammo  $100", 1, (0,0,0))
            else:
                Label = myfont.render("Machine Gun Ammo  $100", 1, (162,149,149))
            screen.blit(Label, (400, 100))

        if player.rpgAmmo == 'x':
            if (player.score - 800) >= 0:
                Label = myfont.render("RPG          $800", 1, (0,0,0))
            else:
                Label = myfont.render("RPG          $800", 1, (162,149,149))
            screen.blit(Label, (100, 130))
            Label = myfont.render("RPG Ammo          $100", 1, (162,149,149))
            screen.blit(Label, (400, 130))
        else:
            Label = myfont.render("RPG          $800", 1, (162,149,149))
            screen.blit(Label, (100, 130))
            if (player.score - 100) >= 0:
                Label = myfont.render("RPG Ammo          $100", 1, (0,0,0))
            else:
                Label = myfont.render("RPG Ammo          $100", 1, (162,149,149))
            screen.blit(Label, (400, 130))

        if player.snipAmmo == 'x':
            if (player.score - 1000) >= 0:
                Label = myfont.render("Sniper Rifle $1000", 1, (0,0,0))
            else:
                Label = myfont.render("Sniper Rifle $1000", 1, (162,149,149))
            screen.blit(Label, (100, 160))
            Label = myfont.render("Sniper Rifle Ammo $100", 1, (162,149,149))
            screen.blit(Label, (400, 160))
        else:
            Label = myfont.render("Sniper Rifle $1000", 1, (162,149,149))
            screen.blit(Label, (100, 160))
            if (player.score - 100) >= 0:
                Label = myfont.render("Sniper Rifle Ammo $100", 1, (0,0,0))
            else:
                Label = myfont.render("Sniper Rifle Ammo $100", 1, (162,149,149))
            screen.blit(Label, (400, 160))
            
            
        Label = myfont.render("Continue...", 1, (0,0,0))
        screen.blit(Label, (330, 210))
        pygame.display.flip()
    

def getHighScore():
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")
    return high_score


def setHighScore(current_score):
    high_score = getHighScore()
    if current_score > high_score: 
        # We do! Save to disk
        try:
            # Write the file to disk
            high_score_file = open("high_score.txt", "w")
            high_score_file.write(str(current_score))
            high_score_file.close()
        except IOError:
            # Hm, can't write it.
            print("Too bad I couldn't save it.")
    

if __name__ == "__main__":
    firstGun = 0
    pygame.init()
    highScore = 0
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((800, 500))
    all_sprites_list = pygame.sprite.Group()
    bullet_list = pygame.sprite.Group()
    zombie_list = pygame.sprite.Group()
    bomb_list = pygame.sprite.Group()
    done = False
    ammoImage = pygame.image.load("ammoIcon.png")
    infinityImage = pygame.image.load("infinity.png")
    wdimage = pygame.image.load("wd.png")
    crosshair = pygame.image.load("crosshair.png")
    wkey = pygame.image.load("wkey.png")
    spacekey = pygame.image.load("space.png")
    y = 30
    level = 1;
    ground1x = 0
    ground2x = 800
    clock = pygame.time.Clock()
    player = Player()
    terrain = Terrain()
    terrain2 = Terrain()
    terrain2.rect.x = 800
    houseAvail = False
    house = House()
    x = True
    while x == True:
        menuChoice = Menu()
        while menuChoice == 0:
            letsPlay()
            menuChoice = gameOver()
            print menuChoice
