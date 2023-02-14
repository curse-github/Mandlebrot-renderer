import pygame
import threading
import time
rangeX = (-2,1)
rangeY = (-1,1)
#rangeX = (-0.593100,-0.592600)
#rangeY = (-0.4343125,-0.4339125)

resolution = 500/min(abs(rangeX[0]-rangeX[1])/3,abs(rangeY[0]-rangeY[1])/3)
width, height = round(abs(rangeX[0]-rangeX[1])*resolution), round(abs(rangeY[0]-rangeY[1])*resolution)
infRange = 20
accuracy = 5000
col = (255,255,255)#white
#col = (86, 29, 201)#purple
#col = (127,0,0)#maroon

def j(cord,cord2,x,y,surface):
    cord = ((cord[0]*cord[0])-(cord[1]*cord[1]) + cord2[0],(2*cord[0]*cord[1]) + cord2[1])
    count = 0
    while (cord[0] < rangeX[0]+infRange and cord[0] > rangeX[1]-infRange and cord[1] < rangeY[0]+infRange and cord[1] > rangeY[1]-infRange):
        if (count>accuracy):
            count = 0
            break
        count = count+1
        cord = ((cord[0]*cord[0])-(cord[1]*cord[1]) + cord2[0],(2*cord[0]*cord[1]) + cord2[1])
        continue
    surface.set_at((x, y), ((count/accuracy)*col[0],(count/accuracy)*col[1],(count/accuracy)*col[2]))
    return

surface = pygame.Surface((width, height));

def getTime():
    return round(time.time()*1000)

cnt = 0;
startTime = getTime()
lastTime = getTime()
crd = (0,0)
for x in range(0,width):
    for y in range(0,height):
        cnt = cnt+1
        crd = ((x/width*abs(rangeX[0]-rangeX[1])+rangeX[0]),  (y/height*abs(rangeY[0]-rangeY[1])+rangeY[0]))
        
        if (round(cnt%(width*height/100))==0):
            tm = getTime()
            print(str(round(cnt/width/height*100))+"%, since last percent : " + str((tm-lastTime)/1000/60) + "min, total time : " + str((tm-startTime)/1000/60) + "min")
            lastTime = tm
        val = j(crd,crd,x,y,surface)
        '''if (threading.active_count() < 5):
            threading.Thread(target=j,args=(crd,crd,x,y,surface)).start()
        else:
            val = j(crd,crd,x,y,surface)'''


pygame.image.save(surface, "mandlebrotZoomed.jpg")
print("\ntotal time : " + str((getTime()-startTime)/1000/60) + "min")