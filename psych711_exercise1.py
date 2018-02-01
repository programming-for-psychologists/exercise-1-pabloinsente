# -*- coding: utf-8 -*-

"""
Psych 711 
Exercise 1
Pablo Caceres
"""

'''1. Make the square red instead of blue'''

import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squarer = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squarer.draw()
win.flip()
core.wait(1)
win.close()
sys.exit()

'''2. Make the square appear for 1.5 secs.'''
import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squarer = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squarer.draw()
win.flip()
core.wait(1.5) 
win.close()
sys.exit()


'''3. Show a red square for 1 s, then switch it to blue and show it for 1 s'''
import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squarer = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squareb = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
squarer.draw()
win.flip()
core.wait(1)
squareb.draw()
win.flip()
core.wait(1)
win.close()
sys.exit()

'''4. Make the square appear for 1.5 secs, then show a blank screen for 1 sec, 
then flash the square 3 times for 30 ms each.'''
import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squarer = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squareb = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
squarebl = visual.Rect(win,lineColor="black",fillColor="black",size=[100,100])


#red for 1.5 sec
squarer.draw()
win.flip()
core.wait(1) 
#black for 1 sec
squarebl.draw()
win.flip()
core.wait(1) 
#loop 3 flash
count = 0
while count < 4:
    squarer.draw()
    win.flip()
    core.wait(.3) 
    squarebl.draw()
    win.flip()
    count += 1

win.close()
sys.exit()


'''5. Show the following sequence: blue, red, blue, red, blue, red (with each square appearing for 1 s 
with a 50 ms blank screen in the middle).'''


import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squarer = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squareb = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])
squarew = visual.Rect(win,lineColor="black",fillColor="white",size=[800,800])


my_list =[0,1,0,1,0]

for i in my_list:
    if i ==0:
        squareb.draw()
        win.flip()
        core.wait(1)
        squarew.draw()
        win.flip()
        core.wait(.05)
    elif i ==1:
        squarer.draw()
        win.flip()
        core.wait(1)
        squarew.draw()
        win.flip()
        core.wait(.05)
win.close()
sys.exit()

'''6. Show a red square for 1 s then change its orientation by 45-deg'''
'''To change the orientation by a certain degree-value use square.setOri(value) where `value` is the new orientation.'''

import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squarer = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
squarer.draw()
win.flip()
core.wait(1) #pause for 1 sec
squarer.setOri(45) #change 45 degree orientation
squarer.draw()
win.flip()
core.wait(1) #pause for 1 sec
win.close()
sys.exit()

'''7. Now make a square rotate continuously, one full 
revolution (360 degrees) per second'''

import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squarer = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
count = 0
while count < 91:
    squarer.ori += 4 #change 4 degree orientation
    squarer.draw()
    win.flip()
    core.wait(1/90) 
    count += 1  # add1 counter

win.close()
sys.exit()


'''8. Make a rotating square stop rotating when you press the 's' key'''
'''To accept keyboard input you'll want to check it 
event.getKeys(['s']) is True.'''
            
import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squarer = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
            
pause = True
while pause:

        theseKeys = event.getKeys()
        if 's' in theseKeys:
            pause = False
        squarer.ori += 4
        squarer.draw()
        win.flip()       
        

'''9. Make a square stop rotating when you press 's' and then start 
rotating again when you press 'r'''

import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squarer = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100])
            
continueRoutine = True
paused = False
while continueRoutine:
        theseKeys = event.getKeys()
        if 's' in theseKeys:
            if not paused:
                paused = True
                continue
            elif paused:
                paused = False
        elif 'e' in theseKeys:
            win.close()
            sys.exit()
        elif paused:
            continue
        squarer.ori += 4 
        squarer.draw()
        win.flip()

'''10. Display a blue square and increase its width (making it a rectangle)
 by 10 pixels whenever the user presses the left-arrow key. 
 Decrease the width by 10 pixels when the user presses the right-arrow key'''
'''The key codes for right and left arrows in PsychoPy are simply 'right' and 'left'''
'''To change the width use `square.size += [x,y]` where `x` and `y` are the
 values by which you want to change the size'''


import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squareb = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100])

squareb.draw()
win.flip()
while True:
    theseKeys = event.getKeys()
    if 'l' in theseKeys:
        squareb.size += [+100,0]
        squareb.draw()
        win.flip()
    if 'r' in theseKeys:
        squareb.size += [-100,0]
        squareb.draw()
        win.flip()
    if 'e' in theseKeys:
        win.close()
        sys.exit()


'''11. Make the rectangle decrease/increase its width by 10% of its current
 width with each keypress instead of 10 pixels'''

import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
x = 100
y = 100
squareb = visual.Rect(win,lineColor="black",fillColor="blue",size=[x,y])

squareb.draw()
win.flip()
while True:
    theseKeys = event.getKeys()
    if 'l' in theseKeys:
        squareb.size += [0.1*(x),0.1*(y)]
        squareb.draw()
        win.flip()
    if 'r' in theseKeys:
        squareb.size += [-(0.1*(x)),-(0.1*(y))]
        squareb.draw()
        win.flip()
    if 'e' in theseKeys:
        win.close()
        sys.exit()

'''12. Show two rotating squares simultaneously, one 
left of center rotating clockwise, the other right of center, 
rotating counterclockwise'''

import time
import sys
from psychopy import visual,event,core
win = visual.Window([400,400],pos=(800,200), color="black", units='pix')
squarer = visual.Rect(win,lineColor="black",fillColor="red",size=[100,100], pos=(-50,0))
squareb = visual.Rect(win,lineColor="black",fillColor="blue",size=[100,100],pos=(50,0))

while True:
    theseKeys = event.getKeys()

    squarer.ori += 4 
    squarer.draw()
    win.flip()
    
    squareb.ori += -4
    squareb.draw()
    win.flip()
    
    if 'e' in theseKeys:
        win.close()
        sys.exit()