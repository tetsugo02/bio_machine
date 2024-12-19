void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  double data_A0 = analogRead(A0)/2;
  double data_A1 = analogRead(A1)/2;

  // Serial.println(data_A0);
  // Serial.println(data_A1);
  Serial.print(data_A0);
  Serial.print(",");
  Serial.println(data_A1);
  delay(100);
}
