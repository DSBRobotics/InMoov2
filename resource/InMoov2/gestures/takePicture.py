def takePicture():
  i01.cameraOn()
  photoFileName = i01_opencv.recordFrame()
  print photoFileName
  AudioPlayer.playFile(RuningFolder+'/system/sounds/ShutterClik.mp3')
  imagedisplay.display(photoFileName)
  sleep(15)
  imagedisplay.closeAll()