void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  double readAnalog = analogRead(A0);
  readAnalog = readAnalog/2;
  Serial.println(readAnalog);
  delay(50);
}
