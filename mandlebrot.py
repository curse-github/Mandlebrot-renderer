import pygame
import threading
import time
def clamp(num, min_value, max_value):
    return max(min(num, max_value), min_value)
def getTime():
    return round(time.time()*1000)
def timeDifString(num):
    num2 = round(num*1000)/1000
    if (num > 1000*60*60*24):#days
        num2 = round(num/(1000*60*60*24)*1000)/1000
        string = str(num2).ljust(6, "0")
        return (string + "days").rjust(9, " ")# 9 possible digits
    elif (num > 1000*60*60):#hours
        num2 = round(num/(1000*60*60)*1000)/1000
        string = str(num2)
        if (num2 < 10):
            string = "0"+string
        string = string.ljust(6, "0")
        return (string + "hrs").rjust(9, " ")# 9 possible digits
    elif (num > 1000*60):#minutes
        num2 = round(num/(1000*60)*1000)/1000
        string = str(num2)
        if (num2 < 10):
            string = "0"+string
        string = string.ljust(6, "0")
        return (string + "min").rjust(9, " ")# 8 possible digits
    elif (num > 1000):#seconds
        num2 = round(num/(1000)*1000)/1000
        string = str(num2)
        if (num2 < 10):
            string = "0"+string
        string = string.ljust(6, "0")
        return (string + "s").rjust(9, " ")# 8 possible digits
    else:#milli-seconds
        return (str(num2).ljust(4, "0")+"ms").rjust(9, " ")# 6 possible digits


#IMPORTANT
rangeX = (1.25-(32/9),1.25)
rangeY = (-1,1)
#rangeX = (-0.593100,-0.592600)
#rangeY = (-0.4343125,-0.4339125)
xrange = abs(rangeX[0]-rangeX[1])
yrange = abs(rangeY[0]-rangeY[1])
resolution = 500/min(xrange/3,yrange/3)
width, height = round(xrange*resolution), round(yrange*resolution)
infRange = 150
accuracy = 750
col = (64,255,64)#white
#col = (86, 29, 201)#purple
#col = (127,0,0)#maroon

def j(cord,cord2,x,y,surface):
    cord = ((cord[0]*cord[0])-(cord[1]*cord[1]) + cord2[0],(2*cord[0]*cord[1]) + cord2[1])
    count = 0
    while (cord[0] > rangeX[0]-infRange and cord[0] < rangeX[1]+infRange and cord[1] > rangeY[1]-infRange and cord[1] < rangeY[0]+infRange):
        if (count>accuracy):
            count = 0
            break
        count = count+1
        cord = ((cord[0]*cord[0])-(cord[1]*cord[1]) + cord2[0],(2*cord[0]*cord[1]) + cord2[1])
        continue
    thing = clamp(count/(accuracy/6),0,1)
    surface.set_at((x, y), (thing*col[0],thing*col[1],thing*col[2]))
    return

surface = pygame.Surface((width, height));

cnt = 0;
startTime = getTime()
lastTime = getTime()
crd = (0,0)
for x in range(0,width):
    for y in range(0,height):
        cnt = cnt+1
        crd = ((x/width*abs(rangeX[0]-rangeX[1])+rangeX[0]),  (y/height*abs(rangeY[0]-rangeY[1])+rangeY[0]))
        
        if (round(cnt%(width*height/100))==0):# nearest percent
            tm = getTime()
            percent = cnt/(width*height)
            sincelast = (tm-lastTime)
            total = (tm-startTime)
            estimate = total/percent
            print(str(round(percent*100)).rjust(3, " ") + "%, " + timeDifString(sincelast) + " since last percent, total time : " + timeDifString(total) + ", finish time estimate: " + timeDifString(estimate))
            lastTime = tm
        if (threading.active_count() < 5):
            threading.Thread(target=j,args=(crd,crd,x,y,surface)).start()
        else:
            val = j(crd,crd,x,y,surface)


pygame.image.save(surface, "Preview.png")
print("\ntotal time : " + timeDifString(getTime()-startTime) + "!")