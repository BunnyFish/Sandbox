import pygame
import math
import random
import copy

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSizeX = 1650
    surfaceSizeY = 900
    
    clock = pygame.time.Clock()  #Force frame rate to be slower
    
    frameCount = 0

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSizeX, surfaceSizeY))

    #-----------------------------Program Variable Initialization----------------------------#

    programState = "prestart"
    
    #button collision
    def distFromPoints(point1, point2):
        
        '''
        Collision between points

        This Function will get two points and their sizes and return the distance
            
        Paramaters 
        ----------
        point1: integers - first point
        point2: integers - second point

        Returns
        -------
        Integer
        '''
          
        distance = math.sqrt( ((point2[0]-point1[0])**2)+((point2[1]-point1[1])**2) )
        return distance

    #deletes block occupying a space where the player is trying to place a new block
    def replaceBlock():

        '''
        Deletes Blocks

        This function will check if the mouse position is ontop of a certain block
        and remove it from its list
          
          
        Paremeters
        ----------
        None

        Returns
        -------
        None
        '''
        for i in range(len(groundList)):
            if mousePos[0] > groundList[i][0] and mousePos[0] < groundList[i][0] +75 and mousePos[1] > groundList[i][1] and mousePos[1] < groundList[i][1] + 75:
                groundList.remove([blockPos[0], blockPos[1]])
                break
        for i in range(len(spikeList)):
            if mousePos[0] > spikeList[i][0] and mousePos[0] < spikeList[i][0] +75 and mousePos[1] > spikeList[i][1] and mousePos[1] < spikeList[i][1] + 75:
                spikeList.remove([blockPos[0], blockPos[1]])
                break
        for i in range(len(iceList)):
            if mousePos[0] > iceList[i][0] and mousePos[0] < iceList[i][0] +75 and mousePos[1] > iceList[i][1] and mousePos[1] < iceList[i][1] + 75:
                iceList.remove([blockPos[0], blockPos[1]])
                break
        for i in range(len(winList)):
            if mousePos[0] > winList[i][0] and mousePos[0] < winList[i][0] +75 and mousePos[1] > winList[i][1] and mousePos[1] < winList[i][1] + 75:
                winList.remove([blockPos[0], blockPos[1]])
                break
        for i in range(len(orbList)):
            if mousePos[0] > orbList[i][0] and mousePos[0] < orbList[i][0] +75 and mousePos[1] > orbList[i][1] and mousePos[1] < orbList[i][1] + 75:
                orbList.remove([blockPos[0], blockPos[1]])
                break
        for i in range(len(lockList)):
            if mousePos[0] > lockList[i][0] and mousePos[0] < lockList[i][0] +75 and mousePos[1] > lockList[i][1] and mousePos[1] < lockList[i][1] + 75:
                lockList.remove([blockPos[0], blockPos[1]])
                break
        for i in range(len(keyList)):
            if mousePos[0] > keyList[i][0] and mousePos[0] < keyList[i][0] +75 and mousePos[1] > keyList[i][1] and mousePos[1] < keyList[i][1] + 75:
                keyList.remove([blockPos[0], blockPos[1]])
                break
        for i in range(len(bounceList)):
            if mousePos[0] > bounceList[i][0] and mousePos[0] < bounceList[i][0] +75 and mousePos[1] > bounceList[i][1] and mousePos[1] < bounceList[i][1] + 75:
                bounceList.remove([blockPos[0], blockPos[1]])
                break
        for i in range(len(fallingList)):
            if mousePos[0] > fallingList[i][0] and mousePos[0] < fallingList[i][0] +75 and mousePos[1] > fallingList[i][1] and mousePos[1] < fallingList[i][1] + 75:
                fallingList.remove([blockPos[0], blockPos[1]])
                break
            
    #clears all block lists 
    def resetLevel():
        '''
        Level Reset

        This function clear every block list that contains items
              
        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        groundList.clear()
        spikeList.clear()
        iceList.clear()
        winList.clear()
        orbList.clear()
        lockList.clear()
        keyList.clear()
        bounceList.clear()
        fallingList.clear()
      
    #writes current block positions into text files
    def saveLevel():
        '''
        Level Save

        This function will place all of the string versions of the block lists
        into text files to be reimplemented into the code at a later time

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        fSw = open("startFile.txt", "w") 
        fSw.write(startString)
        fSw.close()
        
        fGw = open("groundFile.txt", "w") 
        fGw.write(groundString)
        fGw.close()
        
        fSw = open("spikeFile.txt", "w") 
        fSw.write(spikeString)
        fSw.close()
        
        fIw = open("iceFile.txt", "w") 
        fIw.write(iceString)
        fIw.close()
        
        fWw = open("winFile.txt", "w") 
        fWw.write(winString)
        fWw.close()
        
        fOw = open("orbFile.txt", "w") 
        fOw.write(orbString)
        fOw.close()
        
        fLw = open("lockFile.txt", "w") 
        fLw.write(lockString)
        fLw.close()
        
        fKw = open("keyFile.txt", "w") 
        fKw.write(keyString)
        fKw.close()
        
        fBw = open("bounceFile.txt", "w") 
        fBw.write(bounceString)
        fBw.close()
        
        fFw = open("fallingFile.txt", "w") 
        fFw.write(fallingString)
        fFw.close()
            
           
    def dead():
        '''
        Death Reset

        This function will reset certain variables upon player death

        Parameters
        ----------
        None

        Returns
        -------
        None
        '''
        playerPos[0] = startX
        playerPos[1] = startY
        playerSpeed[0] = 0
        playerSpeed[1] = 0
        
        onIce = False
        orbMove.clear()
        lockPlay.clear()
        keyPlay.clear()
        fallingPlay.clear()
        
    #colours
    RED = (255,0,0)
    GREEN = (0,255,0)
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    WHITE = (255,255,255)
   
    
    #start position
    startPos = []
    fSt = open("startFile.txt", "r")
    
    startString = fSt.readline()
    startString = startString.replace("[","")
    startString = startString.replace("]","")
    startString = startString.split(",")
    
    startX = int(startString[0])
    startY = int(startString[1])
    fSt.close()
    
    
    #player
    playerSize = [28,32]
    playerPos = pygame.Rect([startX,startY, 28, 32])  #X and Y Values
    prevPlayerPos = copy.copy(playerPos)
    playerSpeed = [0,0]
    playerGravity = 1
    accel = 5
    
    LHeld = False
    RHeld = False
    playerDirectionH = "right"
    jumpCount = 0
    
    #start menu
    titleFont = pygame.font.SysFont('Courier New', 125, True, False)
    titleText = titleFont.render('Sandbox', True, WHITE)
    startImg = pygame.image.load("images/start.jpg")
    startBackground = pygame.transform.scale(startImg, (1650,900))
    
    startColour = BLACK
    quitColour = BLACK
    
    buttonSize = 100
    quitSize = 50
    
    startButtonPos = [825, 550]
    quitButtonPos = [825, 750]
    
    menuFont = pygame.font.SysFont('Courier New', 25, True, False)
    playText = menuFont.render('Make/Play', True, WHITE)
    quitText = menuFont.render('Quit', True, WHITE)
    
    def startButton():
        pygame.draw.circle(mainSurface, startColour, startButtonPos, buttonSize)
        mainSurface.blit(playText, (startButtonPos[0]-65, startButtonPos[1]-10))
    
    
    def quitButton():
        pygame.draw.circle(mainSurface, quitColour, quitButtonPos, quitSize)
        mainSurface.blit(quitText, (quitButtonPos[0]-30, quitButtonPos[1]-8))
    
    
#sprites/images   
    #dino character
    dinoSpriteSheet = pygame.image.load("sprites/DinoSpriteSheet.png").convert_alpha()
    scale = 2
    dinoSpriteSheet = pygame.transform.smoothscale(dinoSpriteSheet, (scale*dinoSpriteSheet.get_width(),scale*dinoSpriteSheet.get_height())) 
    dinoSprite = [6*scale,4*scale,23*scale,20*scale]
    dinoRun = [101*scale,4*scale,24*scale,16*scale]
    dinoJump = [268*scale,4*scale,24*scale,16*scale]
    
    leftMoveSheet = pygame.transform.flip(dinoSpriteSheet, True, False)
    dinoSpriteLeft = [555*scale,4*scale,23*scale,20*scale]
    dinoRunLeft = [338*scale,4*scale,24*scale,16*scale]
    dinoJumpLeft = [293*scale,4*scale,14*scale,15*scale] 
    
    jumpUp = False
    
    #dino animation
    dinoPatchNumber = 0
    dinoNumPatches = 6
    dinoFrameRate = 4
    
    dinoLeftPatchNumber = 0
    dinoLeftNumPatches = 6
    dinoLeftFrameRate = 4
    
    #maker menu
    tabMenu = pygame.image.load("images/tab.png").convert()
    makeMenu = True
    
    grid = pygame.image.load("images/grid.png").convert_alpha()
    
    levelBackground = pygame.image.load("images/level.png").convert()

    
    #end screen
    endScreen = pygame.image.load("images/end.png").convert()
    
    #blocks
    blockType = ""
    playFont = pygame.font.SysFont('Courier New', 20, False, False)
    keyFont = pygame.font.SysFont('Courier New', 30, False, False)
    
    eraserSprite = pygame.image.load("sprites/eraser.png")
    eraserMouse = pygame.transform.scale(eraserSprite, (45,45))
    
    startSprite = pygame.image.load("sprites/start.png").convert_alpha()
    startMouse = pygame.transform.scale(startSprite, (50,50))
    
    groundSprite = pygame.image.load("sprites/ground.png")
    groundMouse = pygame.transform.scale(groundSprite, (25,25))
    
    spikeSprite = pygame.image.load("sprites/spike.png").convert_alpha()
    spikeMouse = pygame.transform.scale(spikeSprite, (25,25))
    
    iceSprite = pygame.image.load("sprites/ice.png")
    iceMouse = pygame.transform.scale(iceSprite, (25,25))
    onIce = False
    
    winSprite = pygame.image.load("sprites/win.png")
    winMouse = pygame.transform.scale(winSprite, (25,25))
    
    orbSpriteSheet = pygame.image.load("sprites/orb.png").convert_alpha()
    orbSprite = [0,0,75,75]
    orbMouse = pygame.image.load("sprites/orbMouse.png").convert_alpha()
    
    orbShoot = False
    orbPlayerPos = copy.copy(playerPos)
    orbSeconds = 0
   
    orbPatchNumber = 0
    orbNumPatches = 7
    orbFrameRate = 3
    
    lockSprite = pygame.image.load("sprites/lock.png")
    lockMouse = pygame.transform.scale(lockSprite, (25,25))
    locksEnabled = False
    
    keySprite = pygame.image.load("sprites/key.png").convert_alpha()
    keyMouse = pygame.transform.scale(keySprite, (25,25))
    keys = 0
    keyCount = pygame.transform.scale(keySprite, (50,50))
    keyText = keyFont.render(f'{keys}', True, RED)
    keysEnabled = False
    
    bounceSprite = pygame.image.load("sprites/bounce.png").convert_alpha()
    bounceMouse = pygame.transform.scale(bounceSprite, (25,25))
    onBounce = False
    
    fallingSprite = pygame.image.load("sprites/falling.png").convert_alpha()
    fallingMouse = pygame.transform.scale(fallingSprite, (25,25))
    fallingEnabled = False
    
    blockPos = [0,0]
   
#BLOCK LISTS + SAVING
    #open all block text files
    fGr = open("groundFile.txt", "r")
    fSp = open("spikeFile.txt", "r")
    fIc = open("iceFile.txt", "r")
    fWi = open("winFile.txt", "r")
    fOr = open("orbFile.txt", "r")
    fLo = open("lockFile.txt", "r")
    fKe = open("keyFile.txt", "r")
    fBo = open("bounceFile.txt", "r")
    fFa = open("fallingFile.txt", "r")
    
    #ground
    groundList = []
    groundString = fGr.readline()
    groundString = groundString.replace("[","")
    groundString = groundString.replace("]","")
    groundString = groundString.split(",")
    groundExist = False
    
    if len(groundString) > 1:
        groundExist = True
    
    if groundExist == True:
        for i in range(0,len(groundString),2):
            groundList.append([int(groundString[i]) , int(groundString[i+1])])
            
    #spikes        
    spikeList = []
    spikeString = fSp.readline()
    spikeString = spikeString.replace("[","")
    spikeString = spikeString.replace("]","")
    spikeString = spikeString.split(",")
    spikeExist = False
    
    if len(spikeString) > 1:
        spikeExist = True
    
    if spikeExist == True:
        for i in range(0,len(spikeString),2):
            spikeList.append([int(spikeString[i]) , int(spikeString[i+1])])
            
    #ice blocks        
    iceList = []
    iceString = fIc.readline()
    iceString = iceString.replace("[","")
    iceString = iceString.replace("]","")
    iceString = iceString.split(",")
    iceExist = False
    
    if len(iceString) > 1:
        iceExist = True
    
    if iceExist == True:
        for i in range(0,len(iceString),2):
            iceList.append([int(iceString[i]) , int(iceString[i+1])])
            
    #win blocks       
    winList = []
    winString = fWi.readline()
    winString = winString.replace("[","")
    winString = winString.replace("]","")
    winString = winString.split(",")
    winExist = False
    
    if len(winString) > 1:
        winExist = True
    
    if winExist == True:
        for i in range(0,len(winString),2):
            winList.append([int(winString[i]) , int(winString[i+1])])
    
    #orbs
    orbList = []
    orbString = fOr.readline()
    orbString = orbString.replace("[","")
    orbString = orbString.replace("]","")
    orbString = orbString.split(",")
    orbExist = False
    
    if len(orbString) > 1:
        orbExist = True
    
    if orbExist == True:
        for i in range(0,len(orbString),2):
            orbList.append([int(orbString[i]) , int(orbString[i+1])])
            
    orbMove = []
    
    #locks
    lockList = []
    lockString = fLo.readline()
    lockString = lockString.replace("[","")
    lockString = lockString.replace("]","")
    lockString = lockString.split(",")
    lockExist = False
    
    if len(lockString) > 1:
        lockExist = True
    
    if lockExist == True:
        for i in range(0,len(lockString),2):
            lockList.append([int(lockString[i]) , int(lockString[i+1])])
            
    lockPlay = []
    
    #keys
    keyList = []
    keyString = fKe.readline()
    keyString = keyString.replace("[","")
    keyString = keyString.replace("]","")
    keyString = keyString.split(",")
    keyExist = False
    
    if len(keyString) > 1:
        keyExist = True
    
    if keyExist == True:
        for i in range(0,len(keyString),2):
            keyList.append([int(keyString[i]) , int(keyString[i+1])])
            
    keyPlay = []
    
    #bounce blocks
    bounceList = []
    bounceString = fBo.readline()
    bounceString = bounceString.replace("[","")
    bounceString = bounceString.replace("]","")
    bounceString = bounceString.split(",")
    bounceExist = False
    
    if len(bounceString) > 1:
        bounceExist = True
    
    if bounceExist == True:
        for i in range(0,len(bounceString),2):
            bounceList.append([int(bounceString[i]) , int(bounceString[i+1])])
        
    #falling platform        
    fallingList = []
    fallingString = fFa.readline()
    fallingString = fallingString.replace("[","")
    fallingString = fallingString.replace("]","")
    fallingString = fallingString.split(",")
    fallingExist = False
    
    if len(fallingString) > 1:
        fallingExist = True
    
    if fallingExist == True:
        for i in range(0,len(fallingString),2):
            fallingList.append([int(fallingString[i]) , int(fallingString[i+1])])
            
    fallingPlay = []
    
    #close all block text files 
    fGr.close()
    fSp.close()
    fIc.close()
    fWi.close()
    fOr.close()
    fLo.close()
    fKe.close()
    fBo.close()
    fFa.close()
    
   
    
    #-----------------------------Main Program Loop---------------------------------------------#
    while True:
        mousePos = pygame.mouse.get_pos()
        
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        
        #start
        if programState == "prestart":
            programState = "start"
        #start menu
        if programState == "start":

            mainSurface.blit(startBackground, (0,0))
            mainSurface.blit(titleText, (125, 35))
            
            startButton()
            quitButton()
            #button collision
            
            if distFromPoints(startButtonPos, mousePos) < (buttonSize):
                startColour = RED
            else:
                startColour = BLACK
                
            if ev.type == pygame.MOUSEBUTTONDOWN and distFromPoints(startButtonPos, mousePos) < (buttonSize):
                programState = "make"


            if distFromPoints(quitButtonPos, mousePos) < (quitSize):
                quitColour = RED
            else:
                quitColour = BLACK
            
            if ev.type == pygame.MOUSEBUTTONDOWN and distFromPoints(quitButtonPos, mousePos) < (quitSize):
                click.play()
                break
                
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE: 
                    break
        
        #level editor
        if programState == "make":
            
            mainSurface.blit(levelBackground,(0,0))
            mainSurface.blit(grid,(0,0))
            
            #character
            mainSurface.blit(dinoSpriteSheet, playerPos, dinoSprite)
            playerPos[0] = startX
            playerPos[1] = startY
            
            mousePos = pygame.mouse.get_pos()
            
            
            
            #block selection
            if ev.type == pygame.KEYDOWN:
                
                if ev.key == pygame.K_BACKSPACE:
                    blockType = "delete"
                if ev.key == pygame.K_1:
                    blockType = "ground"
                if ev.key == pygame.K_2:
                    blockType = "spike"
                if ev.key == pygame.K_3:
                    blockType = "ice"
                if ev.key == pygame.K_4:
                    blockType = "win"
                if ev.key == pygame.K_5:
                    blockType = "orb"
                if ev.key == pygame.K_6:
                    blockType = "lock"
                if ev.key == pygame.K_7:
                    blockType = "key"
                if ev.key == pygame.K_8:
                    blockType = "bounce"
                if ev.key == pygame.K_9:
                    blockType = "falling"
                    
                #switch to gameplay mode
                if ev.key == pygame.K_SPACE: 
                    programState = "play"                        
                    orb_ticks = pygame.time.get_ticks()
                    locksEnabled = True
                    keysEnabled = True
                    fallingEnabled = True
                    keys = 0
                    keyText = keyFont.render(f'{keys}', True, RED)
                    mainSurface.blit(keyText, (50,50))
                    
                if ev.key == pygame.K_r:
                    resetLevel()
                    startX = 110
                    startY = 793
                
                if ev.key == pygame.K_RSHIFT:
                    startPos = [startX,startY]
                    startString = str(startPos)
                    groundString = str(groundList)
                    spikeString = str(spikeList)
                    iceString = str(iceList)
                    winString = str(winList)
                    orbString = str(orbList)
                    lockString = str(lockList)
                    keyString = str(keyList)
                    bounceString = str(bounceList)
                    fallingString = str(fallingList) 
                    saveLevel()
                    
                if ev.key == pygame.K_RETURN:
                    blockType = "start"
                
                if ev.key == pygame.K_TAB and makeMenu == False:
                    makeMenu = True
                
                elif ev.key == pygame.K_TAB and makeMenu == True:
                    makeMenu = False
                
                #back to menu
                if ev.key == pygame.K_ESCAPE: 
                        programState = "prestart"
                        blockType = ""
                    
            
            #block placement/deletion
            if ev.type == pygame.MOUSEBUTTONDOWN:
                
                
                
                #x position (75 square grid)
                if mousePos[0] < 75:
                    blockPos[0] = 0
                elif mousePos[0] > 75 and mousePos[0] < 150:
                    blockPos[0] = 75
                elif mousePos[0] > 150 and mousePos[0] < 225:
                    blockPos[0] = 150
                elif mousePos[0] > 225 and mousePos[0] < 300:
                    blockPos[0] = 225
                elif mousePos[0] > 300 and mousePos[0] < 375:
                    blockPos[0] = 300
                elif mousePos[0] > 375 and mousePos[0] < 450:
                    blockPos[0] = 375
                elif mousePos[0] > 450 and mousePos[0] < 525:
                    blockPos[0] = 450
                elif mousePos[0] > 525 and mousePos[0] < 600:
                    blockPos[0] = 525
                elif mousePos[0] > 600 and mousePos[0] < 675:
                    blockPos[0] = 600
                elif mousePos[0] > 675 and mousePos[0] < 750:
                    blockPos[0] = 675
                elif mousePos[0] > 750 and mousePos[0] < 825:
                    blockPos[0] = 750
                elif mousePos[0] > 825 and mousePos[0] < 900:
                    blockPos[0] = 825
                elif mousePos[0] > 900 and mousePos[0] < 975:
                    blockPos[0] = 900
                elif mousePos[0] > 975 and mousePos[0] < 1050:
                    blockPos[0] = 975
                elif mousePos[0] > 1050 and mousePos[0] < 1125:
                    blockPos[0] = 1050
                elif mousePos[0] > 1125 and mousePos[0] < 1200:
                    blockPos[0] = 1125
                elif mousePos[0] > 1200 and mousePos[0] < 1275:
                    blockPos[0] = 1200
                elif mousePos[0] > 1275 and mousePos[0] < 1350:
                    blockPos[0] = 1275
                elif mousePos[0] > 1350 and mousePos[0] < 1425:
                    blockPos[0] = 1350
                elif mousePos[0] > 1425 and mousePos[0] < 1500:
                    blockPos[0] = 1425
                elif mousePos[0] > 1500 and mousePos[0] < 1575:
                    blockPos[0] = 1500
                elif mousePos[0] > 1575 and mousePos[0] < 1650:
                    blockPos[0] = 1575
                    
                #y position (75 square grid)
                if mousePos[1] < 75:
                    blockPos[1] = 0
                elif mousePos[1] > 75 and mousePos[1] < 150:
                    blockPos[1] = 75
                elif mousePos[1] > 150 and mousePos[1] < 225:
                    blockPos[1] = 150
                elif mousePos[1] > 225 and mousePos[1] < 300:
                    blockPos[1] = 225
                elif mousePos[1] > 300 and mousePos[1] < 375:
                    blockPos[1] = 300
                elif mousePos[1] > 375 and mousePos[1] < 450:
                    blockPos[1] = 375
                elif mousePos[1] > 450 and mousePos[1] < 525:
                    blockPos[1] = 450
                elif mousePos[1] > 525 and mousePos[1] < 600:
                    blockPos[1] = 525
                elif mousePos[1] > 600 and mousePos[1] < 675:
                    blockPos[1] = 600
                elif mousePos[1] > 675 and mousePos[1] < 750:
                    blockPos[1] = 675
                elif mousePos[1] > 750 and mousePos[1] < 825:
                    blockPos[1] = 750
                elif mousePos[1] > 825 and mousePos[1] < 900:
                    blockPos[1] = 825

                #block placement
                if blockType == "ground":
                    replaceBlock()
                    groundList.append([blockPos[0], blockPos[1]])
                   
                    click.play()
                    
                elif blockType == "spike":
                    replaceBlock()
                    spikeList.append([blockPos[0], blockPos[1]])
                    
                    click.play()
                    
                elif blockType == "ice":
                    replaceBlock()
                    iceList.append([blockPos[0], blockPos[1]])
                    
                    click.play()
                
                elif blockType == "win":
                    replaceBlock()
                    winList.append([blockPos[0], blockPos[1]])
                    
                    click.play()
                    
                elif blockType == "orb":
                    replaceBlock()
                    orbList.append([blockPos[0], blockPos[1]])
                    
                    click.play()
                
                elif blockType == "lock":
                    replaceBlock()
                    lockList.append([blockPos[0], blockPos[1]])
                    
                    click.play()
                
                elif blockType == "key":
                    replaceBlock()
                    keyList.append([blockPos[0], blockPos[1]])
                    
                    click.play()
                    
                elif blockType == "bounce":
                    replaceBlock()
                    bounceList.append([blockPos[0], blockPos[1]])
                    
                    click.play()
                
                elif blockType == "falling":
                    replaceBlock()
                    fallingList.append([blockPos[0], blockPos[1]])
                    
                    click.play()
                    
                elif blockType == "start":
                    replaceBlock()
                    startX = blockPos[0] + 35
                    startY = blockPos[1] +43
                    
                    click.play()
                
                elif blockType == "delete":
                    replaceBlock()
                   
                    click.play()
        
            #drawing images       
            for i in range(len(groundList)):
                #draws ground sprites
                mainSurface.blit(groundSprite, groundList[i])
            
            for i in range(len(spikeList)):
                #draws spike sprites
                mainSurface.blit(spikeSprite, spikeList[i])
                
            for i in range(len(iceList)):
                #draws ice sprites
                mainSurface.blit(iceSprite, iceList[i])
            
            for i in range(len(winList)):
                #draws win block sprites
                mainSurface.blit(winSprite, winList[i])
            
            orbMove.clear()
            for i in range(len(orbList)):
                #draws orb sprites
                mainSurface.blit(orbSpriteSheet, orbList[i], orbSprite)
            
            lockPlay.clear()
            for i in range(len(lockList)):
                #draws lock sprites
                mainSurface.blit(lockSprite, lockList[i])
            
            keyPlay.clear()
            for i in range(len(keyList)):
                #draws key sprites
                mainSurface.blit(keySprite, keyList[i])
                
            for i in range(len(bounceList)):
                #draws bounce sprites
                mainSurface.blit(bounceSprite, bounceList[i])
            
            fallingPlay.clear()
            for i in range(len(fallingList)):
                #draws bounce sprites
                mainSurface.blit(fallingSprite, fallingList[i])
                
            #tab menu to see what blocks require what button                
            if makeMenu == True:
                mainSurface.blit(tabMenu,(0,0))
                
            #block selected displays at mouse location
            if blockType == "delete":
                mainSurface.blit(eraserMouse,(mousePos[0]-23,mousePos[1]-22))
            elif blockType == "start":
                mainSurface.blit(startMouse,(mousePos[0]-20,mousePos[1]-20))
            elif blockType == "ground":
                mainSurface.blit(groundMouse,(mousePos[0]-13,mousePos[1]-12))
            elif blockType == "spike":
                mainSurface.blit(spikeMouse,(mousePos[0]-13,mousePos[1]-12))
            elif blockType == "ice":
                mainSurface.blit(iceMouse,(mousePos[0]-13,mousePos[1]-12))
            elif blockType == "win":
                mainSurface.blit(winMouse,(mousePos[0]-13,mousePos[1]-12))
            elif blockType == "orb":
                mainSurface.blit(orbMouse,(mousePos[0]-13,mousePos[1]-12))
            elif blockType == "lock":
                mainSurface.blit(lockMouse,(mousePos[0]-13,mousePos[1]-12))
            elif blockType == "key":
                mainSurface.blit(keyMouse,(mousePos[0]-13,mousePos[1]-12))
            elif blockType == "bounce":
                mainSurface.blit(bounceMouse,(mousePos[0]-13,mousePos[1]-12))
            elif blockType == "falling":
                mainSurface.blit(fallingMouse,(mousePos[0]-13,mousePos[1]-12))
                
        #gameplay
        if programState == "play":

            mainSurface.blit(levelBackground,(0,0))
            
            #character
            prevPlayerPos = copy.copy(playerPos)
            #controls/movement
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_LEFT:
                    playerSpeed[0] -= accel
                    LHeld = True
                    playerDirectionH = "left"
                    
                elif ev.key == pygame.K_RIGHT:
                    playerSpeed[0] += accel
                    RHeld = True
                    playerDirectionH = "right"
                    
                if ev.key == pygame.K_UP:
                    #double jump check and bounce check
                    if jumpCount < 2 and onBounce == True:
                        playerPos[1] -= 1
                        playerSpeed[1] = -30
                        jumpCount += 1
                        onBounce = False
                        
                
                    elif jumpCount < 2 and onBounce == False:
                        playerPos[1] -= 1
                        playerSpeed[1] = -18
                        jumpCount += 1
                        
                    
                if ev.key == pygame.K_ESCAPE: 
                    programState = "make"                    
                    playerDirectionH = "right"
                    dead()
                    
                
           
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_LEFT and playerSpeed[0] <= 0:
                    playerSpeed[0] += accel
                    LHeld = False
                    
                if ev.key == pygame.K_RIGHT and playerSpeed[0] >= 0:
                    playerSpeed[0] -= accel
                    RHeld = False
            
            if LHeld == False and RHeld == False and onIce == False:
                playerSpeed[0] = 0
            
            if playerSpeed[0] == 0:
                LHeld = False
                RHeld = False
                    

             
            #-----------------------------Program Logic---------------------------------------------#
            # Update your game objects and data structures here...
            
            
            prevPlayerPos = copy.copy(playerPos)
            playerPos[0] += playerSpeed[0]
            playerPos[1] += playerSpeed[1]
            playerSpeed[1] += playerGravity
            
            
            #ice physics
            if onIce == True:
                if playerSpeed[0] == 5:
                    playerSpeed[0] = 10
                elif playerSpeed[0] == -5:
                    playerSpeed[0] = -10
                            
            if onIce == False:
                if playerSpeed[0] < -5:
                    if LHeld == True:
                        playerSpeed[0] = -5
                    else:
                        playerSpeed[0] = 0
                if playerSpeed[0] > 5:
                    if RHeld == True:
                        playerSpeed[0] = 5
                    else:
                        playerSpeed[0] = 0
                if RHeld == False and LHeld == False:
                    playerSpeed[0] 
        
            #bounce physics
            if onBounce == True and playerSpeed[1] > 2:
                onBounce = False
        
        
            #terminal velocity
            if playerSpeed[1] == 20:
                playerSpeed[1] = 20
            if playerSpeed[0] > 10:
                playerSpeed[0] = 10
            if playerSpeed[0] < -10:
                playerSpeed[0] = -10
            
            #screen barrier
            if playerPos[0] < 0:
                playerSpeed[0] = 0
                playerPos[0] += 5
                onIce = False
                
            elif playerPos[0] + playerPos[2] > surfaceSizeX:
                playerSpeed[0] = 0
                playerPos[0] -= 5
                onIce = False
            #below screen death
            if playerPos[1] > surfaceSizeY:
                dead()
                jumpCount = 0
                orb_ticks = pygame.time.get_ticks()
                keys = 0
                locksEnabled = True
                keysEnabled = True
                fallingEnabled = True
                playerDirectionH = "right"
            
            #roof barrier
            elif playerPos[1] < 0:
                playerSpeed[1] = 0
                playerPos[1] += 5
                
            
            #block collision/interaction
            for i in range(len(groundList)):
                #draws ground sprites
                mainSurface.blit(groundSprite, groundList[i])
                
                groundDimensions = [groundList[i][0],groundList[i][1],75,75]
                groundRect = pygame.Rect(groundDimensions)
                #block collision
                
                if playerPos.colliderect(groundRect):
                  
                    #top
                    if prevPlayerPos[1] < groundList[i][1]  and prevPlayerPos[1]+prevPlayerPos[3]-5 <= groundList[i][1]: 
                        playerGravity = 0
                        playerSpeed[1] = 0
                        playerPos[1] = groundList[i][1]-playerPos[3]
                        jumpCount = 0  
                        onIce = False
                        onBounce = False
                        
                    #right
                    elif prevPlayerPos[0] >= groundList[i][0] +75:
                        playerPos[0] = groundList[i][0] + 75
                        jumpCount = 0
                        onIce = False
                        onBounce = False
                    #left
                    elif prevPlayerPos[0] <= groundList[i][0] and prevPlayerPos[1] < groundList[i][1]+75:
                        playerPos[0] = groundList[i][0] - playerPos[2]
                        jumpCount = 0
                        onIce = False
                        onBounce = False
                    #bottom    
                    else:
                        playerPos[1] = groundList[i][1]+75
                        playerSpeed[1] = 0
                        playerGravity = 1
                        
                else:
                    playerGravity = 1
            
            
            for i in range(len(spikeList)):
                #draws spike sprites
                mainSurface.blit(spikeSprite, spikeList[i])
                
                #spike collision
                if playerPos[1] + playerSize[1] > spikeList[i][1] + 5 and playerPos[1] < spikeList[i][1] + 70 and playerPos[0] < spikeList[i][0] + 70 and playerPos[0] + playerSize[0] > spikeList[i][0] +5:
                    dead()
                    jumpCount = 0
                    
                    orb_ticks = pygame.time.get_ticks()
                    keys = 0
                    locksEnabled = True
                    keysEnabled = True
                    fallingEnabled = True
                    playerDirectionH = "right"
                    
                    
            
            for i in range(len(iceList)):
                #draws ice sprites
                mainSurface.blit(iceSprite, iceList[i])
                
                iceDimensions = [iceList[i][0],iceList[i][1],75,75]
                iceRect = pygame.Rect(iceDimensions)
                
                if playerPos.colliderect(iceRect):
                    #top
                    if prevPlayerPos[1] < iceList[i][1]  and prevPlayerPos[1]+prevPlayerPos[3]-5 <= iceList[i][1]: 
                        playerGravity = 0
                        playerSpeed[1] = 0
                        playerPos[1] = iceList[i][1]-playerPos[3]
                        jumpCount = 0
                        
                        onBounce = False
                        
                        if playerSpeed[0] != 0:
                            onIce = True
                        
                    #right
                    elif prevPlayerPos[0] >= iceList[i][0] +75:
                        playerPos[0] = iceList[i][0] + 75
                        jumpCount = 0
                        onIce = False
                        onBounce = False
                    #left
                    elif prevPlayerPos[0] <= iceList[i][0] and prevPlayerPos[1] < iceList[i][1]+75:
                        playerPos[0] = iceList[i][0] - playerPos[2]
                        jumpCount = 0
                        onIce = False
                        onBounce = False
                        
                    #bottom    
                    else:
                        playerPos[1] = iceList[i][1]+75
                        playerSpeed[1] = 0
                        playerGravity = 1
                        
                else:
                    playerGravity = 1
        
                
            for i in range(len(winList)):
                #draws win platform sprites
                mainSurface.blit(winSprite, winList[i])
            
                winDimensions = [winList[i][0],winList[i][1],75,75]
                winRect = pygame.Rect(winDimensions)
                
                if playerPos.colliderect(winRect):
                    #top
                    if prevPlayerPos[1] < winList[i][1]  and prevPlayerPos[1]+prevPlayerPos[3]-5 <= winList[i][1]: 
                        playerGravity = 0
                        playerSpeed[1] = 0
                        playerPos[1] = winList[i][1]-playerPos[3]
                        jumpCount = 0
                        
                        dead()
                        programState = "win"

                        onIce = False
                        onBounce = False
                        
                
                        
                    #right
                    elif prevPlayerPos[0] >= winList[i][0] +75:
                        playerPos[0] = winList[i][0] + 75
                        jumpCount = 0
                        
                        onIce = False
                        onBounce = False
                        
                    #left
                    elif prevPlayerPos[0] <= winList[i][0] and prevPlayerPos[1] < winList[i][1]+75:
                        playerPos[0] = winList[i][0] - playerPos[2]
                        jumpCount = 0
                        
                        onIce = False
                        onBounce = False
                        
                    #bottom    
                    else:
                        playerPos[1] = winList[i][1]+75
                        playerSpeed[1] = 0
                        playerGravity = 1
                        
                else:
                    playerGravity = 1
                    
            
            orbSeconds = int((pygame.time.get_ticks()-orb_ticks)/1000)
            
            if orbSeconds > 10:
                orbMove.clear()
                orbPlayerPos = copy.copy(playerPos)
                orb_ticks = pygame.time.get_ticks()
                orbShoot = True
                
            for i in range(len(orbList)):
                #orb animation
                if (frameCount % orbFrameRate == 0):
                    if (orbPatchNumber < orbNumPatches-1) :
                        orbPatchNumber += 1
                        orbSprite[0] += orbSprite[2]  
                    else:
                        orbPatchNumber = 0           
                        orbSprite[0] -= orbSprite[2]*(orbNumPatches-1)  
                #draws orbs   
                mainSurface.blit(orbSpriteSheet, orbList[i], orbSprite)
                        
                #orb collision
                if playerPos[1] + playerSize[1] > orbList[i][1] + 10 and playerPos[1] < orbList[i][1] + 65 and playerPos[0] < orbList[i][0] + 65 and playerPos[0] + playerSize[0] > orbList[i][0] +10:
                    dead()
                    jumpCount = 0
                    
                    orb_ticks = pygame.time.get_ticks()
                    keys = 0
                    locksEnabled = True
                    keysEnabled = True
                    fallingEnabled = True
                    playerDirectionH = "right"
                
                if orbShoot == True:
                    for j in range(len(orbList)):
                        orbMove.append([orbList[j][0], orbList[j][1]])
                    orbShoot = False
            
            #appends locked blocks into list that can be reset at death or entering make mode
            if locksEnabled == True:
                for j in range(len(lockList)):
                    lockPlay.append([lockList[j][0], lockList[j][1]])
                locksEnabled = False
                   
            for i in range(len(lockPlay)):
                #draws lock sprites
                mainSurface.blit(lockSprite, lockPlay[i])
                
                lockDimensions = [lockPlay[i][0],lockPlay[i][1],75,75]
                lockRect = pygame.Rect(lockDimensions)
                
                #unlocking lock 
                if playerPos.colliderect(lockRect):
                    if keys > 0:
                        lockPlay.remove([lockPlay[i][0],lockPlay[i][1]])
                        keys -= 1
                        break
                    #collision without a key    
                    else:
                        #top
                        if prevPlayerPos[1] < lockPlay[i][1]  and prevPlayerPos[1]+prevPlayerPos[3]-5 <= lockPlay[i][1]: 
                            playerGravity = 0
                            playerSpeed[1] = 0
                            playerPos[1] = lockPlay[i][1]-playerPos[3]
                            jumpCount = 0  
                            onIce = False
                            onBounce = False
                             
                        #right
                        elif prevPlayerPos[0] >= lockPlay[i][0] +75:
                            playerPos[0] = lockPlay[i][0] + 75
                            jumpCount = 0
                            onIce = False
                            onBounce = False
                        #left
                        elif prevPlayerPos[0] <= lockPlay[i][0] and prevPlayerPos[1] < lockPlay[i][1]+75:
                            playerPos[0] = lockPlay[i][0] - playerPos[2]
                            jumpCount = 0
                            onIce = False
                            onBounce = False
                        #bottom    
                        else:
                            playerPos[1] = lockPlay[i][1]+75
                            playerSpeed[1] = 0
                            playerGravity = 1
                            
                else:
                    playerGravity = 1        
                
                
            #appends locked blocks into list that can be reset at death or entering make mode
            if keysEnabled == True:
                for j in range(len(keyList)):
                    keyPlay.append([keyList[j][0], keyList[j][1]])
                keysEnabled = False
                   
            for i in range(len(keyPlay)):
                #draws key sprites
                mainSurface.blit(keySprite, keyPlay[i])
                
                keyDimensions = [keyPlay[i][0],keyPlay[i][1],75,75]
                keyRect = pygame.Rect(keyDimensions)
                #key collision
                
                if playerPos.colliderect(keyRect):
                    keyPlay.remove([keyPlay[i][0],keyPlay[i][1]])
                    keys += 1
                    keyText = keyFont.render(f'{keys}', True, RED)
                    break
            
            
            for i in range(len(bounceList)):
                #draws ground sprites
                mainSurface.blit(bounceSprite, bounceList[i])
                
                bounceDimensions = [bounceList[i][0],bounceList[i][1],75,75]
                bounceRect = pygame.Rect(bounceDimensions)
                #block collision
                
                if playerPos.colliderect(bounceRect):
                  
                    #top
                    if prevPlayerPos[1] < bounceList[i][1]  and prevPlayerPos[1]+prevPlayerPos[3]-5 <= bounceList[i][1]: 
                        playerGravity = 0
                        playerSpeed[1] = 0
                        playerPos[1] = bounceList[i][1]-playerPos[3]
                        jumpCount = 0  
                        onIce = False
                        onBounce = True
                        
                    #right
                    elif prevPlayerPos[0] >= bounceList[i][0] +75:
                        playerPos[0] = bounceList[i][0] + 75
                        jumpCount = 0
                        onIce = False
                        
                    #left
                    elif prevPlayerPos[0] <= bounceList[i][0] and prevPlayerPos[1] < bounceList[i][1]+75:
                        playerPos[0] = bounceList[i][0] - playerPos[2]
                        jumpCount = 0
                        onIce = False
                    #bottom    
                    else:
                        playerPos[1] = bounceList[i][1]+75
                        playerSpeed[1] = 0
                        playerGravity = 1
                        
                else:
                    playerGravity = 1
            

            #appends locked blocks into list that can be reset at death or entering make mode
            if fallingEnabled == True:
                for j in range(len(fallingList)):
                    fallingPlay.append([fallingList[j][0], fallingList[j][1], False])
                fallingEnabled = False
                   
            for i in range(len(fallingPlay)):
                #draws lock sprites
                mainSurface.blit(fallingSprite, (fallingPlay[i][0], fallingPlay[i][1]))
                
                fallingDimensions = [fallingPlay[i][0],fallingPlay[i][1],75,75]
                fallingRect = pygame.Rect(fallingDimensions)
                
                if playerPos.colliderect(fallingRect):
                    
                    #top
                    if prevPlayerPos[1] < fallingPlay[i][1]  and prevPlayerPos[1]+prevPlayerPos[3]-5 <= fallingPlay[i][1] and playerSpeed[1] > 0: 
                        playerGravity = 0
                        playerSpeed[1] = 0
                        playerPos[1] = fallingPlay[i][1]-playerPos[3]
                        jumpCount = 0
                        fallingPlay[i][2] = True
                        onIce = False
                        onBounce = False
                        
                else:
                    playerGravity = 1
                
                #platform falls after touched
                if fallingPlay[i][2] == True:
                    fallingPlay[i][1] += 2
                if fallingPlay[i][1] > surfaceSizeY+10:
                    fallingPlay.remove(fallingPlay[i])
                    break
                
                    
            #key orbs being shot from orb
            for i in range(len(orbMove)):
    
                #draws orbs   
                mainSurface.blit(orbSpriteSheet, orbMove[i], orbSprite)
                
                #orb movement
                if orbPlayerPos[0] < orbList[i][0]+30:
                    orbMove[i][0] -= 4
                    
                elif orbPlayerPos[0] > orbList[i][0]+30:
                    orbMove[i][0] += 4
                 
                
                #orb collision
                if playerPos[1] + playerSize[1] > orbMove[i][1] + 10 and playerPos[1] < orbMove[i][1] + 65 and playerPos[0] < orbMove[i][0] + 65 and playerPos[0] + playerSize[0] > orbMove[i][0] +10:
                    dead()
                    jumpCount = 0
                    
                    orb_ticks = pygame.time.get_ticks()
                    keys = 0
                    locksEnabled = True
                    keysEnabled = True
                    fallingEnabled = True
                    playerDirectionH = "right"
                    break
            
            

        #-----------------------------Drawing Everything-------------------------------------#
        #character animation
            if playerSpeed[1] < 0:
                jumpUp = True
            else:
                jumpUp = False  
                    
            if jumpUp == True:
                if playerDirectionH == "right":
                    mainSurface.blit(dinoSpriteSheet, playerPos, dinoJump)
                elif playerDirectionH == "left":
                    mainSurface.blit(leftMoveSheet, playerPos, dinoJumpLeft)
                    
            
            #right running animation
            elif RHeld == True and LHeld == False:  
                
                if (frameCount % dinoFrameRate == 0):    
                    if (dinoPatchNumber < dinoNumPatches-1) :
                        dinoPatchNumber += 1
                        dinoRun[0] += dinoRun[2] 
                    else:
                        dinoPatchNumber = 0         
                        dinoRun[0] -= dinoRun[2]*(dinoNumPatches-1) 
            
            
                mainSurface.blit(dinoSpriteSheet, playerPos, dinoRun)
            
            #left running animation
            elif RHeld == False and LHeld == True:
                if (frameCount % dinoLeftFrameRate == 0):    
                    if (dinoLeftPatchNumber < dinoLeftNumPatches-1) :
                        dinoLeftPatchNumber += 1
                        dinoRunLeft[0] += dinoRunLeft[2] 
                    else:
                        dinoLeftPatchNumber = 0           
                        dinoRunLeft[0] -= dinoRunLeft[2]*(dinoLeftNumPatches-1)  
               
                mainSurface.blit(leftMoveSheet, playerPos, dinoRunLeft)
            
            else:
                #facing right sprite
                if playerDirectionH == "right":
                    mainSurface.blit(dinoSpriteSheet, playerPos, dinoSprite)
                #facing left sprite
                elif playerDirectionH == "left":
                    mainSurface.blit(leftMoveSheet, playerPos, dinoSpriteLeft)
            
            #key counter
            mainSurface.blit(keyCount, (0,0))
            keyText = keyFont.render(f'{keys}', True, RED)
            mainSurface.blit(keyText, (35,25))
            
        #win screen   
        if programState == "win":
            mainSurface.blit(endScreen,(0,0))
            
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE: 
                    programState = "make"
            
                            
        
        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()
        frameCount += 1;
    
        clock.tick(60) #Force frame rate to be slower


    pygame.quit()     # Once we leave the loop, close the window.

main() 