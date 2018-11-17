#include <Servo.h> 

// MOTOR Inialization Setup
#define MOTORY 9        
#define MOTORX 5    
#define LINEARY_MIN  1000    
#define LINEARY_MAX  2000
#define LINEARX_MIN  1000   
#define LINEARX_MAX  1780  

Servo MotorX, MotorY;

// System Inialization Setup
String protocolString = "";
boolean protocolWait = false;
String parsedString = "";
int startIndex = 0;

bool positionFound = false;
int MotorXPosition = 1450;
int MotorYPosition = 1200;
int rowTop = 0;
int rowBottom;
int colRight = 0;
int colLeft;
double lightInput;
int startY = 1215;
int startX = 1450;
int newX = 0;
int newY = 0;
int currentX = 0;
int timeWait = 10000;
int dpx = 0;
int dpy = 0;

String ledString = "";
String auxString = "";
int auxDuration = 0;
int brightInt = 0;
long brightValue = 0;
long expTime = 0;
int pumpNumb = 0;
int pumpDur = 0;
String totalString = "";

void setup() {
  Serial.begin(9600);
  MotorY.attach(MOTORY , LINEARY_MIN, LINEARY_MAX);  // attaches/activates the linear actuator as a servo object 
  MotorX.attach(MOTORX , LINEARX_MIN, LINEARX_MAX);  // attaches/activates the linear actuator as a servo object
  MotorX.writeMicroseconds(1200);
  MotorY.writeMicroseconds(1200);
  currentX = 1200;
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(2, OUTPUT);
}

void loop() {
//  Serial.println("pass");
  if (Serial.available() > 0) {
    protocolString = Serial.readString();
    Serial.println(protocolString);
    for (int i = 0; i <= protocolString.length(); i++){ // Analyze command string one character at a time
      parsedString = protocolString.substring(i,i+1); 
      if (parsedString == ";"){ // ';' Symbolizes the end of a command
        // Command Key:
        // -------------------------------------------------------------
        // L - Signifies the command to toggle an LED.
        //     Followed by and INTEGER representing the LED Index to toggle.
        //        i.e. The command 'L1;' would toggle the LED in index 1
        // A - Signifies the command to trigger an Auxiliary port
        //     Followed by INTEGER representing the LED Index, as well as the duration to keep port triggered for.
        //        i.e. The command 'A490000;' would trigger the auxiliary LED for 90 s
        // -------------------------------------------------------------
        // C - Signifies the command to perform a step from the calibration protocol
        //     Followed by a LETTER representing the step which to perform and then an INTEGER representing 
        //     whether the plate has 24 wells or 96 wells.
        //     Calibration Step Key:
        //        F - Find Limits: This finds the bottom, top, left & right boundaries of the plate as well 
        //            as the step size between wells (dpx & dpy)
        //              i.e. CF; Performs the step. 
        //        T - Tune Center: This goes to the specified well position and tunes the center position by 
        //            finding the boundaries of the well and calculating the horizantel and vertical midpoints.
        //            Followed by the center position to tune.
        //              i.e. CT1060.001160.00; This would move the Motor X to position 1060.00 and Motor Y to 
        //                   position 10160.00 and perform the tuning step.
        //        P - Signifies the command to get the current Photodiode value
        //              i.e. CP; Performs the step.
        // -------------------------------------------------------------
        // M - Signifies the command to move both motors to the specified positions. 
        //     Followed by the X position and then the Y position as a float value with 2 decimal places.
        //     Motor values can be anywhere from 1000 to 2000 for MOTOR Y, and anywhere from 1000 to 1780 
        //     for MOTOR X. 
        //        i.e. M1060.001160.00; This will move Motor X to position 1060.00 and Motor Y to position 1160.00
        // -------------------------------------------------------------
        // S - Signifies the command to move both motors in a shaking pattern
        //
        if (protocolString.substring(startIndex, startIndex+1) == "L"){
          totalString = protocolString.substring(startIndex,i);
          Serial.println(totalString.length());
          if (totalString.length() <= 2){
            ledString = protocolString.substring(startIndex+1,i);
            if (ledString == "5"){
              digitalWrite(6, !digitalRead(6));
              }
            else if (ledString == "1"){
              digitalWrite(8, !digitalRead(8));
              
              }
            else if (ledString == "2"){
              digitalWrite(7, !digitalRead(7));
              }
            else if (ledString == "3"){
              digitalWrite(4, !digitalRead(4));
              }
            else if (ledString == "4"){
              digitalWrite(2, !digitalRead(2));
              }
          }
          else if (totalString.length() > 2){
            ledString = protocolString.substring(startIndex+1,i);
            if (ledString.substring(0,1) == "1"){
              digitalWrite(8, !digitalRead(8));
              Serial.println("LED 1 ON");
            }
            if (ledString.substring(1,2) == "1"){
              digitalWrite(7, !digitalRead(7));
              Serial.println("LED 2 ON");
            }
            if (ledString.substring(2,3) == "1"){
              digitalWrite(4, !digitalRead(4));
              Serial.println("LED 3 ON");
            }            
          }
          Serial.println("done");           
          }
        if (protocolString.substring(startIndex, startIndex+1) == "A"){
          totalString = protocolString.substring(startIndex,i);
          auxString = protocolString.substring(startIndex+1,startIndex+2);
          auxDuration = (protocolString.substring(startIndex+2,i)).toInt();
          if (auxString == "1"){
            digitalWrite(10, HIGH);
            delay(auxDuration);
            digitalWrite(10, LOW);
            }
          else if (auxString == "2"){
            digitalWrite(8, !digitalRead(8));
            digitalWrite(7, !digitalRead(7));
            digitalWrite(4, !digitalRead(4));
            delay(auxDuration);
            digitalWrite(8, !digitalRead(8));
            digitalWrite(7, !digitalRead(7));
            digitalWrite(4, !digitalRead(4));
//            digitalWrite(11, HIGH);
//            delay(auxDuration);
//            digitalWrite(11, LOW);            
            }
          else if (auxString == "3"){
            digitalWrite(12, HIGH);
            delay(auxDuration);
            digitalWrite(12, LOW);     
            }
          else if (auxString == "4"){
            digitalWrite(2, HIGH);
            delay(auxDuration);
            digitalWrite(2, LOW);     
            }
          Serial.println("done");           
          }
         else if (protocolString.substring(startIndex, startIndex+1) == "C"){
          if (protocolString.substring(startIndex+1, i-1) == "F"){
              MotorY.writeMicroseconds(1450);
              MotorYPosition = 1450;
              if (protocolString.substring(startIndex+2, i) == "1"){
                  MotorX.writeMicroseconds(1450);
                  MotorXPosition = 1450;
               }
              else if (protocolString.substring(startIndex+2, i) == "2"){
                  MotorX.writeMicroseconds(1425);
                  MotorXPosition = 1425;
               }
              delay(5000);
              rowTop = findRow("TOP");
              MotorY.writeMicroseconds(1150);
              MotorYPosition = 1150;
              if (protocolString.substring(startIndex+2, i) == "1"){
                  MotorX.writeMicroseconds(1450);
                  MotorXPosition = 1450;
               }
              else if (protocolString.substring(startIndex+2, i) == "2"){
                  MotorX.writeMicroseconds(1425);
                  MotorXPosition = 1425;                  
               }
              delay(5000);
              rowBottom = findRow("BOTTOM");
              MotorY.writeMicroseconds(1325);
              MotorX.writeMicroseconds(1550);
              MotorYPosition = 1325;
              MotorXPosition = 1550;
              delay(5000);
              colRight = findCol("RIGHT");
              MotorXPosition = startX;
              MotorY.writeMicroseconds(1250);
              MotorX.writeMicroseconds(1150);
              MotorYPosition = 1220;
              MotorXPosition = 1150;
              delay(5000);
              colLeft = findCol("LEFT");
              MotorXPosition = startX;
              MotorY.writeMicroseconds(startY);
              MotorX.writeMicroseconds(startX);
              if (protocolString.substring(startIndex+2, i) == "1"){
                dpy = (rowTop - rowBottom)/3.0;
                dpx = (colRight - colLeft)/5.0;
               }
              else if (protocolString.substring(startIndex+2, i) == "2"){
                dpy = (rowTop - rowBottom)/7.0;
                dpx = (colRight - colLeft)/11.0;
               }
              Serial.print(dpx);
              Serial.print(";");
              Serial.print(dpy);
              Serial.print(";");
              Serial.print(rowTop);
              Serial.print(";");
              Serial.print(rowBottom);
              Serial.print(";");
              Serial.print(colLeft);
              Serial.print(";");
              Serial.println(colRight);
            }
            else if(protocolString.substring(startIndex+1, startIndex+2) == "T"){
              newX = protocolString.substring(startIndex+2,i-4).toInt();
              newY = protocolString.substring(startIndex+6,i).toInt();
              MotorX.writeMicroseconds(newX);
              MotorY.writeMicroseconds(newY);
              delay(7000);
              int centerX = calculateHorizontalCenter(newX, newY);
              delay(2000);
              MotorX.writeMicroseconds(centerX);
              MotorY.writeMicroseconds(newY);
              delay(2000);
              int centerY = calculateVerticalCenter(centerX, newY);
              delay(2000);
              MotorX.writeMicroseconds(1200);
              MotorY.writeMicroseconds(1200);
              delay(3000);
              MotorX.writeMicroseconds(centerX);
              MotorY.writeMicroseconds(centerY);
              Serial.print(centerX);
              Serial.print(';');
              Serial.println(centerY);                            
            }
          }
        else if(protocolString.substring(startIndex, startIndex+1) == "M"){
          newX = protocolString.substring(startIndex+1,i-7).toInt();
          newY = protocolString.substring(startIndex+8,i).toInt();
          int search_valX = 645-(((newX - 1000.00)/1000.00)*645);
          int search_valY = 645-(((newY - 1000.00)/1000.00)*645);
          MotorX.writeMicroseconds(newX);
          MotorY.writeMicroseconds(newY);
          int waitX = 1;
          int waitY = 1;
          int old_X = analogRead(A5);
          int old_Y = analogRead(A4);
          int feedback_X;
          int feedback_Y;
          int count_X = 0;
          int count_Y = 0;
          while((waitX == 1) || (waitY == 1)){
            feedback_X = analogRead(A5);
            feedback_Y = analogRead(A4);
            if((feedback_X < old_X+2) && (feedback_X > old_X - 2)){
               count_X += 1;
               if(count_X == 5){
                waitX = 0;
               }
               
            }
            if((feedback_Y < old_Y+2) && (feedback_Y > old_Y - 2)){
               count_Y += 1;
               if(count_Y == 5){
                waitY = 0;
               }
            }
            old_X = feedback_X;
            old_Y = feedback_Y;
            delay(150);
          }
          Serial.println("done");
        }
        else if(protocolString.substring(startIndex, startIndex+1) == "S"){
          MotorX.writeMicroseconds(1200);
          MotorY.writeMicroseconds(1200);
          delay(500);
          int starttime = millis();
          int endtime = starttime;
          int shake_dir = 1;
          while ((endtime - starttime) <= 5000)
          {
          if(shake_dir == 1) {
            MotorX.writeMicroseconds(1600);
            shake_dir = 2;
          }
          else if(shake_dir == 2){
            MotorX.writeMicroseconds(1200);
            shake_dir = 1;
          }
          delay(500);
          endtime = millis();
          }
          MotorX.writeMicroseconds(1200);
          delay(500);
          Serial.println("done");          
        }
        startIndex = i+1;
       }
    }
  }
  protocolString = "";
  totalString = "";
  parsedString = "";
  startIndex = 0;
  brightInt = 0;
  expTime = 0;
}

int calculateHorizontalCenter(int Xpos, int Ypos){
  // Move LEFT till light is lost
  int lightOn = 1;
  int currentX = Xpos;
  int newX = 0;
  while (lightOn == 1){
    lightInput = analogRead(A0);
    Serial.println(lightInput);
    if (lightInput >= 700){
      newX = currentX - 2;
      if (newX <= 1780){
        MotorX.writeMicroseconds(newX);
      }
      else{
        newX = 1780;
        MotorX.writeMicroseconds(newX);
      }
      delay(100);
    }
    else if (lightInput < 700){
      lightOn = 0;
    }
    currentX = newX;
  }
  MotorX.writeMicroseconds(Xpos);
  delay(3000);
  int currentX2 = Xpos;
  int newX2 = 0;
  lightOn = 1;
  // Move RIGHT till light is lost
  while (lightOn == 1){
    lightInput = analogRead(A0);
    if (lightInput >= 700){
      newX2 = currentX2 + 2;
      MotorX.writeMicroseconds(newX2);
      delay(100);
    }
    else if (lightInput < 700){
      lightOn = 0;
    }
    currentX2 = newX2;
  }
  int centerHor = int((abs((currentX)-currentX2)/2.0)+(currentX));
  return centerHor;
}

int calculateVerticalCenter(int Xpos, int Ypos){
  // Move DOWN till light is lost
  int lightOn = 1;
  int currentY = Ypos;
  int newY = 0;
  while (lightOn == 1){
    lightInput = analogRead(A0);
    if (lightInput >= 700){
      newY = currentY-2;
      MotorY.writeMicroseconds(newY);
      delay(100);
    }
    else if (lightInput < 700){
      lightOn = 0;
    }
    currentY = newY;
  }
  MotorY.writeMicroseconds(Ypos);
  delay(3000);
  int currentY2 = Ypos;
  int newY2 = 0;
  lightOn = 1;
  // Move UP till light is lost
  while (lightOn == 1){
    lightInput = analogRead(A0);
    if (lightInput >= 700){
      newY2 = currentY2 + 2;
      MotorY.writeMicroseconds(newY2);
      delay(100);
    }
    else if (lightInput < 700){
      lightOn = 0;
    }
    currentY2 = newY2;
  }
  int centerVert = int((abs(currentY-(currentY2-12))/2.0)+currentY);
  return centerVert;
}

int findRow(String rowDir){
  if (rowDir == "TOP"){
    positionFound = false;
    while (positionFound == false){
      lightInput = analogRead(A0);
      Serial.println(lightInput);
      if (lightInput >= 800){
        positionFound = true;
        break;
      }
      else {
        MotorYPosition = MotorYPosition + 2;
        MotorY.writeMicroseconds(MotorYPosition);
        delay(100);
      }
    }
    return MotorYPosition;
  }
  else if (rowDir == "BOTTOM"){
      positionFound = false;
      while (positionFound == false){
        lightInput = analogRead(A0);
        Serial.println(lightInput);
        if (lightInput >= 800){
          positionFound = true;
          break;
        }
        else {
          MotorYPosition = MotorYPosition - 1;
          MotorY.writeMicroseconds(MotorYPosition);
          delay(100);
        }
      }
      return MotorYPosition;
  }
}

int findCol(String rowDir){
  if (rowDir == "RIGHT"){
    positionFound = false;
    while (positionFound == false){
      lightInput = analogRead(A0);
      Serial.println(lightInput);
      if (lightInput >= 800){
        positionFound = true;
        break;
      }
      else {
        MotorXPosition = MotorXPosition + 1;
        MotorX.writeMicroseconds(MotorXPosition);
        delay(100);
      }
    }
    return MotorXPosition;
  }
  else if (rowDir == "LEFT"){
      positionFound = false;
      while (positionFound == false){
        lightInput = analogRead(A0);
        Serial.println(lightInput);
        if (lightInput >= 800){
          positionFound = true;
          break;
        }
        else {
          MotorXPosition = MotorXPosition - 1;
          MotorX.writeMicroseconds(MotorXPosition);
          delay(100);
        }
      }
      return MotorXPosition;
  }
}
