import serial
import time

arduino_port = 'COM3' 
baud_rate = 9600

try:
    print(f"Підключення до {arduino_port}...")
    ser = serial.Serial(arduino_port, baud_rate, timeout=1)

    time.sleep(2) 
    print("З'єднання встановлено!\n")

    if ser.in_waiting > 0:
        print("Arduino каже:", ser.readline().decode('utf-8').strip())

    print("\nВідправляємо команду '1' (Увімкнути)...")
    ser.write(b'1')
    time.sleep(0.5) 

    response_on = ser.readline().decode('utf-8').strip()
    print("Відповідь від Arduino:", response_on)

    time.sleep(2) 

    print("\nВідправляємо команду '0' (Вимкнути)...")
    ser.write(b'0')
    time.sleep(0.5)

    response_off = ser.readline().decode('utf-8').strip()
    print("Відповідь від Arduino:", response_off)

    ser.close()
    print("\nЗ'єднання закрито. Тест успішний!")

except serial.SerialException as e:
    print(f"Помилка підключення: {e}\nПеревір, чи правильний COM-порт вказано у коді та чи не відкритий Serial Monitor у Arduino IDE.")
