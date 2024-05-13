#include<Servo.h>

Servo head;
Servo l_hand;
Servo r_hand;

// Function prototypes
void standby();
void hi();
void double_punch();
void hands_up();
void look_left();
void r_upper_cut();
void smash();

// define sonar sensor's pins
int trig = 4;
int echo = 5;

// received data
byte val; // without initialization

void setup() {
  // put your setup code here, to run once:
  head.attach(2);
  l_hand.attach(3);
  r_hand.attach(4);

  Serial.begin(9600); // for communicating via serial port with Python
}

// Define your functions here...

void standby() {
  // Define standby function
}

void hi() {
  // Define hi function
}

void double_punch() {
  // Define double_punch function
}

void hands_up() {
  // Define hands_up function
}

void look_left() {
  // Define look_left function
}

void r_upper_cut() {
  // Define r_upper_cut function
}

void smash() {
  // Define smash function
}

void loop() {
  // put your main code here, to run repeatedly:
  standby();

  while(Serial.available() > 0)  //look for serial data available or not
  {
    val = Serial.read();        //read the serial value

    if(val == 'h'){
      // do hi
       hi();
    }
    if(val == 'p'){
      // do hi
       double_punch();
    }
    if(val == 'u'){
      hands_up();
      delay(3000);
    }
    if(val == 'l'){
      standby();
      look_left();
      delay(2000);
    }
    if(val == 'U'){
      // uppercut
      r_upper_cut();
      delay(2000);
    }
    if(val == 's'){
      smash();
      delay(2000);
    }
  }
}
