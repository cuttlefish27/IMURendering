#include <Arduino.h>
#include <ESP32Servo.h>

// put function declarations here:
Servo myServo;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  myServo.attach(27, 500, 2400);
  myServo.write(0);
  delay(10);
  myServo.write(100);
}

void loop() {
  if(Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if(cmd == "forward") {
      myServo.write(myServo.read() + 10);
    }
    else if(cmd == "backward") {
      myServo.write(myServo.read() - 10);
    }
  }
}

// put function definitions here:
int myFunction(int x, int y) {
  return x + y;
}