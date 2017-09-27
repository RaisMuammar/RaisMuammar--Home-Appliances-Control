const int Lampu = 12;
const int Kipas = 11;
const int Dispenser = 10;

byte RXBuf[64];

void setup() 
{
  Serial.begin(9600); 
  
  pinMode (Lampu, OUTPUT);   
  pinMode (Kipas, OUTPUT);
  pinMode (Dispenser, OUTPUT);
   
  digitalWrite (Lampu, HIGH);
  digitalWrite (Kipas, HIGH);
  digitalWrite (Dispenser, HIGH);
}

void loop() 
{

  if (Serial.available()) 
  {
    int nBytes = Serial.readBytes(RXBuf,sizeof(RXBuf));
    if (nBytes==1) 
      digitalWrite(Lampu, LOW);
    if (nBytes==2) 
      digitalWrite(Lampu, HIGH);
      
      if (nBytes==3)
        digitalWrite (Kipas, LOW);
      if (nBytes==4)
        digitalWrite (Kipas, HIGH);
        
        if (nBytes==5)
          digitalWrite (Dispenser, LOW);
        if (nBytes==6)
          digitalWrite (Dispenser, HIGH);

          if (nBytes==7)
           {
            digitalWrite (Lampu, HIGH);
            digitalWrite (Kipas, HIGH);
            digitalWrite (Dispenser, HIGH);
           }
   }
}
