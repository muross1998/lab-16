
const int ledPin = 13; 

void setup() {
  Serial.begin(9600); 
  pinMode(ledPin, OUTPUT);
  
  Serial.println("Arduino is ready!");
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    if (command == '1') {
      digitalWrite(ledPin, HIGH);   
      Serial.println("LED is ON");  
    }
    else if (command == '0') {
      digitalWrite(ledPin, LOW);    
      Serial.println("LED is OFF"); 
    }
  }
}
