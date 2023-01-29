import random

global playerX
global playerVelX
global moving
global ballX
global ballY
global ballZ
global ballVelX
global ballVelY
global ballVelZ
global aiX

playerSpeed = 1
gravity = .0001
playerPower = 7
fallAccel= 1.00001

player_x = 400
player_y = 100

cloud2_x=400
cloud2_y=200

cloud_dy=0
cloud_x=400
cloud_y=200
ground_x=0
ground_y=-3000
cloudDistance= 300
GameMode="none"

gameEnd=False

dy_ground = 2
player_dx = 0
player_dy=0

circlex = 100
circley = 480
col1 = 150
col2 = 210
col3 = 260
col4 = 320
col5 = 370
col6 = 420
col7 = 480
col8 = 530
col9 = 590
col10 = 640
row1 = 120
row2 = 160
row3 = 200
row4 = 240
row5 = 280
row6 = 320
row7 = 365
row8 = 400
row9 = 440
row10 = 480
ccol = 0
crow = 10
rightstate = 0
upstate = 0
leftstate = 0
downstate = 0

menuEnabled = True

def setup():
    global player, ground, cloud_x, cloud_y, cloud, cloud2, cloud2_y, cloud_x2, menuEnabled, menuBack, maze,playerX, moving, ballX, ballY, ballZ, ballVelX, ballVelY, ballVelZ, aiX, playerMaya
    player = loadImage("parachuter.png")
    ground=loadImage("finalMaccuPicchu.png")
    cloud=loadImage("New Project.jpeg")
    cloud2=loadImage("New Project.jpeg")
    menuBack=loadImage("MenuBack.png")
    maze = loadImage("maze.jpeg")
    playerMaya= loadImage("pixil-frame-0 (3) copy.png")
    
    moving = False
    playerX = 450
    global playerVelX
    playerVelX = 0
    ballX = 500
    ballY = 0
    ballZ = 250
    ballVelX = 0
    ballVelY = 0
    ballVelZ = 5.1
    aiX = 100
    #var loadImage 
    size(800,600)
    
    cloud_y=-200

    
    
def draw():
    global GameMode, menuEnabled, player_x, player_y, ground_x, ground_y,dy_ground, player_dx, player_dy, cloud_y, cloud_x, gameEnd, cloud2_y, cloud2_x, playerPower, ccol, crow, circlex, circley
    
    #print( mouseX, mouseY)
    
    if menuEnabled == True:
        image(menuBack, 0,-150,800,800)
        DrawMenu(100,100,0)
        DrawMenu(300,100,1)
        DrawMenu(500,100,2)
        DrawMenu(700,100,3)
        DrawMenu(100,200,4)
        DrawMenu(300,200,5)
        DrawMenu(500,200,6)
        Words("7 Wonders of the world",400,300,40)
        
        


        
    
    if menuEnabled == True:
        #GameMode == "none"
        if checkCollision(mouseX, mouseY, 1,1,100,100, 100, 20) == True and mousePressed:
            print("changed GameMode")
            GameMode = "Machu"
            menuEnabled == False
        if checkCollision(mouseX, mouseY, 1,1,300,100, 100, 20) == True and mousePressed:
            print("changed GameMode")
            GameMode = "Chichen"
            menuEnabled == False
            global playerX, moving, ballX, ballY, ballZ, ballVelX, ballVelY, ballVelZ, aiX
            moving = False
            playerX = 450
            global playerVelX
            playerVelX = 0
            ballX = 500
            ballY = 0
            ballZ = 250
            ballVelX = 0
            ballVelY = 0
            ballVelZ = 5.1
            aiX = 100
            #var loadImage 
            #size(800,600)
        if checkCollision(mouseX, mouseY, 1,1,700,100, 100, 20) == True and mousePressed:
            print("changed GameMode")
            GameMode = "Petra"
            ccol = 0
            crow = 10
            circlex = 100
            circley = 480
            menuEnabled == False
    
    
    
    if GameMode == "Machu":
        FallingGame()
    if GameMode == "Chichen":
        #Game
        Mayangame()
    # if GameMode == "Redeemer":
    #     #game
    if GameMode == "Petra":
        MazeGame()
        
    
    
    
    
def keyPressed():
    global player_dx, ccol, crow, playerVelX, moving
    if key==CODED:
        if keyCode == RIGHT:
            player_dx = playerPower
        if keyCode == LEFT:
            player_dx = -playerPower
    if keyCode == RIGHT and rightstate == 0:
        ccol += 1
    if keyCode == LEFT and leftstate == 0:
        ccol -= 1
    if keyCode == UP and upstate == 0:
        crow -= 1
    if keyCode == DOWN and downstate == 0:
        crow += 1
    if key == CODED:
        moving = True
            
def keyReleased():
    global player_dx, moving
    player_dx = 0
    moving = False
            
def checkCollision(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1+w1 > x2 and x1 < x2 + w2 and y1+h1 > y2 and y1 < y2 + h2

def FallingGame():
    global player_x, player_y, ground_x, ground_y,dy_ground, player_dx, player_dy, cloud_y, cloud_x, gameEnd, cloud2_y, cloud2_x, playerPower, menuEnabled
    while gameEnd == True:
        a = 1
        #print("over")
        menuEnabled = True
        
    if ground_y < -7400:
        dy_ground=0
        player_dy=5
        if player_y > 520:
            player_dy=0 
            #background(0)
            #print("you won")
            Words("Welcome to Machu Picchu!",400,500, 30)
            menuEnabled = True
            
    else: 
        dy_ground += gravity
        player_y = 100
    
    if cloud_y < -100:
        #print("d", player_x)
        #print((int(max(player_x-0.1*(400/(10*dy_ground)), 0)),int(min(player_x+0.1*(400/(10*dy_ground)),800))))
        cloud_x=random.randint(int(max(player_x-7*(400/(10*dy_ground)), 0)),int(min(player_x+7*(400/(10*dy_ground)),750)))
        #print(cloud_x)
        cloud_y=random.randint(500,600)
        cloud2_x = cloud_x + cloudDistance
        cloud2_y=cloud_y
        #checkIfPossible()
    #print(player_y)
    
    # print("Cloud1 ", cloud_x)
    # print("Cloud2 ", cloud2_x)
    
    ground_y -= 2*dy_ground
    
    #print(ground_y)
    player_x += player_dx
    cloud_y -= 5*dy_ground
    cloud2_y = cloud_y
    #print(cloud_y)
    #print(dy_ground)
    playerPower += .001
    player_y += player_dy
    
    #print(playerPower)
    #print(ground_y)

    if player_y <= 520:
        image(ground, ground_x, ground_y, 800,8000)
        image(cloud, cloud_x-800, cloud_y,800,50)
        image(cloud2, cloud2_x-150, cloud2_y,800,50)
    image(player, player_x, player_y,100,100)

    if checkCollision(player_x,player_y,50,50,cloud_x-800,cloud_y,800,50) == True:
        background(0)
        gameEnd= True

    if checkCollision(player_x,player_y,50,50,cloud2_x-150,cloud2_y,800,50) == True:
        background(0)
        gameEnd= True
    
def Words(Text,x,y,Size):
    textAlign(CENTER, CENTER)
    textSize(Size)
    text(Text,x,y)
    
    

def DrawMenu(x,y,m):#d=diameter r=red g=green b=blue m = mode (0 = regular, 1 = clear, 2 = brush up 3= brush down, 4 = style and b = type)
    fill (255)
    if m ==0:
        Words("Machu Picchu", x, y, 20)
    if m ==1:
        Words("Chichen Itza", x, y, 20)
    if m==2:
        Words("Christ the Redeemer(CS)", x, y, 20)
    if m == 3:
        Words("Petra", x, y, 20)
    if m == 4:
        Words("Taj Mahal(CS)", x, y, 20)
    if m == 5:
        Words("Colosseum(CS)", x, y, 20)
    if m ==6:
        Words("Great Wall of China(CS)", x, y, 20)
    
        
def MazeGame():
    global ccol, crow, menuEnabled, GameMode
    image (maze, 0, 0, 800, 600)
    fill (255, 153, 0)
    circle (circlex, circley, 10)
    if crow > 10:
        crow = 10
    if crow < 1:
        crow = 1
    if ccol > 10:
        ccol = 10
    if crow != 10 and ccol < 1:
        ccol = 1
    circlecheck()
    upstatecheck()
    downstatecheck()
    rightstatecheck()
    leftstatecheck()
    if keyCode == RIGHT and crow == 1 and ccol == 10:
        background(0)
        menuEnabled = True
        GameMode = 0
        #gameEnd= True
        

def circlecheck():
    global circlex, circley
    if ccol == 1:
        circlex = col1
    if ccol == 2:
        circlex = col2
    if ccol == 3:
        circlex = col3
    if ccol == 4:
        circlex = col4
    if ccol == 5:
        circlex = col5
    if ccol == 6:
        circlex = col6
    if ccol == 7:
        circlex = col7
    if ccol == 8:
        circlex = col8
    if ccol == 9:
        circlex = col9
    if ccol == 10:
        circlex = col10
    if crow == 1:
        circley = row1
    if crow == 2:
        circley = row2
    if crow == 3:
        circley = row3
    if crow == 4:
        circley = row4
    if crow == 5:
        circley = row5
    if crow == 6:
        circley = row6
    if crow == 7:
        circley = row7
    if crow == 8:
        circley = row8
    if crow == 9:
        circley = row9
    if crow == 10:
        circley = row10
        
def upstatecheck():
    global upstate
    upstate = 0
    if crow == 10 and ccol == 2 or crow == 10 and ccol == 3 or crow == 10 and ccol == 6 or crow == 10 and ccol == 8:
        upstate = 1
    if crow == 9 and ccol == 2 or crow == 9 and ccol == 9 or crow == 9 and ccol == 10:
        upstate = 1
    if crow == 8 and ccol == 1 or crow == 8 and ccol == 2 or crow == 8 and ccol == 5 or crow == 8 and ccol == 7 or crow == 8 and ccol == 8:
        upstate = 1
    if crow == 7 and ccol == 2 or crow == 7 and ccol == 5 or crow == 7 and ccol == 7:
        upstate = 1
    if crow == 6 and ccol == 3 or crow == 6 and ccol == 4 or crow == 6 and ccol == 6 or crow == 6 and ccol == 10:
        upstate = 1
    if crow == 5 and ccol == 2 or crow == 5 and ccol == 3 or crow == 5 and ccol == 5 or crow == 5 and ccol == 9:
        upstate = 1
    if crow == 4 and ccol == 2 or crow == 4 and ccol == 4 or crow == 4 and ccol == 5 or crow == 4 and ccol == 7 or crow == 4 and ccol == 8 or crow == 4 and ccol == 9:
        upstate = 1
    if crow == 3 and ccol == 3 or crow == 3 and ccol == 6 or crow == 3 and ccol == 7 or crow == 3 and ccol == 8 or crow == 3 and ccol == 10:
        upstate = 1
    if crow == 2 and ccol == 1 or crow == 2 and ccol == 4 or crow == 2 and ccol == 8 or crow == 2 and ccol == 9:
        upstate = 1

def downstatecheck():
    global downstate
    downstate = 0
    if crow == 9 and ccol == 2 or crow == 9 and ccol == 3 or crow == 9 and ccol == 6 or crow == 9 and ccol == 8:
        downstate = 1
    if crow == 8 and ccol == 2 or crow == 8 and ccol == 9 or crow == 8 and ccol == 10:
        downstate = 1
    if crow == 7 and ccol == 1 or crow == 7 and ccol == 2 or crow == 7 and ccol == 5 or crow == 7 and ccol == 7 or crow == 7 and ccol == 8:
        downstate = 1
    if crow == 6 and ccol == 2 or crow == 6 and ccol == 5 or crow == 6 and ccol == 7:
        downstate = 1
    if crow == 5 and ccol == 3 or crow == 5 and ccol == 4 or crow == 5 and ccol == 6 or crow == 5 and ccol == 10:
        downstate = 1
    if crow == 4 and ccol == 2 or crow == 4 and ccol == 3 or crow == 4 and ccol == 5 or crow == 4 and ccol == 9:
        downstate = 1
    if crow == 3 and ccol == 2 or crow == 3 and ccol == 4 or crow == 3 and ccol == 5 or crow == 3 and ccol == 7 or crow == 3 and ccol == 8 or crow == 3 and ccol == 9:
        downstate = 1
    if crow == 2 and ccol == 3 or crow == 2 and ccol == 6 or crow == 2 and ccol == 7 or crow == 2 and ccol == 8 or crow == 2 and ccol == 10:
        downstate = 1
    if crow == 1 and ccol == 1 or crow == 1 and ccol == 4 or crow == 1 and ccol == 8 or crow == 1 and ccol == 9:
        downstate = 1
def rightstatecheck():
    global rightstate
    rightstate = 0
    if ccol == 1 and crow == 2 or ccol == 1 and crow == 3 or ccol == 1 and crow == 5 or ccol == 1 and crow == 6 or ccol == 1 and crow == 9:
        rightstate = 1
    if ccol == 2 and crow == 2 or ccol == 2 and crow == 4:
        rightstate = 1
    if ccol == 3 and crow == 1 or ccol == 3 and crow == 3 or ccol == 3 and crow == 6 or ccol == 3 and crow == 8:
        rightstate = 1
    if ccol == 4 and crow == 2 or ccol == 4 and crow == 5 or ccol == 4 and crow == 6 or ccol == 4 and crow == 8 or ccol == 4 and crow == 9:
        rightstate = 1
    if ccol == 5 and crow == 1 or ccol == 5 and crow == 3 or ccol == 5 and crow == 4 or ccol == 5 and crow == 8:
        rightstate = 1
    if ccol == 6 and crow == 2 or ccol == 6 and crow == 4 or ccol == 6 and crow == 5 or ccol == 6 and crow == 8 or ccol == 6 and crow == 10:
        rightstate = 1
    if ccol == 7 and crow == 1 or ccol == 7 and crow == 3 or ccol == 7 and crow == 5 or ccol == 7 and crow == 6 or ccol == 7 and crow == 9:
        rightstate = 1
    if ccol == 8 and crow == 4 or ccol == 8 and crow == 6 or ccol == 8 and crow == 7 or ccol == 8 and crow == 9:
        rightstate = 1
    if ccol == 9 and crow == 3 or ccol == 9 and crow == 6 or ccol == 9 and crow == 7 or ccol == 9 and crow == 10:
        rightstate = 1
    
def leftstatecheck():
    global leftstate
    leftstate = 0
    if ccol == 2 and crow == 2 or ccol == 2 and crow == 3 or ccol == 2 and crow == 5 or ccol == 2 and crow == 6 or ccol == 2 and crow == 9:
        leftstate = 1
    if ccol == 3 and crow == 2 or ccol == 3 and crow == 4:
        leftstate = 1
    if ccol == 4 and crow == 1 or ccol == 4 and crow == 3 or ccol == 4 and crow == 6 or ccol == 4 and crow == 8:
        leftstate = 1
    if ccol == 5 and crow == 2 or ccol == 5 and crow == 5 or ccol == 5 and crow == 6 or ccol == 5 and crow == 8 or ccol == 5 and crow == 9:
        leftstate = 1
    if ccol == 6 and crow == 1 or ccol == 6 and crow == 3 or ccol == 6 and crow == 4 or ccol == 6 and crow == 8:
        leftstate = 1
    if ccol == 7 and crow == 2 or ccol == 7 and crow == 4 or ccol == 7 and crow == 5 or ccol == 7 and crow == 8 or ccol == 7 and crow == 10:
        leftstate = 1
    if ccol == 8 and crow == 1 or ccol == 8 and crow == 3 or ccol == 8 and crow == 5 or ccol == 8 and crow == 6 or ccol == 8 and crow == 9:
        leftstate = 1
    if ccol == 9 and crow == 4 or ccol == 9 and crow == 6 or ccol == 9 and crow == 7 or ccol == 9 and crow == 9:
        leftstate = 1
    if ccol == 10 and crow == 3 or ccol == 10 and crow == 6 or ccol == 10 and crow == 7 or ccol == 10 and crow == 10:
        leftstate = 1
    
    
def Mayangame():
    global playerX, playerVelX, ballX, ballY, ballZ, ballVelX, ballVelY,aiX, ballVelZ, GameMode, menuEnabled, playerMaya
    #image(image, x, y)
    #image(image, x, y, xsize, ysize) scale
    if moving==True:
        if keyCode == RIGHT:
            playerVelX += 0.8
        elif keyCode == LEFT:
            playerVelX -= 0.8
    playerX += playerVelX
    playerVelX *= 0.7

    
    #background
    fill(0, 0, 0)
    rect(0, 0, 800, 600)
    fill(176, 155, 97)
    rect(0, 0, 800, 200)
    fill(140, 120, 60)
    rect(0, 200, 800, 200)
    fill(120, 100, 40)
    rect(0, 400, 800, 400)
    
    lines(150)
    noStroke()
    
    #hoop
    fill(140, 120, 60)
    rect(390, 100, 10, 80)
    
    
    ballX += ballVelX
    ballY += ballVelY
    
    ballVelY += 0.1
    ballVelX *= 0.99
    
    if ballY>=330 and abs(playerX+100-ballX)<100:
        ballVelY = -8 + (random.randint(0,50)-25.0)/25
        #print((random.randint(0,50)-25.0)/50)
        ballVelX = -6 +(random.randint(0,50)-25.0)/25
    
    if ballY>=360 and abs(aiX+25-ballX)<50:
        ballVelY = -8 + (random.randint(0,50)-25.0)/25
        #print((random.randint(0,50)-25.0)/50)
        ballVelX = 6 + (random.randint(0,50)-25.0)/25
        
    if ballX > 380 and ballX < 420 and ballY > 60 and ballY < 140: 
        menuEnabled = True
        GameMode = 0
    
    
    if ballVelY > 460:
        menuEnabled = True
        GameMode = 0
    

    #print(ballX, ballY, ballZ)
    #print(ballVelX, ballVelY, ballVelZ)
    fill(255, 0, 0)
    circle(ballX, ballY, 40)
    #print("by", ballY, (ballY-300)/(ballZ/100)+300)
    #circle(ballX, (ballY-300)/(ballZ/100)+300, 60/(ballZ/100))
    
    #player
    fill(0, 0, 255)
    #rect(playerX, 360, 50, 100)
    image(playerMaya, playerX-10, 300, 200,250)
    
    if ballX<400:
        if aiX<ballX-70:
            aiX += 5
        else: 
            aiX -= 5
            
    fill(0, 255, 0)
    rect(aiX, 360, 50, 100)
    
    
    
def lines(w):
    stroke(0)
    for i in range(-800/w, 800/w*2):
        line(i*w, 600, (i*w-400)/2+400, 400)
    for i in range(-800/w, 800/w*2):
        line((i*w-400)/2+400, 400, (i*w-400)/3+400, 200)
    for i in range(-800/w, 800/w*2):
        line((i*w-400)/3+400, 200, (i*w-400)/3+400, 0)
    for i in range(-25, 25):
        line(0, i*24, 800, i*24);
        
def verticalGradientRect(x,y,w,h,r,g,b,r2,g2,b2):
    for i in range(h):
        fill(r+(r2-r)*i/h, g+(g2-g)*i/h, b+(b2-b)*i/h)
        rect(x, y+i, w, 1)
