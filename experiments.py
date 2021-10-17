from posixpath import join
from pygaze.display import Display
from pygaze.screen import Screen
import pygaze.libtime as timer
from pygaze.sound import Sound
from constants import WORDS,NONWORDS
from pygaze.keyboard import Keyboard
from pygaze.logfile import Logfile

import random



disp = Display()
kb= Keyboard()

good_sound= Sound(osc="sine",freq=440,length=500)
bad_sound= Sound(osc="saw",freq=440,length=500)

log= Logfile()
log.write(["trialnr","stim,type","stim_onset","response","RT"])

fix_screen= Screen()
# fix_screen.draw_fixation(fixtype="cross",pw=3,diameter=25)
all_trials =[]
# Create a trial structure 
for word in WORDS:
    trial={}
    trial["stimtype"]="word"
    trial["stimulus"]=word
    all_trials.append(trial)
# Create a trial structure 
for word in NONWORDS:
    trial={}
    trial["stimtype"]="nonword"
    trial["stimulus"]=word
    all_trials.append(trial)

random.shuffle(all_trials)



for trialnr, trial in enumerate(all_trials):  
    stim_screen = Screen()
    stim_screen.draw_text(trial["stimulus"],fontsize=100)

    #Start recording

    disp.fill(fix_screen)
    t0= disp.show()
    timer.pause(1000)
    disp.fill(stim_screen)
    t1 = disp.show()

    
    key,time= kb.get_key(keylist=["left","right"],timeout=3000,flush=True)
    print(key,time-t1)
    log.write([trialnr ,trial["stimtype"],trial["stimulus"],t1,key,time-t1])
    correct =((trial["stimtype"]=="word")& ((key=="left")) or 
    (trial["stimtype"]=="nonword") &(key=="right"))
    if correct:
        good_sound.play()
    else:
        bad_sound.play()

    disp.fill()
    disp.show()
    timer.pause(500)



# t1= disp.show()

# timer.pause(2000)
# fix_screen.draw_fixation(fixtype="dot",pw=3,diameter=25,colour=(255,12,89))
# disp.fill(fix_screen)
# t2= disp.show()
# timer.pause(2000)

# #
# stim_screen = Screen()
# stim_screen.draw_text("Hello",fontsize=100)
# disp.fill(stim_screen)
# t3= disp.show()
# timer.pause(2000)


# disp.close()


