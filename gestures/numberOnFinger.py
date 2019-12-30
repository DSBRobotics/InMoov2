#Each gesture correspond to a number showed by the hand
def oneFinger():
  i01.startedGesture()
  rest()
  i01.moveHead(64.00,94.00,76.93,58.72,0.00,129.00)
  i01.moveArm("left",90.00,60.00,83.00,15.00)
  i01.moveArm("right",5.20,90.20,30.20,12.20)
  sleep(2.5)
  i01.moveHand("left",0.00,180.00,180.00,180.00,180.00,90.20)
  i01.moveHand("right",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveTorso(90.20,90.20,90.00)
  sleep(2)
  i01.finishedGesture()
  relax()

def twoFinger():
  i01.startedGesture()
  rest()
  i01.moveHead(64.00,94.00,95.00,90.00,0.00,38.00)
  i01.moveArm("left",90.00,60.00,83.00,15.00)
  i01.moveArm("right",5.20,90.20,30.20,12.20)
  sleep(2.5)
  i01.moveHand("left",0.00,0.00,180.00,180.00,180.00,90.20)
  i01.moveHand("right",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveTorso(90.20,90.20,90.00)
  sleep(2)
  i01.finishedGesture()
  relax()

def threeFinger():
  i01.startedGesture()
  rest()
  i01.moveHead(64.00,94.00,95.00,90.00,0.00,129.00)
  i01.moveArm("left",80.00,66.00,83.00,10.00)
  i01.moveArm("right",5.20,90.20,30.20,12.20)
  sleep(2.5)
  i01.moveHand("left",0.00,0.00,0.00,180.00,180.00,90.20)
  i01.moveHand("right",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveTorso(90.20,90.20,90.00)
  sleep(2)
  i01.finishedGesture()
  relax()

def fourFinger():
  i01.startedGesture()
  rest()
  i01.moveHead(43.00,94.00,90.00,90.00,0.00,129.00)
  i01.moveArm("left",80.00,58.00,75.00,10.00)
  i01.moveArm("right",5.20,90.20,30.20,12.20)
  sleep(2.5)
  i01.moveHand("left",0.00,0.00,0.00,0.00,180.00,90.20)
  i01.moveHand("right",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveTorso(90.20,90.20,90.00)
  sleep(2)
  i01.finishedGesture()
  relax()

def fiveFinger():
  i01.startedGesture()
  rest()
  i01.moveHead(46.00,90.00,122.17,64.06,0.00,74.37)
  i01.moveArm("left",88.00,58.00,75.00,10.00)
  i01.moveArm("right",5.20,90.20,30.20,12.20)
  sleep(2.5)
  i01.moveHand("left",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveHand("right",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveTorso(90.20,90.20,90.00)
  sleep(2)
  i01.finishedGesture()
  relax()

def sixFinger():
  i01.startedGesture()
  rest()
  i01.moveHead(46.00,73.00,122.17,64.06,0.00,21.00)
  i01.moveArm("left",88.00,58.00,75.00,10.00)
  i01.moveArm("right",90.00,90.20,55.00,12.20)
  sleep(2.5)
  i01.moveHand("left",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveHand("right",0.00,180.00,180.00,180.00,180.00,90.20)
  i01.moveTorso(90.20,90.20,90.00)
  sleep(2)
  i01.finishedGesture()
  relax()

def sevenFinger():
  i01.startedGesture()
  rest()
  i01.moveHead(90.00,70.00,122.17,64.06,0.00,21.00)
  i01.moveArm("left",55.00,58.00,75.00,10.00)
  i01.moveArm("right",90.00,90.20,55.00,12.20)
  sleep(2.5)
  i01.moveHand("left",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveHand("right",0.00,0.00,180.00,180.00,180.00,90.20)
  i01.moveTorso(90.20,90.20,90.00)
  sleep(2)
  i01.finishedGesture()
  relax()

def eightFinger():
  i01.startedGesture()
  rest()
  i01.moveHead(72.00,64.00,122.17,64.06,0.00,0.00)
  i01.moveArm("left",86.00,58.00,75.00,16.00)
  i01.moveArm("right",90.00,93.00,58.00,12.20)
  sleep(2.5)
  i01.moveHand("left",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveHand("right",0.00,0.00,0.00,180.00,180.00,90.20)
  i01.moveTorso(90.20,90.20,90.00)
  sleep(2)
  i01.finishedGesture()
  relax()

def nineFinger():
  i01.startedGesture()
  rest()
  i01.moveHead(72.00,64.00,122.17,64.06,0.00,0.00)
  i01.moveArm("left",86.00,58.00,75.00,16.00)
  i01.moveArm("right",90.00,93.00,58.00,12.20)
  sleep(2.5)
  i01.moveHand("left",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveHand("right",0.00,0.00,0.00,0.00,180.00,90.20)
  i01.moveTorso(90.20,90.20,90.00)
  sleep(2)
  i01.finishedGesture()
  relax()

def tenFinger():
  i01.startedGesture()
  rest()  
  i01.moveHead(72.00,64.00,122.17,64.06,0.00,0.00)
  i01.moveArm("left",86.00,58.00,75.00,16.00)
  i01.moveArm("right",90.00,93.00,58.00,12.20)
  sleep(2.5)
  i01.moveHand("left",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveHand("right",0.00,0.00,0.00,0.00,0.00,90.20)
  i01.moveTorso(90.20,90.20,90.00)
  sleep(2)
  i01.finishedGesture()
  relax()
