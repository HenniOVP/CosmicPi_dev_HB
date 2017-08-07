import sys
sys.path.append('.')
import time
import sensors
import detectors


# set up the IMU
IMU_SETTINGS_FILE = "IMU_settings"
imu = sensors.IMU_Reader(IMU_SETTINGS_FILE)

# set up and start the GPS
gps = sensors.GPS_location_provider()


# def a recieving function
def do_something_with_new_detector_data(*args):
    print("Fresh new data now at the detector!")
    print(args)
    # print the last GPS data
    gps_data = gps.get_last_location_data()
    print("--> GPS: ", gps_data)
    # get imu data
    IMU_data = imu.get_IMU_and_Pressure_data()
    # print imu data
    imu.print_IMU_and_pressure_data(IMU_data)

# start our detector
detec = detectors.simulated_detector()
# subscribe to detector events
detec.on_publish_new_data += do_something_with_new_detector_data

