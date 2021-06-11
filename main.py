import recordVideo
import takePic
import time
import logging
import filepath
import CheckStorage
import PiCFlask


def main():
    PiCFlask.hello_world()
    filepath.cameraLogMkdir()
    time.sleep(0.5)
    recordVideo.startRec()
    logging.info(" Done Recording")
    print(" Done Recording")
    time.sleep(5)
    takePic.startPic()
    logging.info(" Done with photo")
    print(" Done with photo")
    CheckStorage.checkSizeOfAllVidoes()
    CheckStorage.checkSizeOfAllPics()
    CheckStorage.checkSizeOfAllLogs()
    print("found the storage size ")


if __name__ == '__main__':
    app.run()
    main()
