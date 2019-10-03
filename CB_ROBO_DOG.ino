/****************************************************/
/* THIS FILE IS STILL A WORK IN PROGRESS
/* CREATED 10/03/2019 - BY ALFRED MARTINEZ
/*
/****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  500 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  600 // this is the 'maximum' pulse length count (out of 4096)

uint8_t HIPservo0 = 0;//      *
uint8_t HIPservo1 = 4;//      * 
uint8_t HIPservo2 = 8;//      *
uint8_t HIPservo3 = 12;//     *
uint8_t THIGHservo0 = 1;//    *
uint8_t THIGHservo1 = 5;//    *
uint8_t THIGHservo2 = 9;//    *
uint8_t THIGHservo3 = 13;//   *
uint8_t KNEEservo0 = 2;//     *
uint8_t KNEEservo1 = 6;//     *
uint8_t KNEEservo2 = 10;//    *
uint8_t KNEEservo3 = 14;//    *

void setup() {
  Serial.begin(9600);
  Serial.println("16 channel Servo test!");
  pwm.begin(); 
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates
  delay(10);
}

void loop() {
//***********HIP JOINTS***********************************************************************************//
/************HIP_SERVO_0************/ 
//    pwm.setPWM(HIPservo0,0,220);      //SHOWS 3 PHASES OF LEGS AS AN EXAMPLE ON THE L1 HIP JOINT
//    delay(1000);                      //250 SEEMS TO BE FACING STRAIGHT DOWN AND THE 220/320 SEEM 
//    pwm.setPWM(HIPservo0,0,250);      //TO BE ABOUT 30 DEGREES OUT/IN RESPECTIVELY.
//    delay(1000);                      //
//    pwm.setPWM(HIPservo0,0,320);
//    delay(1000);
/************HIP_SERVO_1************/ 
    pwm.setPWM(HIPservo1,0,0);
/************HIP_SERVO_2************/ 
    pwm.setPWM(HIPservo2,0,0);
/************HIP_SERVO_3************/ 
    pwm.setPWM(HIPservo3,0,0);

//***********THIGH JOINTS*********************************************************************************//
/************THIGH_SERVO_0************/ 
    pwm.setPWM(THIGHservo0,0,0);
    
/************THIGH_SERVO_1************/  
      pwm.setPWM(THIGHservo1,0,0);
//    pwm.setPWM(THIGHservo1,0,100);
//    delay(1000);
//    pwm.setPWM(THIGHservo1,0,300);
//    delay(1000);
///************THIGH_SERVO_2************/ 
      pwm.setPWM(THIGHservo2,0,0);   
//    pwm.setPWM(THIGHservo2,0,200);
//    delay(1000);
//    pwm.setPWM(THIGHservo2,0,425);
//    delay(1000);
/************THIGH_SERVO_3************/    
    pwm.setPWM(THIGHservo3,0,0);

//***********KNEE JOINTS**********************************************************************************// 
/************KNEE_SERVO_0************/ 
//    pwm.setPWM(KNEEservo0,0,0);       //KNEEservo0 IS GIVING A LOT OF TROUBLE
//    delay(1000);                      //IT IS THE ONLY MOTOR WITH A 360 RANGE OF MOTION
//    pwm.setPWM(KNEEservo0,0,4000);    //THIS IS PROBABLY THE REASON
//    delay(1000);                      //
/************KNEE_SERVO_1************/    
//    pwm.setPWM(KNEEservo1,0,200);       //200 == 60DEG FROM TABLE PERPENDICULAR
//    delay(1000);
//    pwm.setPWM(KNEEservo1,0,350);       //350 == 0 DEG FROM TABLE PERPENDICULAR
//    delay(1000); 
//    pwm.setPWM(KNEEservo1,0,500);       //500 == -60DEG FROM TABLE PERPENDICULAR
//    delay(1000); 
/************KNEE_SERVO_2************/ 
//    pwm.setPWM(KNEEservo2,0,175);       //XXX == 60 DEG FROM TABLE PERPENDICULAR
//    delay(1000);
//    pwm.setPWM(KNEEservo2,0,315);       //XXX == 0 DEG FROM TABLE PERPENDICULAR
//    delay(1000); 
//    pwm.setPWM(KNEEservo2,0,475);       //XXX == -60DEG FROM TABLE PERPENDICULAR
//    delay(1000);  
/************KNEE_SERVO_3************/ 
    pwm.setPWM(KNEEservo3,0,0);

//****RANDOM MIX OF TEST CODE*****************************************************************************//
//    pwm.setPWM(THIGHservo1,0,100);
//    pwm.setPWM(THIGHservo2,0,200);  
//    pwm.setPWM(KNEEservo1,0,200);         //MOVES BOTH KNEE JOINTS ON ONE SIDE
//    pwm.setPWM(KNEEservo2,0,175);         //AT THE SAME TIME.  
//    delay(1000);                          // 
//    pwm.setPWM(KNEEservo1,0,350);         //
//    pwm.setPWM(KNEEservo2,0,315);         //
//    delay(1000);                          //
//    pwm.setPWM(THIGHservo1,0,300);
//    pwm.setPWM(THIGHservo2,0,425);
//    pwm.setPWM(KNEEservo1,0,500);         //
//    pwm.setPWM(KNEEservo2,0,475);         //
//    delay(1000);                          //  

}
