void setup() {
  Serial.begin(9600);
}

void loop() {

  // String data1 = ".";
  // String data2 = "-";
  // Serial.println(data1);
  // Serial.println(data1);
  // Serial.println(data1);
  // delay(5000);
  // Serial.println(data2);
  // Serial.println(data2);
  // Serial.println(data2);
  // delay(5000);
  // Serial.println(data1);
  // Serial.println(data1);
  // Serial.println(data1);
  // delay(5000);

  double readAnalog = analogRead(A0);
  Serial.println(readAnalog/100);

}
