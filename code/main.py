import camera
import gps
import datetime

camera = camera.Camera()
gps = gps.Gps()

# camera
def triggerCamera(gpsData):
    gpsCoordinatesOptions = ""

    if gpsData:
        gpsCoordinatesOptions = (
        " --exif GPS.GPSLatitude=%s " 
        " --exif GPS.GPSLongitude=%s "
        " --exif GPS.GPSAltitude=%s "
        ) % ( gpsData['latitude'], gpsData['longitude'], gpsData['altitude'])
    else:
        dateString = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        os.system( "echo 'ERROR: gpsData is empty' %s >> log.txt" % (dateString))

    cameraOptions = (
                    " --exposure sports "
                    " --width 800 "
                    " --height 600 "
                    " --quality 75 "
                    )

    options = cameraOptions + gpsCoordinatesOptions

    try:
        camera.takePicture(options)
    except Exception, e:
        dateString = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        os.system( "echo 'ERROR: picture NOT saved' %s >> log.txt" % (dateString))
    else:
        return 1
  

# TODO format lat and lon
def formatGpsData(gpsData):
    # Receives the latitude, longitude and altitude with the original format from gps reading
    # And converts to the camera options required format
    # Required format sample: latitude or longitude: '-33/1,66/1,451/100' Altitude: 71.2/10
    gpsDataFormated = {}
    gpsDataFormated['latitude'] = gpsData['latitude']
    gpsDataFormated['longitude'] = gpsData['longitude']
    gpsDataFormated['altitude'] = gpsData['altitude'] + '/10'
    return gpsDataFormated

# TODO gps reading 
gpsData = gps.read()
gpsDataFormated = formatGpsData(gpsData)
triggerCamera(gpsDataFormated)
