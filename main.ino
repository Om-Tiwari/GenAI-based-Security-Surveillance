#include <SoftwareSerial.h>

const int sensor = 2; // Pin connected to the sensor

// Variable to store the state of the wire connection
bool wireState = false;

void setup()
{
    // Set the wire pin as input with internal pull-up resistor
    pinMode(sensor, INPUT_PULLUP);
    Serial.begin(9600);
}

void loop()
{
    // Read the state of the wire connection
    bool currentWireState = digitalRead(sensor) == LOW;

    // Check if the wire state has changed
    if (currentWireState != wireState)
    {
        wireState = currentWireState;
        if (wireState)
        {
            Serial.println("DoorbellPressed"); // Send signal when doorbell is pressed
        }
    }
}