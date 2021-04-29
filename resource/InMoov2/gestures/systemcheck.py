def systemcheck():
  fullspeed()
  i01.startedGesture()
  i01.setHeadSpeed(30,30,70)
  i01.moveHead(90,90,90)
  sleep(1)
  i01.moveHead(90,40,90)
  sleep(1)
  i01.moveHead(165,90,90)
  sleep(1)
  i01.moveHead(90,160,90)
  sleep(1)
  i01.moveHead(20,90,90)
  sleep(1)
  i01.moveHead(90,90,20)
  sleep(1)
  i01.moveHead(90,90,160)
  sleep(1)
  i01.moveHead(90,90,20)
  sleep(1)
  i01.moveHead(90,90,160)
  sleep(1)
  i01.moveHead(90,90,90)
  sleep(2)
  i01.speakBlocking("Head, neck and mouth,   check")
  #i01.speakBlocking(u"Голова, шея и рот, проверил")
  sleep(1)
  i01.setHeadSpeed(60,60,70)
  i01.moveHead(25,61,90)
  i01.setArmSpeed("left",40,40,40,40)
  i01.setArmSpeed("right",40,40,40,40)
  i01.moveArm("left",0,90,30,10)
  i01.moveArm("right",24,62,52,45)
  i01.moveHand("left",0,0,0,0,0,90)
  i01.moveHand("right",0,0,0,0,0,90)
  sleep(2)
  i01.moveHead(90,90,90)
  sleep(1)
  i01.speakBlocking("right arm and right shoulder,  check")
  #i01.speakBlocking(u"Правая рука и правое плечо, проверил")
  sleep(1)
  i01.moveHead(20,122,90)
  i01.moveArm("left",24,62,52,45)
  sleep(2)
  i01.moveHead(90,90,90)
  sleep(1)
  i01.speakBlocking("left arm and left shoulder,  check")
  #i01.speakBlocking(u"Левая рука и левое плечо, проверил")
  sleep(1)
  i01.moveHead(20,120,90)
  i01.moveArm("left",75,123,52,45)
  i01.moveArm("right",75,123,52,45)
  i01.moveHand("left",180,180,180,180,180,30)
  i01.moveHand("right",180,180,180,180,180,170)
  sleep(3)
  i01.moveHead(59,67,90)
  i01.moveHand("right",0,0,0,0,0,19)
  i01.moveHand("left",0,0,0,0,0,170)
  sleep(1)
  i01.moveHand("left",180,180,180,180,180,30)
  i01.moveHand("right",180,180,180,180,180,170)
  sleep(1.5)
  i01.moveHead(90,90,90)
  sleep(1)
  i01.speakBlocking(" hands and Wrists,  check")
  #i01.speakBlocking(u" Кисти и запястья, проверил")
  sleep(1)
  i01.moveHead(90,90,90)
  i01.moveArm("left",0,90,30,10)
  i01.moveArm("right",0,90,30,10)
  i01.moveHand("left",0,0,0,0,0,90)
  i01.moveHand("right",0,0,0,0,0,90)
  i01.speakBlocking("all servos are functioning properly")
  #i01.speakBlocking(u"Все сервоприводы функционируют должным образом")
  sleep(1.5)
  i01.speakBlocking("awaiting your commands")
  #i01.speakBlocking(u"Ожидаю ваши команды")
  sleep(0.5)
  i01.finishedGesture()
  relax()

