#include <Servo.h>
#include <ros.h>
#include <std_msgs/Float64.h>
#include "sensor_msgs/JointState.h"

ros::NodeHandle nh;
Servo myservo1, myservo2, myservo3;

float angle[3] = {0, 0, 0}; // Servo açıları (derece cinsinden)

void cmd_cb(const sensor_msgs::JointState& cmd_arm) {
  // Gelen radyan değerlerini dereceye çevir
  angle[0] = constrain((cmd_arm.position[0] + 1.5708) * (180.0 / 3.14159), 0, 180); // Servo 1: -π/2 → 0, +π/2 → 180
  angle[1] = 180 - constrain((cmd_arm.position[1] + 1.5708) * (180.0 / 3.14159), 0, 180); // Servo 2: -π/2 → 0, +π/2 → 180
  angle[2] = constrain((cmd_arm.position[2] + 1.5708) * (180.0 / 3.14159), 0, 360); // Servo 3: -π/2 → 0, +π/2 → 180
}

ros::Subscriber<sensor_msgs::JointState> sub("/joint_states", &cmd_cb);

void setup() {
  myservo1.attach(9);  // Servo 1 pin
  myservo2.attach(10); // Servo 2 pin
  myservo3.attach(11); // Servo 3 pin

  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  // Servo motorlara açı değerlerini gönder
  myservo1.write(angle[0]);          // Servo 1 için normal gönderim
  myservo2.write(angle[1]);    // Servo 2 için ters çevrilmiş açı
  myservo3.write(angle[2]);          // Servo 3 için normal gönderim

  nh.spinOnce();
  delay(10); // Mesaj gönderim hızını sınırlamak için küçük bir gecikme
}
