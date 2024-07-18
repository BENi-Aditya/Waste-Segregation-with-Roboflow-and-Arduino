import serial
import time

# Establish a serial connection
serial_device_name = '/dev/cu.usbserial-2140'  # Replace with your correct serial port
time.sleep(2)  # Wait for the connection to establish

# Send command to move the servo
serial_device_name.write(b'M')  # Send 'M' command to Arduino
print("Command sent to move servo to 45 degrees")

# Wait for a response from Arduino
while True:
    if serial_device_name.in_waiting > 0:
        response = serial_device_name.readline().decode('utf-8').strip()
        print(f"Arduino response: {response}")
        break

# Close the serial connection
serial_device_name.close()