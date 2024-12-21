
# Log / notes

**21.12.**

Game finalized, not perfect but maybe ok. Some functions added. 


**12.12.**

A little bit better dev version, class additions to monster and coin and a little bit clearer code. Time counting still not working, ended up in a wait version, not very classy. 




**11.12.**

V3 to master published. 

V4 to some point
- parameters in front
- changed door to own class, don't know really if it's wise but a little less global parameters now 
  - could do this for robo movement speed also!!
  - could do this for coin also? 
- init_screen function works for creating screen object but didn't get check_coin_encounter to work... 
  - maybe something more simple?
- final time still not working - if not, then freeze screen for ten secs TMP solution?  
- TODO
  - can i get encounter coin / encounter monster to work (ref. starship and bullets)

**9.12.**

V2 to master published. 

V3: could do so that one monster increases speed until 3 coins, then more monsters appear
- if monster has a value of direction, those could be randomized? or every other lengthwise, every other heighwise? 
- if monster is encountered, reduce one coin and move to 0,0 (where no mosters can be created?) 
  - priority is to get this working! 

Did get monster encounter working for one monster and list multiple monsters. 
- continue by triyng to plot one monster per additional point and worry about moving them afterwards? 
- or by trying to for loop the movement pattern
- or by revising piirileikki / robots from sky 

A secret spot that enhances the speed to max 2? 

**6.12.**

V1 to master, V2 to some point. Many problems still with v2, including: 

- how to get point counter so that it only adds one BUT prints the text for example for 5 seconds
  - if only locations match, does the trick for points
- monster is not moving great 
- boundaries should be set
- time: change to systime minus start time and maybe a new robot every minute? 
- is there a way to start the game for example in 5 seconds / until you press enter: show instructions 

Fix some of these for V2! Point counting and coins appearing to a new place should be a priority so door and monsters appearing work! 