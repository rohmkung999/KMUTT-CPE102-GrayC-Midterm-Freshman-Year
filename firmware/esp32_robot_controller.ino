/* =========================================================================
 * King Mongkut's University of Technology Thonburi (KMUTT)
 * Department of Computer Engineering | CPE 102 Engineering Exploration
 * Midterm Project: Autonomous Gem-Sorting Robot
 * Group: Gray C
 *
 * Authors:
 *   - May Thu Thu Khaing           (69070503402)
 *   - Nyan Lin Htet                (69070503403)
 *   - Kritapath Tanapholpaiboon    (69070503407)
 *   - Kulchayarat Anuprasert       (69070503410)
 *   - Natthaphat Witthayaphiroonthong (69070503419)
 *   - Thanawat Kongchaiyantr       (69070503421)
 *   - Romteela Chitvuttichot       (69070503440)
 * ========================================================================= */

#include <ESP32Servo.h>

// --- TCS3200 Color Sensor Pins ---
#define S0_PIN 18
#define S1_PIN 19
#define S2_PIN 21
#define S3_PIN 22
#define SENSOR_OUT 23

// --- Motor Driver Pins (Differential Drive) ---
#define MOTOR_LEFT_PWM 25
#define MOTOR_LEFT_DIR 26
#define MOTOR_RIGHT_PWM 27
#define MOTOR_RIGHT_DIR 14

// --- Rubber Band Roller Intake (12V Drive) ---
#define ROLLER_MOTOR_PWM 12

// --- Single Gem Outlet Servo Gate ---
#define GATE_SERVO_PIN 13

Servo dropperServo;

void setup() {
  Serial.begin(115200);

  // Sensor Pin Setup
  pinMode(S0_PIN, OUTPUT);
  pinMode(S1_PIN, OUTPUT);
  pinMode(S2_PIN, OUTPUT);
  pinMode(S3_PIN, OUTPUT);
  pinMode(SENSOR_OUT, INPUT);

  // Set TCS3200 Frequency to 20%
  digitalWrite(S0_PIN, HIGH);
  digitalWrite(S1_PIN, LOW);

  // Motor Driver Setup
  pinMode(MOTOR_LEFT_PWM, OUTPUT);
  pinMode(MOTOR_LEFT_DIR, OUTPUT);
  pinMode(MOTOR_RIGHT_PWM, OUTPUT);
  pinMode(MOTOR_RIGHT_DIR, OUTPUT);
  pinMode(ROLLER_MOTOR_PWM, OUTPUT);

  // Servo Setup
  dropperServo.attach(GATE_SERVO_PIN);
  dropperServo.write(0); // 0 degrees = Closed gate

  Serial.println("[KMUTT CPE102] Gray C Controller Ready.");
}

void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    executeCommand(cmd);
  }
}

void driveChassis(int leftSpeed, int rightSpeed) {
  digitalWrite(MOTOR_LEFT_DIR, leftSpeed >= 0 ? HIGH : LOW);
  analogWrite(MOTOR_LEFT_PWM, constrain(abs(leftSpeed), 0, 255));

  digitalWrite(MOTOR_RIGHT_DIR, rightSpeed >= 0 ? HIGH : LOW);
  analogWrite(MOTOR_RIGHT_PWM, constrain(abs(rightSpeed), 0, 255));
}

void dropSingleStone() {
  Serial.println("[GATE] Opening singulation gate...");
  dropperServo.write(55); // Release position
  delay(380);             // Calibrated time window for 1 stone
  dropperServo.write(0);  // Close
  Serial.println("[GATE] Gate locked.");
}

void executeCommand(char cmd) {
  switch (cmd) {
    case 'F': driveChassis(200, 200); break;   // Forward
    case 'B': driveChassis(-200, -200); break; // Backward
    case 'L': driveChassis(-150, 150); break;  // Pivot Left
    case 'R': driveChassis(150, -150); break;  // Pivot Right
    case 'S': driveChassis(0, 0); break;       // Stop
    case 'I': analogWrite(ROLLER_MOTOR_PWM, 255); break; // Roller ON
    case 'i': analogWrite(ROLLER_MOTOR_PWM, 0); break;   // Roller OFF
    case 'D': dropSingleStone(); break;        // Eject 1 stone
  }
}
