def agreeanswer():
  i01.startedGesture()
  i01.setHandVelocity("left", -1, -1, -1, -1, -1, -1)
  i01.setHandVelocity("right", -1, -1, -1, -1, -1, -1)
  i01.setArmVelocity("left", -1.0, -1.0, -1.0, -1.0)
  i01.setArmVelocity("right", -1.0, -1.0, -1.0, -1.0)
  i01.setHeadVelocity(-1, 50)
  i01.setTorsoVelocity(-1, -1, -1)
  i01.moveHead(120,90)
  sleep(0.5)
  i01.moveHead(20,90)
  sleep(0.5)
  i01.moveArm("left",20,93,42,16)
  i01.moveArm("right",20,93,37,18)
  i01.moveHand("left",180,180,65,81,41,143)
  i01.moveHand("right",180,180,18,61,36,21)
  i01.moveTorso(90,90,90)
  sleep(0.5)
  i01.moveHead(90,90)
  sleep(0.2)
  i01.finishedGesture()
  relax()
