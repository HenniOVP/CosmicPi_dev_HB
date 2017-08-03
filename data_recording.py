import sys
sys.path.append('.')
import time
import sensors


IMU_SETTINGS_FILE = "IMU_settings"

# set up the IMU
imu = sensors.IMU_Reader(IMU_SETTINGS_FILE)

# set up and start the GPS
gps = sensors.GPS_location_provider();
gps.start()


do_test_run = True
while do_test_run:
    # print some data regularily
    time.sleep(0.5)
    # print the last GPS data
    gps_data = gps.get_last_location_data()
    print("--> GPS: ", gps_data)
    # get imu data
    IMU_data = imu.get_IMU_and_Pressure_data(average=1)
    # print imu data
    imu.print_IMU_and_pressure_data(IMU_data)


