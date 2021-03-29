import os

camera_Pic = "/home/pi/picam/pictures/"
camera_Vid = "/home/pi/picam/videos/"
camera_Log = "/home/pi/picam/logs/"


def cameraPic(timeStamp):
    print(str(os.path.isdir(camera_Pic)))
    if os.path.isdir(camera_Pic) == True:
        print("Path: " + camera_Pic + " Already exist")
        return camera_Pic + timeStamp + ".h264"
    else:
        os.makedirs(camera_Pic)
        return camera_Pic + timeStamp + ".h264"


def cameraVid(timeStamp):
    print(str(os.path.isdir(camera_Vid)))
    if os.path.isdir(camera_Vid) == True:
        print("Path: " + camera_Vid + " Already exist")
        return camera_Vid + timeStamp + ".h264"
    else:
        os.makedirs(camera_Vid)
        return camera_Vid + timeStamp + ".h264"


def cameraLog(timeStamp):
    print(str(os.path.isdir(camera_Log)))
    if os.path.isdir(camera_Log) == True:
        print("Path: " + camera_Log + " Already exist")
        return camera_Log + timeStamp + ".h264"
    else:
        os.makedirs(camera_Log)
        return camera_Log + timeStamp + ".h264"
