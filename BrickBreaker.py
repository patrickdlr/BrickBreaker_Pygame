import sys, pygame, random, math, time
from pygame.locals import *



#task: make block 2-hit required, put two balls?, put up pause menu
#show 4 version of games on one screen? lol get a recorder
#import pictures, sound = NOPE
#add border limit for dropping block? and orange bar

#fix dropping block (not in line, causes whole army of blocks to halt until its destroyed)

#clean up code?
#Brick breaker

#Try hockey style, dodging bar, scoreboard, collision sound, pause menu, pushing bar (speed up the ball), add more balls, numbering on army of enemies, animatedbackground?, floating power up, OR learn about delay time?, guitar hero style on bottom

#make each block fall when hit once, add 8 directions to the ball


#init, display, color, fps, tick, caption, font
pygame.init()

swidth = 800
print(swidth)
sheight = 600
windowsurface = pygame.display.set_mode((swidth,sheight), 0,32)

pygame.display.set_caption('Project')
pygame.mouse.set_visible(False)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLOR1 = (45, 45, 155)
COLOR2 = (155, 45, 45)
COLOR3 = (155, 75, 45)
COLOR4 = (155, 45, 75)
COLOR5 = (45, 2, 155)
COLOR6 = (155, 45, 2)
COLOR7 = (2, 75, 45)
COLOR8 = (155, 45, 155)
TEXTCOLOR = (255, 255, 255)
BACKGROUNDCOLOR = (0, 0, 0)

FPS = 60
mainClock = pygame.time.Clock()

##FONT
#phrase1
basicfont1 = pygame.font.SysFont('calibri', 48)
phrase1 = basicfont1.render('brick breaker', 1, TEXTCOLOR)
phrase1rect = phrase1.get_rect()
phrase1rect.centerx = math.floor(swidth/2)
phrase1rect.centery = math.floor(sheight/2) - 27

#phrase2
basicfont2 = pygame.font.SysFont('calibri', 24)
phrase2 = basicfont2.render('by Patrick DLR', 1, TEXTCOLOR)
phrase2rect = phrase1.get_rect()
phrase2rect.centerx = math.floor(swidth/2)
phrase2rect.centery = math.floor(sheight/2) + 27

#phrase3
basicfont3 = pygame.font.SysFont('calibri', 20)
phrase3 = basicfont3.render('Press any key to start.', 1, TEXTCOLOR)
phrase3rect = phrase1.get_rect()
phrase3rect.centerx = math.floor(swidth/2) + 45
phrase3rect.centery = sheight - math.floor(sheight*.1)
print(phrase3rect)

#phrase4
basicfont4 = pygame.font.SysFont('calibri', 20)
phrase4 = basicfont4.render('GAME OVER', 1, RED)
phrase4rect = phrase1.get_rect()
phrase4rect.centerx = math.floor(swidth/2) + 85
phrase4rect.centery = 30 + math.floor(sheight*.8)


#phrase6
basicfont6 = pygame.font.SysFont('calibri', 24)
phrase6 = basicfont6.render('Score', 1, RED)
phrase6rect = phrase6.get_rect()
phrase6rect.centerx = math.floor(swidth/2) + 85
phrase6rect.centery = 30 + math.floor(sheight*.8)


#sound
pygame.mixer.music.load('background.mid')
gameOverSound = pygame.mixer.Sound('gameover.wav')


#player image
playerimage = pygame.image.load(r"C:\Users\patri\OneDrive\Pictures\Akali_rework.jpg")
playerimage = pygame.transform.scale(playerimage, (67,30))

#player rect
playerrect = playerimage.get_rect() #blit



#print player
print(playerrect)
print(playerimage)

#enemyrect (transfered)
enemyrect1 = pygame.Rect(0, 0, 37, 30) #non-image
#enemyrect2 = pygame.Rect(random.randint(60, swidth-60),120,120,10)

coverforenemyrect1 = pygame.Rect(enemyrect1.left, enemyrect1.top, 67, 30)
print(enemyrect1)
#enemy


#armyofenemies, rest of configuration put in game loop
#armywidth = random.randint(30,50)
#armyheight = random.randint(10,30)
#armywidth = random.randint(30,50)
#armyheight = random.randint(10,30)
#row = 1
#column = 300
#make a block of bricks = looks okay!
#armyofenemies =  []



#rate,speed, gravity,

#player
playerspeed = 10
slowplayer = playerspeed/2
normalplayerspeed = playerspeed

#enemy
enemyspeed = 1 #tbd
enemy1direction = 'left'
enemy2direction = 'left'
enemymoveup = False
enemymovedown = False
enemymoveleft = False
enemymoveright = False


#ball
ball = pygame.Rect(math.floor(swidth*.5), math.floor(sheight*.5), 20,20)
#laser
shootlaser = False
laserlist = []


moveup = movedown = moveleft = moveright = False



gameover = False
go_on = False

#yourconfiguration
randomblockmode = False
freeze = 0
freezefalldown = []

score = 0
score2 = 0

def randomblockchoose(a):
    nw = random.choice(armyofenemies[math.floor(int(a)):])['rect']
    return nw

def blocklabeler(numb):
    basicfont5 = pygame.font.SysFont('calibri', 4)
    phrase5 = basicfont5.render(str(a), 1, WHITE)
    phrase5rect = phrase5.get_rect()
    return phrase5rect


#pregameloop
while True:

    basicfont6 = pygame.font.SysFont('calibri', 24)
    phrase6 = basicfont6.render(f'Score: {score}', 1, WHITE)
    phrase6rect = phrase6.get_rect()
    phrase6rect.centerx = math.floor(phrase6rect.width/2)
    phrase6rect.centery = math.floor(phrase6rect.height/2)


    basicfont7 = pygame.font.SysFont('calibri', 24)
    phrase7 = basicfont7.render(f'Missed: {score2}', 1, WHITE)
    phrase7rect = phrase7.get_rect()
    phrase7rect.centerx = math.floor(swidth-phrase7rect.width/2)
    phrase7rect.centery = math.floor(phrase7rect.height/2)

    #game start screen
    windowsurface.fill(BLACK)
    windowsurface.blit(phrase6, phrase6rect)
    windowsurface.blit(phrase7, phrase7rect)
    pygame.mixer.music.stop()

    windowsurface.blit(phrase1, phrase1rect)
    windowsurface.blit(phrase2, phrase2rect)
    windowsurface.blit(phrase3, phrase3rect)
    if gameover == True:
        windowsurface.blit(phrase4, phrase4rect)
        gameover = False


    pygame.display.update()

    while True:
        for a in pygame.event.get():
            if a.type == QUIT:
                sys.exit(), pygame.quit()
            if a.type == MOUSEBUTTONDOWN:
                if a.button == 1:
                    break
            if a.type == KEYDOWN:
                if a.key == K_ESCAPE:
                    sys.exit(), pygamequit()
                go_on = True
                break
        if go_on == True:
            go_on = False
            break
    score = 0
    score2 = 0


    #game setup 1
    #(anything that needs to be set-up/restored between games)

    armywidth = random.randint(30,35)
    armyheight = random.randint(math.floor(armywidth*.5),math.floor(armywidth*.8))
    row = random.randint(5,8)
    column = random.randint(10,40) #(row-2*column)+1    (len(armyofenemies)/row)*(row-1)
    horizontalgap = 1.2 #horizontal gap
    verticalgap = 1.2
    armyofenemies = []
    blockid = 1
    hitted2 = []

    for i in range(row): #row
        i = i+1
        for a in range(column): #column
            randomcolor = (random.randint(90,120),random.randint(100,180),random.randint(200,240))

            a = a+1
            if a*(armywidth) < (swidth - armywidth)/1.4: #how wide  (prevent overexpanding)
                rect = pygame.Rect(a*(armywidth*verticalgap),(armyheight*horizontalgap) * i,armywidth,armyheight)
                armyofenemies.append({'rect':rect, 'color':randomcolor, 'hit':1, 'falldown':False, 'blockid':rect.centerx})

            else:
                break

    for a in armyofenemies:
        a['rect'].centery += 40 #SOLVED (why does = only show 1 row, while += still allows all rows showing.
    print(len(armyofenemies))
    armyofenemiesdirection = 'left'


    #game setup 2
    #laser emptyer
    laserlist = []


    #game setup 3
    #enemyrect1 repositioner
    enemyrect1.bottom = sheight


    #player positioning
    playerrect = pygame.Rect(0, 0, 67, 30)
    playerrect.centerx = random.randint(math.floor(playerrect.width/2),math.floor(swidth-(playerrect.width/2)))
    playerrect.centery = math.floor(sheight * .95)


    #enemy positioning

    enemyrect1 = pygame.Rect(0, 0, 67, 30)
    enemyrect1.centerx = random.randint(math.floor(playerrect.width/2),math.floor(swidth-(playerrect.width/2)))
    enemyrect1.bottom = math.floor(sheight)
    coverforenemyrect1 = pygame.Rect(enemyrect1.left, enemyrect1.top, 67, 30)

    #ball
    ball.centerx = math.floor(random.randint(ball.width,swidth-ball.width))
    ball.centery = math.floor(sheight*.9)
    balldirection = 'downleft'
    ballspeed = 10
    slowballspeed = math.floor(ballspeed/3)
    normalballspeed = ballspeed


    #arandom block
    if randomblockmode == True:
        arandomblock = random.choice(armyofenemies)['rect']
        freeze = arandomblock.centerx


    end_the_game_now = False
    pygame.mixer.music.play(-1, 0.0)


    #urgent
    urgentlist = []
    urgentlist2 = []
    num = 0

    phrase7rect = phrase7.get_rect()


    #realgameloop
    while True:
        phrase6 = basicfont6.render(f'Score: {score}', 1, WHITE)
        phrase6rect = phrase6.get_rect()

        phrase7 = basicfont7.render(f'Missed: {score2}', 1, WHITE)
        phrase7rect = phrase7.get_rect()
        phrase7rect.centerx = math.floor(swidth-phrase7rect.width/2)


        #game over
        windowsurface.fill(BLACK)
        windowsurface.blit(phrase6, phrase6rect)
        windowsurface.blit(phrase7, phrase7rect)


        if end_the_game_now == True:
            gameover = True
            break

        if len(armyofenemies) == 0:
            gameover = True
            break

        #gameover
        if ball.centery >= sheight-3:
            gameover = True
            break

        #KEY CONTROL
        for a in pygame.event.get():


            if a.type == QUIT:
                sys.exit(), pygame.quit()


            if a.type == KEYDOWN:
                if a.key == K_w:
                    moveup = True
                    movedown = False
                if a.key == K_s:
                    moveup = False
                    movedown = True
                if a.key == K_a:
                    moveleft = True
                    moveright = False
                if a.key == K_d:
                    moveleft = False
                    moveright = True

                if a.key == K_UP:
                    enemymoveup = True
                if a.key == K_DOWN:
                    enemymovedown = True
                if a.key == K_LEFT:
                    enemymoveleft = True
                if a.key == K_RIGHT:
                    enemymoveright = True

                if a.key == K_SPACE:
                    shootlaser = True

                if a.key == K_q:
                    end_the_game_now = True

            if a.type == KEYUP:
                if a.key == K_w:
                    moveup = False
                if a.key == K_s:
                    movedown = False
                if a.key == K_a:
                    moveleft = False
                if a.key == K_d:
                    moveright = False

                if a.key == K_UP:
                    enemymoveup = False
                if a.key == K_DOWN:
                    enemymovedown = False
                if a.key == K_LEFT:
                    enemymoveleft = False
                if a.key == K_RIGHT:
                    enemymoveright = False

                if a.key == K_SPACE:
                    shootlaser = False


            if a.type == MOUSEBUTTONDOWN:
                ballspeed = slowballspeed
            if a.type == MOUSEBUTTONUP:
                ballspeed = normalballspeed
                 #   playerrect.centerx = a.pos[0]
                 #   playerrect.centery = a.pos[1]



#movement: player
        if playerrect.top > 0 and moveup == True:
            playerrect.centery -= playerspeed
        if playerrect.bottom < sheight and movedown == True:
            playerrect.centery += playerspeed
        if playerrect.left > 0 and moveleft == True:
            playerrect.centerx -= playerspeed
        if playerrect.right < swidth and moveright == True:
            playerrect.centerx += playerspeed
#automated moving bar
        stopmoving = False
        if ball.centery >= sheight*.20:
            if stopmoving == False and playerrect.centerx <= ball.centerx:
                playerrect.centerx += random.randint(1,6)
                stopmoving = True
            if stopmoving == False and playerrect.centerx >= ball.centerx:
                playerrect.centerx -= random.randint(1,6)
                stopmoving = True
        if ball.centery >= sheight*.50:
            if playerrect.centerx <= ball.centerx:
                playerrect.centerx += 14
            if playerrect.centerx >= ball.centerx:
                playerrect.centerx -= 14
        if ball.centery >= sheight*.6:
            if playerrect.centerx <= ball.centerx:
                playerrect.centerx += 45
            if playerrect.centerx >= ball.centerx:
                playerrect.centerx -= 45
        stopmoving = False
#erase laser that are off border
        for l in laserlist:
            if l['rect'].centery <= 0:
                laserlist.remove(l)




       #
        enemyspeed_toggle = False

        #automation 2
        '''
        for a in armyofenemies:
            urgentlist = []
            urgentlist2 = []
            if a['hit'] == 2 and a['rect'].centery >= math.floor(enemyrect1.top - (sheight * .2)): #priority 1
                urgentlist += [a['rect'].centerx]

                #laserlist.append({'rect':pygame.Rect(enemyrect1.centerx, enemyrect1.top, 3, 16)})
                for u in urgentlist:

                    if enemyrect1.centerx <= u:
                        if u + 10 > enemyrect1.centerx:
                            enemyrect1.centerx += 8
                            shootlaser = True
                        elif u + 5 > enemyrect1.centerx:
                            enemyrect1.centerx += 0
                            shootlaser = True
                        else:
                            enemyrect1.centerx += 20
                            shootlaser = True
                    if enemyrect1.centerx > u:
                        if u - 10 < enemyrect1.centerx:
                            enemyrect1.centerx -= 8
                            shootlaser = True
                        elif u - 5 < enemyrect1.centerx:
                            enemyrect1.centerx -= 0
                            shootlaser = True
                        else:
                            enemyrect1.centerx -= 20
                            shootlaser = True


                #if laserlist[-1]['rect'].centery <= math.floor(sheight * .8):
                    #shootlaser = True #again
                    #shootlaser = False

                #if len(laserlist) >= 1:
                if len(laserlist) == 0:
                    shootlaser = True
                if len(laserlist) >= 1 and laserlist[-1]['rect'].centery >= enemyrect1.top - (sheight * .05):
                    shootlaser = False




            elif a['hit'] == 2 and a['rect'].centery >= math.floor(enemyrect1.top - (sheight * .5)):
                if a['hit'] == 2 and a['rect'].centery >= math.floor(enemyrect1.top - (sheight * .2)):
                    break
                urgentlist += [a['rect'].centerx]

                #laserlist.append({'rect':pygame.Rect(enemyrect1.centerx, enemyrect1.top, 3, 16)})
                for u in urgentlist:

                    if enemyrect1.centerx <= u:
                        if u + 10 > enemyrect1.centerx:
                            enemyrect1.centerx += 8
                            shootlaser = True
                        elif u + 5 > enemyrect1.centerx:
                            enemyrect1.centerx += 0
                            shootlaser = True
                        else:
                            enemyrect1.centerx += 14
                            shootlaser = True
                    if enemyrect1.centerx > u:
                        if u - 10 < enemyrect1.centerx:
                            enemyrect1.centerx -= 8
                            shootlaser = True
                        elif u - 5 < enemyrect1.centerx:
                            enemyrect1.centerx -= 0
                            shootlaser = True
                        else:
                            enemyrect1.centerx -= 14
                            shootlaser = True


                #if laserlist[-1]['rect'].centery <= math.floor(sheight * .8):
                    #shootlaser = True #again
                    #shootlaser = False

                #if len(laserlist) >= 1:
                if len(laserlist) >= 1 and laserlist[-1]['rect'].centery >= enemyrect1.top - (sheight * .1):
                    shootlaser = False

            elif a['hit'] == 2 and a['rect'].centery >= math.floor(sheight * .3):
                if a['hit'] == 2 and a['rect'].centery >= math.floor(enemyrect1.top - (sheight * .2)):
                    break
                #laserlist.append({'rect':pygame.Rect(enemyrect1.centerx, enemyrect1.top, 3, 16)})
                if enemyrect1.centerx <= a['rect'].centerx:
                    if a['rect'].centerx + 10 > enemyrect1.centerx:
                        enemyrect1.centerx += 0
                        shootlaser = True
                    else:
                        enemyrect1.centerx += 8
                        shootlaser = True

                if enemyrect1.centerx > a['rect'].centerx:
                    if a['rect'].centerx - 10 < enemyrect1.centerx:
                        enemyrect1.centerx -= 0
                        shootlaser = True
                    else:
                        enemyrect1.centerx -= 8
                        shootlaser = True

                #if len(laserlist) >= 1:
                    #shootlaser = False
                if len(laserlist) >= 1 and laserlist[-1]['rect'].centery >= enemyrect1.top - (sheight * .6):
                    shootlaser = False



                #enemyrect1.centerx =
            elif a['hit'] == 1:# and a['rect'].centery >= math.floor(sheight * .5):
                #laserlist.append({'rect':pygame.Rect(enemyrect1.centerx, enemyrect1.top, 3, 16)})
                if a['hit'] == 2 and a['rect'].centery >= math.floor(enemyrect1.top - (sheight * .2)):
                    break
                if enemyrect1.centerx <= a['rect'].centerx:
                    if a['rect'].centerx + 10 > enemyrect1.centerx:
                        enemyrect1.centerx += 0
                        shootlaser = True
                    else:
                        enemyrect1.centerx += 8
                        #shootlaser = True

                if enemyrect1.centerx > a['rect'].centerx:
                    if a['rect'].centerx - 10 < enemyrect1.centerx:
                        enemyrect1.centerx -= 0
                        shootlaser = True
                    else:
                        enemyrect1.centerx -= 8
                        #shootlaser = True

                if len(laserlist) >= 1 and laserlist[-1]['rect'].centery >= enemyrect1.top - (sheight * .4):
                    shootlaser = False
        '''
        #enemyspeed_toggle = True

        #automation 3
        shootlaser = True

        for a in armyofenemies:
            if a['hit'] == 2:
                hitted2.append(a['rect'].centerx)


        #if len(armyofenemies) < 20:
         #   for a in armyofenemies:

         #       enemyrect1.centerx = a['rect'].centerx


        #automation 3
        if len(hitted2) >= 1:
            if enemyrect1.centerx > hitted2[0]:
                if enemyrect1.centerx <= hitted2[0] + 3:
                    enemyrect1.centerx -= 1
                else:
                    enemyrect1.centerx -= 14

            if enemyrect1.centerx < hitted2[0]:
                if enemyrect1.centerx >= hitted2[0] - 3:
                    enemyrect1.centerx += 1
                else:
                    enemyrect1.centerx += 14


        #if len(armyofenemies) < 20:
        #    for a in armyofenemies:
        #        if a['rect'].centery > enemyrect1.centery:
        #            enemyrect1.centery = a['rect'].centery + (sheight * .2#)
     #           else:
      #              enemyrect1.centery = math.floor(sheight*.5)

       # if len(armyofenemies) < 20:
        #    for a in armyofenemies:
         #       if enemy1direction == 'left':
          #          hitted2.append(a['rect'].centerx - 35)

           #     if enemy1direction == 'right':
            #        hitted2.append(a['rect'].centerx + 35)








        #enemies:
        if enemyspeed_toggle == True:
            if enemy1direction == 'left': #use signal variable
                enemyrect1.centerx -= 0
            elif enemy1direction == 'right':
                enemyrect1.centerx += 0 #or enemyspeed

            if enemyrect1.right >= swidth: #>= instead of == to gaurante enemy direction change in case the game "runs too fast" and "misses the point"w
                enemy1direction = 'left'
            elif enemyrect1.left <= 0:
                enemy1direction = 'right'

        #pygame.draw.rect(windowsurface, COLOR3, enemyrect1)

       # if enemy2direction == 'left': #use signal variable
       #     enemyrect2.centerx -= enemyspeed
       # elif enemy2direction == 'right':
       #     enemyrect2.centerx += enemyspeed

       # if enemyrect2.right >= swidth - 30: #>= instead of == to gaurante enemy direction change in case the game "runs too fast" and "misses the point"w
       #     enemy2direction = 'left'
       # elif enemyrect2.left <= 30:
       #     enemy2direction = 'right'
       # pygame.draw.rect(windowsurface, COLOR3, enemyrect2)

        #move an enemy define:
        if enemymoveup == True:
            enemyrect1.centery -= 4
        if enemymovedown == True:
            enemyrect1.centery += 4
        if enemymoveleft == True:
            enemyrect1.centerx -= 9
        if enemymoveright == True:
            enemyrect1.centerx += 9


    #armyofenemiesdirection = 'left'
    #print(len(armyofenemies))


        #movement: armyofenemies/blocks
        for a in armyofenemies:
            if a['rect'].right >= swidth:
                 armyofenemiesdirection = 'left'
            if a['rect'].left <= 0:
                armyofenemiesdirection = 'right'
        if armyofenemiesdirection == 'left':
            for a in armyofenemies:
                a['rect'].centerx -= 1
                if a['hit'] == 1:
                    a['blockid'] = a['rect'].centerx
                if a['hit'] == 2:
                    a['rect'].centerx = a['blockid']

        if armyofenemiesdirection == 'right':
            for a in armyofenemies:
                a['rect'].centerx += 1
                if a['hit'] == 1:
                    a['blockid'] = a['rect'].centerx
                if a['hit'] == 2:
                    a['rect'].centerx = a['blockid']



        #ball:
        #direction define
        if balldirection == 'downleft':
            ball.centerx -= ballspeed
            ball.centery += ballspeed
        if balldirection == 'downright':
            ball.centerx += ballspeed
            ball.centery += ballspeed
        if balldirection == 'upleft':
            ball.centerx -= ballspeed
            ball.centery -= ballspeed
        if balldirection == 'upright':
            ball.centerx += ballspeed
            ball.centery -= ballspeed



        #ball direction change (against player)
        if playerrect.colliderect(ball):
            if balldirection == 'downleft':
                balldirection = 'upleft'
            if balldirection == 'downright':
                balldirection = 'upright'



        #collision between ball and wall
        if ball.top <= 0:
            if balldirection == 'upleft':
                balldirection = 'downleft'
            if balldirection == 'upright':
                balldirection = 'downright'

        if ball.left <= 0:
            if balldirection == 'downleft':
                balldirection = 'downright'
            if balldirection == 'upleft':
                balldirection = 'upright'
        if ball.right >= swidth:
            if balldirection == 'downright':
                balldirection = 'downleft'
            if balldirection == 'upright':
                balldirection = 'upleft'

        if ball.bottom >= sheight:
            if balldirection == 'downleft':
                balldirection = 'upleft'
            if balldirection == 'downright':
                balldirection = 'upright'





        ##collision between ball and enemyrect1
        lockindirection = False

        if ball.colliderect(enemyrect1): #checks for error carefully!! review each line of code thoroughly.
            if lockindirection == False and balldirection == 'upleft':
                if ball.top <= enemyrect1.bottom and ball.bottom > enemyrect1.bottom: #good
                    balldirection = 'downleft'
                    lockindirection = True

                if ball.left <= enemyrect1.right and ball.right > enemyrect1.right and ball.top <= enemyrect1.bottom and ball.bottom >= enemyrect1.top: #good
                    balldirection = 'upright'
                    lockindirection = True

            if lockindirection == False and balldirection == 'upright':
                if ball.top <= enemyrect1.bottom and ball.bottom > enemyrect1.bottom: #good
                    balldirection = 'downright'
                    lockindirection = True

                if ball.right >= enemyrect1.left and ball.left < enemyrect1.left and ball.top <= enemyrect1.bottom and ball.bottom >= enemyrect1.top: #good
                    balldirection = 'upleft'
                    lockindirection = True



    #--------------------------------------------
            if lockindirection == False and balldirection == 'downleft':
                if ball.bottom >= enemyrect1.top and ball.top < enemyrect1.top: #good
                    balldirection = 'upleft'
                    lockindirection = True

                if ball.left <= enemyrect1.right and ball.right > enemyrect1.right and ball.bottom >= enemyrect1.top and ball.top <= enemyrect1.bottom: #make more specific
                    balldirection = 'downright'
                    lockindirection = True


            if lockindirection == False and balldirection == 'downright':
                if ball.bottom >= enemyrect1.top and ball.top < enemyrect1.top: #good, ACTUALLY ITS BAD LOL. Solved.
                    balldirection = 'upright'
                    lockindirection = True

                if ball.right >= enemyrect1.left and ball.left < enemyrect1.left and ball.bottom >= enemyrect1.top and ball.top <= enemyrect1.bottom: #make more specific
                    balldirection = 'downleft'
                    lockindirection = True


    #####

        #produces laser
        if shootlaser == True:
            if len(laserlist) == 0:
                laserlist.append({'rect':pygame.Rect(enemyrect1.centerx, enemyrect1.top, 3, 16)})

            if len(laserlist) >= 1 and laserlist[-1]['rect'].centery <= math.floor(enemyrect1.centery - (sheight * .1)):
                #num = len(laserlist) -

                laserlist.append({'rect':pygame.Rect(enemyrect1.centerx, enemyrect1.top, 3, 16)})
                #num -= 1

        for a in laserlist:
            a['rect'].centery -= 7



        #laser destroys bricks (causes ValueError: list.remove(x): x not in list -- maybe put in different order (brick/ball and brick/laser)
        #for a in laserlist:
        #    for m in armyofenemies:
         #       if a['rect'].colliderect(m['rect']):
         #           laserlist.remove(a)
         #           armyofenemies.remove(m)



        #collision: laser and block
        for m in armyofenemies:
            for a in laserlist:
                if m['rect'].colliderect(a['rect']):
                    laserlist.remove(a)
                    if m['hit'] == 2:
                        if m in armyofenemies:
                            armyofenemies.remove(m)
                            for w in hitted2:
                                if m['rect'].centerx == w:
                                    hitted2.remove(w)

                        score += 1
                    if m['hit'] == 1:
                        m['hit'] += 1
                        m['color'] = (random.randint(70,85),14,14)
                        m['falldown'] = True
                        #freezefalldown += {a['blockid']:a['rect'].centerx}
                        #m['blockid'] = \
                        m['rect'].centerx = m['blockid']

                    if randomblockmode == True:
                        if m['rect'] == arandomblock:
                            if len(armyofenemies) > 0:
                                arandomblock = randomblockchoose((len(armyofenemies)/row)*(row-1))
                                freeze = arandomblock.centerx
                                arandomblock.centerx = freeze

        lockindirection = False

        #collision between ball and block
        for a in armyofenemies:
            if ball.colliderect(a['rect']):

                if a['hit'] == 2:
                    armyofenemies.remove(a)
                    score += 1
                    for w in hitted2:
                        if a['rect'].centerx == w:
                            hitted2.remove(w)

                if a['hit'] == 1:
                    a['hit'] += 1
                    a['color'] = (random.randint(0,80), random.randint(130,205), random.randint(130,170))
                    #print(pygame.Color('#ffebee'))(255, 235, 238, 255)
                    a['falldown'] = True
                    #freezefalldown += {a['blockid']:a['rect'].centerx}
                    #a['rect'].centerx = freezefalldown[-1]
                    a['rect'].centerx = a['blockid']

                #armyofenemies.remove(a)

                if randomblockmode == True:
                    if a['rect'] == arandomblock:
                        if len(armyofenemies) > 0:
                            arandomblock = randomblockchoose((len(armyofenemies)/row)*(row-1))
                            freeze = arandomblock.centerx
                            #arandomblock.centerx = freeze



                if '0' in str(len(armyofenemies)):
                    print('---')
                    print(f'{len(armyofenemies)}')
                else:
                    print(f'{len(armyofenemies)}')



                if lockindirection == False and balldirection == 'upleft':
                    if ball.top <= a['rect'].bottom and ball.bottom > a['rect'].bottom: #good
                        balldirection = 'downleft'
                        lockindirection = True

                    if ball.left <= a['rect'].right and ball.right > a['rect'].right and ball.top <= a['rect'].bottom and ball.bottom >= a['rect'].top: #good
                        balldirection = 'upright'
                        lockindirection = True

                if lockindirection == False and balldirection == 'upright':
                    if ball.top <= a['rect'].bottom and ball.bottom > a['rect'].bottom: #good
                        balldirection = 'downright'
                        lockindirection = True

                    if ball.right >= a['rect'].left and ball.left < a['rect'].left and ball.top <= a['rect'].bottom and ball.bottom >= a['rect'].top: #good
                        balldirection = 'upleft'
                        lockindirection = True


                if lockindirection == False and balldirection == 'downleft':
                    if ball.bottom >= a['rect'].top and ball.top < a['rect'].top: #good
                        balldirection = 'upleft'
                        lockindirection = True

                    if ball.left <= a['rect'].right and ball.right > a['rect'].right and ball.bottom >= a['rect'].top and ball.top <= a['rect'].bottom: #make more specific
                        balldirection = 'downright'
                        lockindirection = True

                if lockindirection == False and balldirection == 'downright':
                    if ball.bottom >= a['rect'].top and ball.top < a['rect'].top: #good, ACTUALLY ITS BAD LOL. Solved.
                        balldirection = 'upright'
                        lockindirection = True

                    if ball.right >= a['rect'].left and ball.left < a['rect'].left and ball.bottom >= a['rect'].top and ball.top <= a['rect'].bottom: #make more specific
                        balldirection = 'downleft'
                        lockindirection = True



        #erase block
        for a in armyofenemies:
            if a['rect'].top >= sheight:
                armyofenemies.remove(a)
                score2 += 1

                for w in hitted2:
                    if w == a['rect'].centerx:
                        hitted2.remove(w)

                if randomblockmode == True:
                    if a['rect'] == arandomblock:
                        if len(armyofenemies) > 0:
                            arandomblock = randomblockchoose((len(armyofenemies)/row)*(row-1))
                            freeze = arandomblock.centerx



        #moving individual block
        if randomblockmode == True:
            arandomblock.centerx = freeze
            if arandomblock.right < swidth or arandomblock.left > 0:
                arandomblock.centery += 1


        #falldown individual block
        for a in armyofenemies:
            if a['falldown'] == True:
                a['rect'].centerx = a['blockid']
       # for a in armyofenemies:
            #if a['blockid'] == a['rect'].centerx:
                a['rect'].centery += 1

        ##draw

        #draw laser
        for a in laserlist:
            randomcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            pygame.draw.rect(windowsurface, RED, a['rect'])

        #draw army
        for a in armyofenemies:
            pygame.draw.rect(windowsurface, a['color'], a['rect'])
            #windowsurface.blit(blocklabeler(a),a['rect'])

        coverforenemyrect1.centerx = enemyrect1.centerx
        #draw ball
        pygame.draw.rect(windowsurface, BLUE, ball)

        #draw player
        #windowsurface.blit(playerimage, playerrect)
        pygame.draw.rect(windowsurface, COLOR2, playerrect)

        #draw enemy
        #pygame.draw.rect(windowsurface, COLOR4, coverforenemyrect1)
        pygame.draw.rect(windowsurface, COLOR3, enemyrect1)

        #draw score


        #update game/configure fps
        pygame.display.update()
        mainClock.tick(60)
        if len(hitted2) >= 1:
            hitted2 = hitted2[1:]
        else:
            hitted2 = []


        for a in hitted2:
            if a > enemyrect1.bottom + (sheight * .2):
                hitted2.remove(a)
        continue



    #
    #pygame.display.update()
    #mainClock.tick(60)

        #continue


#idea: add speed to the ball if the bar is pushing it