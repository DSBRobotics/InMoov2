def eatindianfood():
  fullspeed()
  i01.startedGesture()
  i01.setHeadVelocity(43.0, 36, 50, 50, -1)
  i01.moveHead(60,40,7,85,52)
  sleep(1)
  i01.moveHead(80,40,7,85,52)
  sleep(2)
  i01.setHeadVelocity(0.92, 36, 50, 50, -1)
  i01.moveHead(100,40,7,85,52)
  sleep(0.4)
  i01.moveArm("left",85,106,25,18)
  i01.moveArm("right",87,107,32,18)
  i01.moveHand("left",110,62,56,88,81,145)
  i01.moveHand("right",78,88,101,95,81,27)
  i01.moveTorso(90,90,90)
  i01.moveHead(80,40,7,85,52)
  i01.mouth.speakBlocking("yes, i want some paneer tikka")
  #i01.mouth.speakBlocking(u"Да, я хочу немного paneer tikka")
  sleep(1)
  i01.moveHead(60,90,80,90,52)
  sleep(0.8)
  i01.finishedGesture()
  relax()
