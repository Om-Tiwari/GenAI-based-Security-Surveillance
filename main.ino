#include <Servo.h>
#include <SoftwareSerial.h>

// button connection
const int doorbellPin = 2; // Pin connected to the doorbell button
Servo myServo;

// Variable to store the state of the wire connection
bool wireState = false;

void setup()
{
    // Set the wire pin as input with internal pull-up resistor
    pinMode(doorbellPin, INPUT_PULLUP);
    Serial.begin(9600);
    // Attach the Servo object to pin 9
    myServo.attach(9);
    myServo.write(0);
}

void loop()
{
    // Read the state of the wire connection
    bool currentWireState = digitalRead(doorbellPin) == LOW;

    // Check if the wire state has changed
    if (currentWireState != wireState)
    {
        wireState = currentWireState;

        // Move the servo based on the wire state
        if (wireState)
        {
            myServo.write(0);
            Serial.println("DoorbellPressed"); // Send signal when doorbell is pressed
            delay(1000);                       // Debounce delay
        }                                      // Rotate to 180 degrees when wire is connected
        else
        {
            myServo.write(180); // Rotate to 0 degrees when wire is disconnected
        }
    }
}