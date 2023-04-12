from asyncio import sleep
import msgTwilio
import attachMail
import subprocess
import datetime
from mpu6050 import mpu6050

# Set up MPU6050 sensor
sensor = mpu6050(0x68)

def recordVideo(filename):
    # Set the output filename and duration
    duration = 5
    resolution = '640x480'

    # Define the command to start the video recording
    command = ['ffmpeg', '-t', '-s', resolution, str(duration), '-f', 'video4linux2', '-i', 'dev/video0', filename]
    # Start the recording process
    process = subprocess.Popen(command)

    # Wait for the recording to finish
    process.wait()

    print("Saved video.....")

def getAcclerAndGyro():
    # Wait for any tilt or acceleration
    while True:
        acceleration_data = sensor.get_accel_data()
        gyroscope_data = sensor.get_gyro_data()
        acceleration_threshold = 1.0  # Set acceleration threshold here
        tilt_threshold = 1.0  # Set tilt threshold here

        if (abs(acceleration_data['x']) > acceleration_threshold or
                abs(acceleration_data['y']) > acceleration_threshold or
                abs(acceleration_data['z']) > acceleration_threshold or
                abs(gyroscope_data['x']) > tilt_threshold or
                abs(gyroscope_data['y']) > tilt_threshold or
                abs(gyroscope_data['z']) > tilt_threshold):
            

            # recording video for 5 second
            filename = 'video.mp4'
            recordVideo(filename=filename)

            # sending recorded file with mail
            attachMail.send(filename)

            # sending msg
            #msgTwilio.sendMsg()

        else:
            print("Waiting for motion...")

        sleep(3)

if __name__== '__main__':
    getAcclerAndGyro()