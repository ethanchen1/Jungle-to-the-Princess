#Narwhale Inc
#Jessica Cui, Ethan Chen, Joseph Devito
#Jungle to the Princess - Gargamel has captured the princess from Clumsy. You must control Clumsy to save the princess by passing several levels.
#objects

from gamelib import*
game=Game(800,600,"Berry Hunt",60)
bk=Image("forest1.jpg",game,)
bk.resizeTo(game.width,game.height)
game.setBackground(bk)
madguy=Animation("run.png",10,game,1400/5,770/2,10)
madguy.resizeBy(-50)
guy=Animation("run.png",10,game,1400/5,770/2,10)
guy.resizeBy(-55)
guy.x=100
guy.y=500
play=Image("play-text-png-7.png",game)
play.resizeBy(-70)
play.moveTo(425,250)
tree=[] 
branch=[]
berry=[]
pberry=[]

for index in range(100):
    tree.append(Image("Tree.png",game))
    berry.append(Image("berry1.png",game))
    pberry.append(Image("poisonberry.png",game))
    tree[index].resizeBy(-70)
    berry[index].resizeBy(-93)
    pberry[index].resizeBy(-95)
for index in range(100):
    x=randint(-100,700)
    y=randint(50,10000)
    berry[index].moveTo(x,y)
    berry[index].y-=10100
for index in range(100):
    x=randint(100,600)
    y=randint(100,10000)
    pberry[index].moveTo(x,y)
    pberry[index].y-=10100
for index in range(100):
          if guy.collidedWith(berry[index]):
            berry[index].visible=False
            game.score+=10
          if guy.collidedWith(pberry[index]):
             pberry[index].visible=False
             game.score-=5
             guy.health-=10

f=Font(black,70,green,"Impact")

#variable for jumping action        
jumping = False #Used to check to see if you are jumping
landed = False  #Used to check to see if you have landed on the "ground" (platform)
factor = 1  #Used for a slowing effect of the jumping

while not game.over:   #title screen
    game.processInput()
    bk.draw()
    play.draw()
    madguy.draw()
    madguy.moveTo(200,300)
    game.drawText("Berry Hunt",game.width / 2 - 100, game.height / 2,f)
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over=True
    game.update(30)

game.over=False


while not game.over:    #level 1
    game.processInput()
    game.scrollBackground("left",2)
    game.health=100
    tree[1].moveTo(300,170)
    tree[0].moveTo(130,250)
    tree[2].moveTo(400,420)
    tree[3].moveTo(200,430)
    tree[4].moveTo(500,150)
    tree[5].moveTo(650,330)
    for index in range(100):
        s=randint(2,8)
        berry[index].draw()
        berry[index].move()
        berry[index].setSpeed(s,180)
        pberry[index].draw()
        pberry[index].move()
        pberry[index].setSpeed(s,180)
    if guy.y< 500:#value of y is based on your object's y position
        landed = False#not landed

    else:
        landed = True
   
            
    if keys.Pressed[K_SPACE] and landed and not jumping:#if you have landed and are not jumping and press the space bar then jump
        jumping = True

    if jumping:
   
        guy.y -=35*factor#adjust for the drop
        #Make the character go up.  Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
            
    if not landed: #is jumping
        guy.y +=15#adjust for the height of the jump - lower number higher jump
    if keys.Pressed[K_SPACE]:
        guy.y-=8   
    if keys.Pressed[K_RIGHT]:
        guy.x+=8
    if keys.Pressed[K_LEFT]:
        guy.x-=8
    for index in range(100):
          if guy.collidedWith(berry[index]):
            berry[index].visible=False
            game.score+=10
          if guy.collidedWith(pberry[index]):
             pberry[index].visible=False

             game.score-=5
    if game.score>100 and game.time<0:
        game.over=True
    guy.draw()
    game.displayScore()
    game.displayTime(100,5)
    game.update(30)
game.quit()
