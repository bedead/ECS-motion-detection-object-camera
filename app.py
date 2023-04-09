from asyncio import sleep
import msgTwilio
import attachMail
from mpu6050 import mpu6050

# Set up MPU6050 sensor
sensor = mpu6050(0x68)

# Set up PiCamera
camera = picamera.PiCamera()

# Wait for any tilt or acceleration
while True:
    acceleration_data = sensor.get_accel_data()
    gyroscope_data = sensor.get_gyro_data()
    acceleration_threshold = 0.1  # Set acceleration threshold here
    tilt_threshold = 1.0  # Set tilt threshold here

    if (abs(acceleration_data['x']) > acceleration_threshold or
            abs(acceleration_data['y']) > acceleration_threshold or
            abs(acceleration_data['z']) > acceleration_threshold or
            abs(gyroscope_data['x']) > tilt_threshold or
            abs(gyroscope_data['y']) > tilt_threshold or
            abs(gyroscope_data['z']) > tilt_threshold):
        print('Motion detected! Starting video recording...')
        
        # recording video for 5 second
        

        # sending recorded file with mail
        filename = ''
        attachMail.send(filename)
        # sending msg
        msgTwilio.sendMsg()

    else:
        pass

    sleep(5)