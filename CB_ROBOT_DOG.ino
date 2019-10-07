/****************************************************/
/* THIS FILE IS STILL A WORK IN PROGRESS
/* CREATED 10/03/2019 - BY ALFRED MARTINEZ
/*
/****************************************************/

#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define SERVOMIN  300 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  500 // this is the 'maximum' pulse length count (out of 4096)
#define MIN_HIP_ANGLE -30     //inner hip motion
#define MAX_HIP_ANGLE  30     //outer hip motion
#define MIN_THIGH_ANGLE  -60  //rear thigh motion
#define MAX_THIGH_ANGLE   60  //forward thigh motion
#define MIN_KNEE_ANGLE -90    //rear knee motion
#define MAX_KNEE_ANGLE  90    //forward knee motion

                                                                //HIP#    
uint8_t HIPservo0 = 0;//      ***********************        ******************
uint8_t HIPservo1 = 4;//      * 1      Front      0 *           * (THIGH#)*  
uint8_t HIPservo2 = 8;//      *                     *           *_________*
uint8_t HIPservo3 = 12;//     *                     *           *         *
uint8_t THIGHservo0 = 1;//    *                     *           *_________*
uint8_t THIGHservo1 = 5;//    *                     *           *         *
uint8_t THIGHservo2 = 9;//    *                     *           * (KNEE#) *
uint8_t THIGHservo3 = 13;//   *                     *            *__________*
uint8_t KNEEservo0 = 2;//     *                     *              *          *
uint8_t KNEEservo1 = 6;//     *                     *                *          *
uint8_t KNEEservo2 = 10;//    * 2       Rear       3*                  **********
uint8_t KNEEservo3 = 14;//    ***********************

uint8_t HIPservo[] = {0, 4, 8, 12};
uint8_t THIGHservo[] = {1, 5, 9, 13};
uint8_t KNEEservo[] = {2, 6, 10, 14};

//HIP ANGLE AND PWM CONVERSIONS
const int hip_pwm_minimum[] = {350, 260, 400, 50};  //inner values
const int hip_pwm_maximum[] = {225, 395, 200, 200};
//THIGH ANGLE AND PWM CONVERSIONS
const int thigh_pwm_minimum[] = {180, 330, 480, 160};
const int thigh_pwm_maximum[] = {400, 100, 220, 380};
//KNEE ANGLE AND PWM CONVERSIONS
const int knee_pwm_minimum[] = {80, 620, 510, 60};
const int knee_pwm_maximum[] = {500, 100, 110, 680};

void setup() {
  Serial.begin(9600);
  Serial.println("16 channel Servo test!");
  pwm.begin(); 
  pwm.setPWMFreq(60);  // Analog servos run at ~60 Hz updates
  delay(10);
}

//resets turn off motors & let them float freely
void reset(){
  resetHips();
  resetThighs();
  resetKnees();
}
void resetHips(){
    pwm.setPWM(HIPservo0,0,0);        
    pwm.setPWM(HIPservo1,0,0); 
    pwm.setPWM(HIPservo2,0,0); 
    pwm.setPWM(HIPservo3,0,0);  
}
void resetThighs(){
    pwm.setPWM(THIGHservo0,0,0);    
    pwm.setPWM(THIGHservo1,0,0);
    pwm.setPWM(THIGHservo2,0,0);
    pwm.setPWM(THIGHservo3,0,0);
}
void resetKnees(){
    pwm.setPWM(KNEEservo0,0,0);
    pwm.setPWM(KNEEservo1,0,0);
    pwm.setPWM(KNEEservo2,0,0);
    pwm.setPWM(KNEEservo3,0,0);
}
void zeroAllMotors(){
  HipAngle(0, 0);
  HipAngle(1, 0);
  HipAngle(2, 0);
  HipAngle(3, 0);
  ThighAngle(0, 0);
  ThighAngle(1, 0);
  ThighAngle(2, 0);
  ThighAngle(3, 0);
  KneeAngle(0, 0);
  KneeAngle(1, 0);
  KneeAngle(2, 0);
  KneeAngle(3, 0);
}
/*steps through pwm signal as an angle!!!*/
/*inputs are servo number[0,3] and delay time in millisec.*/
void HipAngleStepping(int num, int speed){
    int x = 1; //x lets us go forward and backwards
  for(int i = MIN_HIP_ANGLE; i<MAX_HIP_ANGLE;i=i+x){
    int angle_to_pwm = map(i, MIN_HIP_ANGLE, MAX_HIP_ANGLE, hip_pwm_minimum[num], hip_pwm_maximum[num]);
    pwm.setPWM(HIPservo[num],0,angle_to_pwm);
    delay(speed);
  }
  for(int i = MAX_HIP_ANGLE; i>MIN_HIP_ANGLE;i=i-x){
    int angle_to_pwm = map(i, MIN_HIP_ANGLE, MAX_HIP_ANGLE, hip_pwm_minimum[num], hip_pwm_maximum[num]);
    pwm.setPWM(HIPservo[num],0,angle_to_pwm);
    delay(speed);
  }  
}
void HipAngle(int num, int angle){
  int angle_to_pwm = map(angle, MIN_HIP_ANGLE, MAX_HIP_ANGLE, hip_pwm_minimum[num], hip_pwm_maximum[num]);
  pwm.setPWM(HIPservo[num],0,angle_to_pwm);
}
void ThighAngleStepping(int num, int speed){
  int x = 1; //x lets us go forward and backwards
  for(int i = MIN_THIGH_ANGLE; i<MAX_THIGH_ANGLE;i=i+x){
    int angle_to_pwm = map(i, MIN_THIGH_ANGLE, MAX_THIGH_ANGLE, thigh_pwm_minimum[num], thigh_pwm_maximum[num]);
    pwm.setPWM(THIGHservo[num],0,angle_to_pwm);
    delay(speed);
  }
  for(int i = MAX_THIGH_ANGLE; i>MIN_THIGH_ANGLE;i=i-x){
    int angle_to_pwm = map(i, MIN_THIGH_ANGLE, MAX_THIGH_ANGLE, thigh_pwm_minimum[num], thigh_pwm_maximum[num]);
    pwm.setPWM(THIGHservo[num],0,angle_to_pwm);
    delay(speed);
  }  
}
void ThighAngle(int num, int angle){
    int angle_to_pwm = map(angle, MIN_THIGH_ANGLE, MAX_THIGH_ANGLE, thigh_pwm_minimum[num], thigh_pwm_maximum[num]);
    pwm.setPWM(THIGHservo[num],0,angle_to_pwm);
}
void KneeAngleStepping(int num, int speed){
  int x = 1; //x lets us go forward and backwards
  for(int i = MIN_KNEE_ANGLE; i<MAX_KNEE_ANGLE;i=i+x){
    int angle_to_pwm = map(i, MIN_KNEE_ANGLE, MAX_KNEE_ANGLE, knee_pwm_minimum[num], knee_pwm_maximum[num]);
    pwm.setPWM(KNEEservo[num],0,angle_to_pwm);
    delay(speed);
  }
  for(int i = MAX_KNEE_ANGLE; i>MIN_KNEE_ANGLE;i=i-x){
    int angle_to_pwm = map(i, MIN_KNEE_ANGLE, MAX_KNEE_ANGLE, knee_pwm_minimum[num], knee_pwm_maximum[num]);
    pwm.setPWM(KNEEservo[num],0,angle_to_pwm);  
    delay(speed);
  }  
}
void KneeAngle(int num, int angle){
  int angle_to_pwm = map(angle, MIN_KNEE_ANGLE, MAX_KNEE_ANGLE, knee_pwm_minimum[num], knee_pwm_maximum[num]);
  pwm.setPWM(KNEEservo[num],0,angle_to_pwm);
}
void loop() {
//  reset();   // does not reset the legs back to the initial position??
    zeroAllMotors();
//  delay(1000);
//  HipAngle(0, -30);
//  HipAngle(1, -30);
//  HipAngle(2, -30);
//  HipAngle(3, -30);
//  ThighAngle(0, -60);
//  ThighAngle(1, -60);
//  ThighAngle(2, -60);
//  ThighAngle(3, -60);
//  KneeAngle(0, -30);
//  KneeAngle(1, -30);
//  KneeAngle(2, -30);
//  KneeAngle(3, -30);
//  delay(1000);
//  HipAngle(0, 0);
//  HipAngle(1, 0);
//  HipAngle(2, 0);
//  HipAngle(3, 0);
//  ThighAngle(0, 0);
//  ThighAngle(1, 0);
//  ThighAngle(2, 0);
//  ThighAngle(3, 0);
//  KneeAngle(0, 0);
//  KneeAngle(1, 0);
//  KneeAngle(2, 0);
//  KneeAngle(3, 0);
//  delay(1000);
//  HipAngle(0, 30);
//  HipAngle(1, 30);
//  HipAngle(2, 30);
//  HipAngle(3, 30);
//  ThighAngle(0, 60);
//  ThighAngle(1, 60);
//  ThighAngle(2, 60);
//  ThighAngle(3, 60);
//  KneeAngle(0, 30);
//  KneeAngle(1, 30);
//  KneeAngle(2, 30);
//  KneeAngle(3, 30);
//  delay(1000);
  
//  KneeAngleStepping(0, 3);
//  KneeAngleStepping(1, 3);
//  KneeAngleStepping(2, 3);
//  KneeAngleStepping(3, 3);
//  ThighAngleStepping(0, 3);
//  ThighAngleStepping(1, 3);
//  ThighAngleStepping(2, 3);
//  ThighAngleStepping(3, 3);
//  HipAngleStepping(0, 3);
//  HipAngleStepping(1, 3);
//  HipAngleStepping(2, 3);
 // HipAngleStepping(3, 3);
}

//********************************************************************************************************//  
//***********HIP JOINTS***********************************************************************************//
/************HIP_SERVO_0************/ 
//    pwm.setPWM(HIPservo0,0,225);      //         OUTER30/MIDDLE/INNER30
//    delay(1000);                      //HIP_SERVO_0 = (225:280:350)
//    pwm.setPWM(HIPservo0,0,280);      //
//    delay(1000);                      //
//    pwm.setPWM(HIPservo0,0,350);
//   delay(1000);
/************HIP_SERVO_1************/ 
//    pwm.setPWM(HIPservo1,0,360);      //HIP_SERVO_1 =(395:330:260)
//    delay(1000);                      // 
//    pwm.setPWM(HIPservo1,0,330);      //
//    delay(1000);                      //
//    pwm.setPWM(HIPservo1,0,260);
//    delay(1000);
/************HIP_SERVO_2************/ 
//    pwm.setPWM(HIPservo2,0,270);      //HIP_SERVO_2 = (250:305:400)
//    delay(1000);                      // 
//    pwm.setPWM(HIPservo2,0,305);      //
//    delay(1000);                      //
//    pwm.setPWM(HIPservo2,0,380);
//    delay(1000);
/************HIP_SERVO_3************/ 
//    pwm.setPWM(HIPservo3,0,200);      //HIP_SERVO_3 = (200:120:70)
//    delay(1000);                      // 
//    pwm.setPWM(HIPservo3,0,120);      //
//    delay(1000);                      //
//    pwm.setPWM(HIPservo3,0,70);
//    delay(1000);
//********************************************************************************************************//
//***********THIGH JOINTS*********************************************************************************//
/************THIGH_SERVO_0************/ 
                                        //            BACK60/MIDDLE/FORWARD60  
//    pwm.setPWM(THIGHservo0,0,180);    //THIGH_SERVO_0 = (180:280:400)
//    delay(1000);
//    pwm.setPWM(THIGHservo0,0,280);
//    delay(1000);
//    pwm.setPWM(THIGHservo0,0,400);
//    delay(1000);
///************THIGH_SERVO_1************/  
//    pwm.setPWM(THIGHservo1,0,330);    //THIGH_SERVO_1 = (330:210:100)
//    delay(1000);
//    pwm.setPWM(THIGHservo1,0,210);
//    delay(1000);
//    pwm.setPWM(THIGHservo1,0,100);
//    delay(1000);
///************THIGH_SERVO_2************/ 
//    pwm.setPWM(THIGHservo2,0,480);    //THIGH_SERVO_2 = (220:330:480)
//    delay(1000);  
//    pwm.setPWM(THIGHservo2,0,330);
//    delay(1000);
//    pwm.setPWM(THIGHservo2,0,220);
//    delay(1000);
///************THIGH_SERVO_3************/    
//    pwm.setPWM(THIGHservo3,0,160);    //THIGH_SERVO_3 = (160:270:380)
//    delay(1000);
//    pwm.setPWM(THIGHservo3,0,270);
//    delay(1000);
//    pwm.setPWM(THIGHservo3,0,380);      
//    delay(1000);  
///************SIMULTANEOUS THIGH MOVEMENT*************************/
//    pwm.setPWM(THIGHservo0,0,180);        //ALL THIGHS BACK ANGLE     
//    pwm.setPWM(THIGHservo1,0,330);
//    pwm.setPWM(THIGHservo2,0,480);
//    pwm.setPWM(THIGHservo3,0,160);
//    delay(1000);
//    pwm.setPWM(THIGHservo0,0,280);        //ALL THIGHS MIDDLE ANGLE
//    pwm.setPWM(THIGHservo1,0,210);
//    pwm.setPWM(THIGHservo2,0,330);
//    pwm.setPWM(THIGHservo3,0,270);
//    delay(1000);
//    pwm.setPWM(THIGHservo0,0,400);        //ALL THIGHS FRONT ANGLE
//    pwm.setPWM(THIGHservo1,0,100);
//    pwm.setPWM(THIGHservo2,0,220);
//    pwm.setPWM(THIGHservo3,0,380);      
//    delay(1000);
//********************************************************************************************************//
//***********KNEE JOINTS**********************************************************************************// 
/************KNEE_SERVO_0************/          //BACK90:MIDDLE:FORWARD90
//    pwm.setPWM(KNEEservo0,0,100);    //KNEE_SERVO_0 = (100:300:500)
//    delay(1000);                     
//    pwm.setPWM(KNEEservo0,0,300);    
//    delay(1000);  
//    pwm.setPWM(KNEEservo0,0,500);    
//    delay(1000); //
/************KNEE_SERVO_1************/    
//    pwm.setPWM(KNEEservo1,0,670);    //KNEE_SERVO_1 = (150:360:670)
//    delay(1000);
//    pwm.setPWM(KNEEservo1,0,360);      
//    delay(1000); 
//    pwm.setPWM(KNEEservo1,0,150);       
//    delay(1000); 
/************KNEE_SERVO_2************/ 
//    pwm.setPWM(KNEEservo2,0,535);    //KNEE_SERVO_0 = (535:305:110)   
//    delay(1000);
//    pwm.setPWM(KNEEservo2,0,305);       
//    delay(1000); 
//    pwm.setPWM(KNEEservo2,0,110);       
//    delay(1000);  
/************KNEE_SERVO_3************/ 
//    pwm.setPWM(KNEEservo3,0,150);      //KNEE_SERVO_0 = (150:360:700)   
//    delay(1000);
//    pwm.setPWM(KNEEservo3,0,360);       
//    delay(1000); 
//    pwm.setPWM(KNEEservo3,0,700);       
//    delay(1000);  




//end of main loop

//********************************************************************************************************//
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

//Lower the angles of each one some and slow it down
//Looking from the back of the dog
////Moves the Front Left Leg
//pwm.setPWM(THIGHservo3,0,200);
//delay(2000);
//pwm.setPWM(KNEEservo3,0,350);   
//delay(2000);
//pwm.setPWM(THIGHservo3,0,300);
//delay(200);
//pwm.setPWM(KNEEservo3,0,200);
//delay(2000);
//
////Moves the Back Right Leg
//pwm.setPWM(THIGHservo1,0,300);
//delay(2000);
//pwm.setPWM(KNEEservo1,0,220); 
//delay(2000);
//pwm.setPWM(THIGHservo1,0,200);
//delay(200);
//pwm.setPWM(KNEEservo1,0,350);
//delay(2000);
//
////Moves the Front Right Leg
//pwm.setPWM(THIGHservo2,0,400);
//delay(2000);
//pwm.setPWM(KNEEservo2,0,250); 
//delay(2000);
//pwm.setPWM(THIGHservo2,0,300);
//delay(200);
//pwm.setPWM(KNEEservo2,0,350);
//delay(2000);
//
////Move Back Left Leg ( Not tested yet) 
//pwm.setPWM(THIGHservo0,0,300);
//delay(2000);
//pwm.setPWM(KNEEservo0,0,500); 
//delay(2000);
//pwm.setPWM(THIGHservo0,0,300);
//delay(200);
//pwm.setPWM(KNEEservo0,0,300); 
//delay(2000);

