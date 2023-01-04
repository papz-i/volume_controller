int pot = A0;
int potVal = 0;

void setup()
{	
  	Serial.begin(9600);
}

void loop()
{
	potVal = analogRead(pot);
  int mappedValue = map(potVal, 1, 1023, 1, 100);
  Serial.println(mappedValue);
  delay(1000);
}

