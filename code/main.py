import camera
import gpsPoller
import datetime
import database
import os


camera = camera.Camera()
gps = gpsPi.Gps()
db = database.Database('../www/database/pi_database.db')

# camera
def triggerCamera(gpsData):

    gpsCoordinatesOptions = ""

    dateString = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

    gpsDataFormated = formatGpsData(gpsData)

    # this section should be uncomented when the method formatGpsData is working
    # if gpsData:
    #     gpsCoordinatesOptions = (
    #     " --exif GPS.GPSLatitude=%s "
    #     " --exif GPS.GPSLongitude=%s "
    #     " --exif GPS.GPSAltitude=%s "
    #     ) % ( gpsDataFormated['latitude'], gpsDataFormated['longitude'], gpsDataFormated['altitude'])
    # else:
    #     print "ERROR: gpsData is empty"
    #     os.system( "echo 'ERROR: gpsData is empty' %s >> log.txt" % (dateString))

    cameraOptions = (
                    " --exposure sports "
                    " --width 800 "
                    " --height 600 "
                    " --quality 75 "
                    )

    options = cameraOptions + gpsCoordinatesOptions

    fullPath = 'http://drone.nulldivision.com/www/images/camera/'
    fileName = dateString + '.jpg'

    dataToDatabase = {
        'dateTime': dateString,
        'pathToImage': fullPath + fileName,
        'latitude': gpsData['latitude'],
        'longitude': gpsData['longitude'],
        'altitude': gpsData['altitude']
    }

    pathToImage = '../www/images/camera/' + fileName
    db.dataEntry(dataToDatabase)

    try:
        camera.takePicture(options, pathToImage)
    except Exception, e:
        dateString = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        os.system( "echo 'ERROR: picture NOT saved' %s >> log.txt" % (dateString))
    else:
        db.dataEntry(dataToDatabase)
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

#show gps reading in terminal
if __name__ == '__main__' :
        gpsp = GpsPoller()
        try:
                gpsp.start()
                while True:

                        os.system('clear')

                        print
                        print 'GPS reading'
                        print '-------------------------------------------------'
                        print 'latitude   ' , gpsData['latitude']
                        print 'longitude   ' , gpsdData['longitude']
                        print 'altitude (m)   ' , gpsdData['altitude']
                        print
triggerCamera(gpsData)
