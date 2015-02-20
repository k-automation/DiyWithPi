/****************************************************
Weasley Weather Clock example
This Arduino sketch displaying weather conditions based on the 
weather data fetched from a Raspberry Pi

*****************************************************/
#include <avr/pgmspace.h>
#include <Wire.h>
#include "Adafruit_LEDBackpack.h"
#include "Adafruit_GFX.h"
#include "BlinkM_funcs.h"
//Proximity sensor address
#define SENSOR_ADDR_ON_ON    (0x20)
#define REDPIN 2
#define GREENPIN 4
#define BLUEPIN 3
#define FADESPEED 10 

char serInString[10];  
char sevenseg_string[10];
char matrixInString[10];
char color_bit;                       
int  serInIndx  = 0;    
int  serOutIndx = 0;    
//declare variables for the motor pins
//http://forum.arduino.cc/index.php?topic=85335.25;wap2
int motorPin1 = 8;	// Blue   - 28BYJ48 pin 1
int motorPin2 = 9;	// Pink   - 28BYJ48 pin 2
int motorPin3 = 10;	// Yellow - 28BYJ48 pin 3
int motorPin4 = 11;	// Orange - 28BYJ48 pin 4
int temp      = 0;                        // Red    - 28BYJ48 pin 5 (VCC)

int motorSpeed = 0;     //variable to set stepper speed
int steps;

byte blinkm_addr = 0x09; // the default address of all BlinkMs

const uint8_t sensorAddr = SENSOR_ADDR_ON_ON;

Adafruit_8x8matrix matrix = Adafruit_8x8matrix();
Adafruit_7segment matrix_7segment = Adafruit_7segment();


 const int mydata[6][2] PROGMEM = {
     1, 10,
     2, 18,
     3, 28,
     4, 43,
     5, 54,
     6, 66};

//////////////////////////////////////////////////////////////////////////////
void setup() {
  //declare the motor pins as outputs
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(motorPin3, OUTPUT);
  pinMode(motorPin4, OUTPUT);
  
  pinMode(REDPIN, OUTPUT);
  pinMode(GREENPIN, OUTPUT);
  pinMode(BLUEPIN, OUTPUT);
  Serial.begin(9600);
  
   Wire.begin();
   matrix.begin(0x73);  // pass in the address
   matrix_7segment.begin(0x70);

   WriteByte(sensorAddr, 0x3, 0xFE);

    BlinkM_stopScript( blinkm_addr );
}
//LED Matrix values
static uint8_t __attribute__ ((progmem)) smile_bmp[]={0x3C, 0x42, 0x95, 0xA1, 0xA1, 0x95, 0x42, 0x3C};
static uint8_t __attribute__ ((progmem)) frown_bmp[]={0x3C, 0x42, 0xA5, 0x91, 0x91, 0xA5, 0x42, 0x3C};
static uint8_t __attribute__ ((progmem)) neutral_bmp[]={0x3C, 0x42, 0x95, 0x91, 0x91, 0x95, 0x42, 0x3C};

//////////////////////////////////////////////////////////////////////////////
void loop(){

     uint8_t val;
 //parse incoming message 
 readSerialString();
 //Read stepper data and move stepper 
 if(serInIndx>0)
 {
   int var_serial=serInString[1]-48;
   serInIndx=0;
   if(var_serial>0 && var_serial <=6)
   {
     steps=pgm_read_word_near(&mydata[(var_serial-1)][1]);
     Serial.println(steps);
   }
   if(serInString[0]==43){
   
   motorSpeed=20;
   for(int i=0;i<steps;i++){
     clockwise();
     
   }
   
   Serial.println("The motor is going clockwise");
   
 }
 else if(serInString[0]==45){
   motorSpeed=20;
   for(int j=0; j<steps;j++) {
     counterclockwise();
   }
   Serial.println("The motor is going counterclockwise");
 }
 
 }
 
  // Get the value from the sensor
 if(color_bit=='R'){
   lightsequence_red();
 }
 else if(color_bit=='G'){
   lightsequence_green();
 }
 else if(color_bit=='B'){
   lightsequence_blue();
 }
 
 sevenseg_write();
 
 delay(20);
}
//////////////////////////////////////////////////////////////////////////////
//set pins to ULN2003 high in sequence from 1 to 4
//delay "motorSpeed" between each pin setting (to determine speed)

void counterclockwise (){
  // 1
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, LOW);
  delay(motorSpeed);
  // 2
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, LOW);
  delay (motorSpeed);
  // 3
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, LOW);
  delay(motorSpeed);
  // 4
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin4, LOW);
  delay(motorSpeed);
  // 5
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin4, LOW);
  delay(motorSpeed);
  // 6
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin4, HIGH);
  delay (motorSpeed);
  // 7
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, HIGH);
  delay(motorSpeed);
  // 8
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin4, HIGH);
  delay(motorSpeed);
}

//////////////////////////////////////////////////////////////////////////////
//set pins to ULN2003 high in sequence from 4 to 1
//delay "motorSpeed" between each pin setting (to determine speed)

void clockwise(){
  // 1
  digitalWrite(motorPin4, HIGH);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin1, LOW);
  delay(motorSpeed);
  // 2
  digitalWrite(motorPin4, HIGH);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin1, LOW);
  delay (motorSpeed);
  // 3
  digitalWrite(motorPin4, LOW);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin1, LOW);
  delay(motorSpeed);
  // 4
  digitalWrite(motorPin4, LOW);
  digitalWrite(motorPin3, HIGH);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin1, LOW);
  delay(motorSpeed);
  // 5
  digitalWrite(motorPin4, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin1, LOW);
  delay(motorSpeed);
  // 6
  digitalWrite(motorPin4, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin2, HIGH);
  digitalWrite(motorPin1, HIGH);
  delay (motorSpeed);
  // 7
  digitalWrite(motorPin4, LOW);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin1, HIGH);
  delay(motorSpeed);
  // 8
  digitalWrite(motorPin4, HIGH);
  digitalWrite(motorPin3, LOW);
  digitalWrite(motorPin2, LOW);
  digitalWrite(motorPin1, HIGH);
  delay(motorSpeed);
}
//parse incoming message
void readSerialString () {
    int sb;  
    serInIndx=0;
    if(Serial.available()) { 
       //Serial.print("reading Serial String: ");
       //optional confirmation
       
       char serial_read = Serial.read();
         if(serial_read=='A'){
           Serial.print("A");           
         }
         if(serial_read=='H'){
          reset_stepper();
          lightsequence();
        }
        if(serial_read=='M'){
          sb=Serial.read();
          if(sb-'0'==1) {
            set_display(smile_bmp);
          }
          else if(sb-'0'==2) {
            set_display(frown_bmp);
          }
        }
        
       
        if( serial_read == 'T' ) { 
         while(Serial.available())
         {
          sb = Serial.read();             
          serInString[serInIndx] = sb;
          serInIndx++;
         }
        }
       if(serial_read=='S') {
          while(Serial.available()){
          sb = Serial.read();             
          sevenseg_string[serInIndx] = sb;
          serInIndx++;
          temp=0;
          }
          temp=atoi(sevenseg_string);   
          memset(sevenseg_string,0,9);
        }
       if(serial_read=='R' || serial_read=='G' ||
           serial_read=='B') {
             color_bit=serial_read;          
        }
        if(serial_read== 'o' ) {
          Serial.println("Stop script");
          BlinkM_stopScript( blinkm_addr );
        }
       if( serial_read == 'P' ) {
          while(Serial.available())
           {
            sb = Serial.read();             
            serInString[serInIndx] = sb;
            serInIndx++;
           }
      BlinkM_playScript( blinkm_addr,serInString[0]-48,0,0 );
    }
     
    }
        
  //  
}
// Read a byte on the i2c interface
int ReadByte(uint8_t addr, uint8_t reg, uint8_t *data)
{
   // Do an i2c write to set the register that we want to read from
   Wire.beginTransmission(addr);
   Wire.write(reg);
   Wire.endTransmission();

   // Read a byte from the device
   Wire.requestFrom(addr, (uint8_t)1);
   if (Wire.available())
   {
      *data = Wire.read();
   }
   else
   {
      // Read nothing back
      return -1;
   }

   return 0;
}

// Write a byte on the i2c interface
void WriteByte(uint8_t addr, uint8_t reg, byte data)
{
   // Begin the write sequence
   Wire.beginTransmission(addr);

   // First byte is to set the register pointer
   Wire.write(reg);

   // Write the data byte
   Wire.write(data);

   // End the write sequence; bytes are actually transmitted now
   Wire.endTransmission();
}

void set_display(const uint8_t *bitmap) {
   matrix.clear();
   matrix.setRotation(3);
  matrix.drawBitmap(0, 0, bitmap, 8, 8, LED_ON);
  matrix.writeDisplay();
}

void reset_stepper(void){
  uint8_t val;

   // Get the value from the sensor
   if (ReadByte(sensorAddr, 0x0, &val) == 0)
   {
      // The second LSB indicates if something was not detected, i.e.,
      // LO = object detected, HI = nothing detected
      while(val & 0x2)
      {
         motorSpeed=20;
         Serial.println("Nothing detected");
         if(ReadByte(sensorAddr, 0x0, &val) == 0){
           clockwise();
         }
      }
    
   }
   else
   {
      Serial.println("Failed to read from sensor");
   }

   // Run again in 1 s (1000 ms)
   

}
//startup sequence
void lightsequence(void) {
   int r, g, b;
 
  // fade from blue to violet
  for (r = 0; r < 256; r++) { 
    analogWrite(REDPIN, r);
    delay(FADESPEED);
  } 
  // fade from violet to red
  for (b = 255; b > 0; b--) { 
    analogWrite(BLUEPIN, b);
    delay(FADESPEED);
  } 
  // fade from red to yellow
  for (g = 0; g < 256; g++) { 
    analogWrite(GREENPIN, g);
    delay(FADESPEED);
  } 
  // fade from yellow to green
  for (r = 255; r > 0; r--) { 
    analogWrite(REDPIN, r);
    delay(FADESPEED);
  } 
  // fade from green to teal
  for (b = 0; b < 256; b++) { 
    analogWrite(BLUEPIN, b);
    delay(FADESPEED);
  } 
  // fade from teal to blue
  for (g = 255; g > 0; g--) { 
    analogWrite(GREENPIN, g);
    delay(FADESPEED);
  } 
}
//fade to red
void lightsequence_red(void) {
  int r, g, b;
 
  
  for (r = 0; r < 256; r++) { 
    analogWrite(REDPIN, r);
    delay(FADESPEED);
  } 
    analogWrite(GREENPIN,0);
    analogWrite(BLUEPIN,0);
}
//fade too green
void lightsequence_green(void) {
  int r,g,b;
  /
  for (g = 0; g < 256; g++) { 
    analogWrite(GREENPIN, g);
    delay(FADESPEED);
  } 

  analogWrite(REDPIN,0);
  analogWrite(BLUEPIN,0);

}
//write to seven segment display
void sevenseg_write(void) {
  matrix_7segment.clear();
  matrix_7segment.print(temp, DEC);
  matrix_7segment.writeDisplay();
  delay(500);
}
//blue light sequence
void lightsequence_blue(void) {
  int r,g,b;
 // fade from green to teal
  for (b = 0; b < 256; b++) { 
    analogWrite(BLUEPIN, b);
    delay(FADESPEED);
  } 
   analogWrite(GREENPIN,0);
    analogWrite(REDPIN,0);
}
