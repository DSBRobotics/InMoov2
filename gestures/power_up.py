def power_up():
  ##sleep(2)
  ##rightSerialPort.digitalWrite(53, Arduino.HIGH)
  ##leftSerialPort.digitalWrite(53, Arduino.HIGH)
  i01.speakBlocking("I was sleeping")
  lookrightside()
  sleep(2)
  lookleftside()
  sleep(4)
  relax()
  ear.clearLock()
  sleep(2)