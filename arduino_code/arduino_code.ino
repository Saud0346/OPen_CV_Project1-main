
int trig1,echo1,trig2,echo2;
double distance1, duration1,distance2, duration2;
void setup() 
{
  Serial.begin(9600);
  pinMode(trig1,INPUT);
  pinMode(trig2,INPUT);
  pinMode(echo1,OUTPUT);
  pinMode(echo2,OUTPUT);
}
int counter =0;

void loop() 
{

//  // distance1
//    //*******************************
//    digitalWrite(trig1, LOW);
//    delayMicroseconds(2);
//
//    digitalWrite(trig1, HIGH);
//    delayMicroseconds(10);
//    digitalWrite(trig1, LOW);
//
//    duration1 = pulseIn(echo1, HIGH);
//    distance1 = (duration1 * 0.034) / 2;
//    //*******************************
//
//    // distance2
//    //*******************************
//    digitalWrite(trig2, LOW);
//    delayMicroseconds(2);
//
//    digitalWrite(trig2, HIGH);
//    delayMicroseconds(10);
//    digitalWrite(trig2, LOW);
//
//    duration2 = pulseIn(echo2, HIGH);
//    distance2 = (duration2 * 0.034) / 2;
//    //******************************

distance1 = 110;
distance2 = 111;

    if(counter < 35)
    {
      Serial.println("Entry");
//      while(distance1 <100)
//      {
//        delay(1);
//      }
    }

    else if(counter < 50)
    {
      Serial.println("Exit");
//      while(distance1 <100)
//      {
//        delay(1);
//      }
    }
    else
    {
      Serial.println("e");
      
    }
    counter++;
    delay(1000);
 

}
