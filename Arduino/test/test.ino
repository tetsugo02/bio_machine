void setup() {
  Serial.begin(9600);
}

void loop() {

  String data1 = ".";
  String data2 = "-";
  for (int i = 0; i<3; i++) {
      int randNumber = random(300);
    if (randNumber%2==0) {
      Serial.println(".");
    }
    else if (randNumber%3==0) {
      Serial.println("-");
    }
    else {
      Serial.println("None");
    }
  }
  delay(5000);
}
