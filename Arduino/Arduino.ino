#include <FastLED.h>

#define NUM_LEDS 86
#define DATA_PIN 13

CRGB leds[NUM_LEDS];
int sum = 0;

void setup() {
  Serial.begin(115200);
  FastLED.addLeds<NEOPIXEL, DATA_PIN>(leds, NUM_LEDS);
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');

    // Find the position of the colon
    int colonIndex = data.indexOf(':');

    // Extract the index part and convert it to an integer
    String indexString = data.substring(0, colonIndex);
    int index = indexString.toInt();

    // Extract the color part and convert it to a hexadecimal integer
    String colorString = data.substring(colonIndex + 1);
    long color = strtol(colorString.c_str(), NULL, 16);

    sum += index;

    setLEDColor(index, color);
  }
  
  if (sum == 3655) {
    FastLED.show();
    sum = 0;
  }
}

void setLEDColor(int index, CRGB color) {
  leds[index] = color;
}
