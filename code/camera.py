import os

class Camera(object):
    """Manages the camera for the raspberry pi"""

    def takePicture(self, cameraOptions, path_to_image):
    # receives a string with all the camera options available at
    # http://www.raspberrypi.org/documentation/raspbian/applications/camera.md
    # takes a picture and logs to the log.txt file

        print "Taking picture ... "

        takePictureCommand = 'raspistill --output ' + path_to_image + cameraOptions

        try:
            print "Sending picture command to pi"
            os.system(takePictureCommand)
        except:
            print "Unexpected error:", sys.exc_info()[0]
            os.system( "echo 'ERROR: picture NOT saved' %s >> log.txt" % (dateString))
        else:
            os.system( "echo 'picture saved' %s >> log.txt" % (dateString))
            print "Picture saved successfuly."




