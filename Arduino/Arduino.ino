#include <FastLED.h>

#define NUM_LEDS 86
#define DATA_PIN 13


CRGB leds[NUM_LEDS];


const byte numChars = 15;
char receivedChars[numChars];
char tempChars[numChars];
boolean newData = false;

struct LEDData {
  int index;
  long color;
};


void setup() {
  Serial.begin(115200);
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
  FastLED.clear();
}


void loop() {
  recvWithStartEndMarkers();

  if (newData == true) {
      strcpy(tempChars, receivedChars);
      // Serial.println(tempChars);
      
      struct LEDData currentLEDData = extractLEDData(tempChars);

      setLEDColor(currentLEDData.index, currentLEDData.color);

      newData = false;

      Serial.println("<" + String(currentLEDData.index) + ":" + String(currentLEDData.color) + ">");

      FastLED.show();
  }
}


void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;

    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}


struct LEDData extractLEDData(char line[]) {
  // line: 54:FFFFFF
  struct LEDData data;

  char * strtokIndx;

  strtokIndx = strtok(tempChars, ":");
  data.index = atoi(strtokIndx);

  strtokIndx = strtok(NULL, ":");
  data.color = strtol(strtokIndx, NULL, 16);

  return data;
}


void setLEDColor(int index, CRGB color) {
  leds[index] = color;
}