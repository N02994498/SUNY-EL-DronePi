import datetime
import os

class Camera(object):
    """Manages the camera for the raspberry pi"""
    def __init__(self):
        if not os.path.exists("img/"):
            os.system("mkdir img/")
            os.system("sudo chmod 777 img/")

    def takePicture(self, cameraOptions):
    # receives a string with all the camera options available at
    # http://www.raspberrypi.org/documentation/raspbian/applications/camera.md
    # takes a picture and logs to the log.txt file

        print "Taking picture ... "

        dateString = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        takePictureCommand = 'raspistill --output img/' + dateString + '.jpg' + cameraOptions

        try:
            os.system(takePictureCommand)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            os.system( "echo 'ERROR: picture NOT saved' %s >> log.txt" % (dateString))
        else:
            os.system( "echo 'picture saved' %s >> log.txt" % (dateString))
            print "Picture saved successfuly."
    


