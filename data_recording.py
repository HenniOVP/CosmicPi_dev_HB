import sys, getopt

sys.path.append('.')
import RTIMU
import os.path
import time
import math

class IMU_Reader():

    def __init__(self, IMU_SETTINGS_FILE):
        # ---------  Set up IMU
        print("Using settings file " + IMU_SETTINGS_FILE + ".ini")
        if not os.path.exists(IMU_SETTINGS_FILE + ".ini"):
            print("Settings file does not exist, will be created")

        self.s = RTIMU.Settings(IMU_SETTINGS_FILE)
        self.imu = RTIMU.RTIMU(self.s)
        self.pressure = RTIMU.RTPressure(self.s)

        print("IMU Name: " + self.imu.IMUName())
        print("Pressure Name: " + self.pressure.pressureName())

        if (not self.imu.IMUInit()):
            print("IMU Init Failed")
            raise RuntimeError("Could not initilize IMU! Is I2C enabled? Are you on the Pi? Did you check that the IMU is visible via I2C?")
        else:
            print("IMU Init Succeeded");

        # this is a good time to set any fusion parameters

        self.imu.setSlerpPower(0.02)
        self.imu.setGyroEnable(True)
        self.imu.setAccelEnable(True)
        self.imu.setCompassEnable(True)

        if (not self.pressure.pressureInit()):
            print("Pressure sensor Init Failed")
            raise RuntimeError("Could not initilize pressure sensor! Did you check that the sensor is visible via I2C?")
        else:
            print("Pressure sensor Init Succeeded")

        self.poll_interval = self.imu.IMUGetPollInterval()
        print("Recommended Poll Interval: %dmS\n" % self.poll_interval)
        print("IMU init successfully finished!")

        


IMU_SETTINGS_FILE = "IMU_settings"

imu = IMU_Reader(IMU_SETTINGS_FILE)

'''
# ---------  Set up IMU
print("Using settings file " + IMU_SETTINGS_FILE + ".ini")
if not os.path.exists(IMU_SETTINGS_FILE + ".ini"):
    print("Settings file does not exist, will be created")

s = RTIMU.Settings(IMU_SETTINGS_FILE)
imu = RTIMU.RTIMU(s)
pressure = RTIMU.RTPressure(s)

print("IMU Name: " + imu.IMUName())
print("Pressure Name: " + pressure.pressureName())

if (not imu.IMUInit()):
    print("IMU Init Failed")
    sys.exit(1)
else:
    print("IMU Init Succeeded");

# this is a good time to set any fusion parameters

imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

if (not pressure.pressureInit()):
    print("Pressure sensor Init Failed")
else:
    print("Pressure sensor Init Succeeded")

poll_interval = imu.IMUGetPollInterval()
print("Recommended Poll Interval: %dmS\n" % poll_interval)

# ----- read IMU

while True:
    if imu.IMURead():
        # gat Data from IMU
        data = imu.getIMUData()
        (data["pressureValid"], data["pressure"], data["temperatureValid"],
         data["temperature"]) = pressure.pressureRead()
        # accel
        if data["accelValid"] == True:
            print("Accel: ", data["accel"])
        else:
            print("Accel data NOT valid!")
        # gyro
        if data["gyroValid"] == True:
            print("Gyro: ", data["gyro"])
        else:
            print("Gyro data NOT valid!")
        # compass
        if data["compassValid"] == True:
            print("Compass: ", data["compass"])
        else:
            print("Compass data NOT valid!")
        # pressure
        if (data["pressureValid"]):
            print("Pressure: %f" % (data["pressure"]))
        else:
            print("Pressure data NOT valid!")
        # temperature
        if (data["temperatureValid"]):
            print("Temperature: %f" % (data["temperature"]))
        else:
            print("Temperature data NOT valid!")
        # fused position
        print("Fused position: ", data["fusionPose"])


        time.sleep(poll_interval * 1.0 / 1000.0)
'''
