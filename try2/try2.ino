 

void setup()
{
  Serial.begin(9600);
 pinMode(9,0);  
}

void loop() 
{
  while(Serial.available()>0 )
    {
      int a=Serial.parseInt();
      Serial.println(a);
      if ( Serial.read()== '\n' )
      {
        a=constrain(a,0,180);
       analogWrite(9,a);
      }
      }


   
}

