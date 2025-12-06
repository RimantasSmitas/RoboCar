/* AiLightsArduino.ino

  Controls 4 LEDs with PWM on an Arduino (Uno-compatible pins by default).

  Behavior:
  - All LEDs are ON by default (full brightness).
  - Repeatedly choose 3 unique LEDs at random and fade them OUT.
  - After reaching OFF, each chosen LED remains OFF for a random duration
    between 1 and 5 seconds, then fades back IN.
  - Uses non-blocking timing (millis) so fades and waits overlap and the
    sketch remains responsive.

  Wiring:
  - Connect four LEDs (with current-limiting resistors) to the PWM pins
    defined in LED_PINS below. The pins listed are suitable for Arduino Uno.

  Uploading:
  - Open this sketch in the Arduino IDE and upload to your board.

*/

// --- Configuration ---
const uint8_t LED_COUNT = 4;
const uint8_t LED_PINS[LED_COUNT] = {11, 10, 9, 6}; // PWM-capable pins on Uno

const uint8_t FULL_BRIGHT = 255; // PWM max
const unsigned long FADE_MS = 500; // fade duration in milliseconds
const unsigned long SELECT_INTERVAL_MS = 700; // how often to try selecting LEDs

// Off duration range (milliseconds)
const unsigned long OFF_MIN_MS = 1000ul;
const unsigned long OFF_MAX_MS = 5000ul;

enum LedState { LS_ON, LS_FADING_OUT, LS_OFF_WAIT, LS_FADING_IN };

struct Led {
  uint8_t pin;
  LedState state;
  uint8_t brightness; // 0..255
  unsigned long transStart; // millis when fade started
  unsigned long transDur;   // fade duration
  unsigned long offUntil;   // millis until which LED stays off
};

Led leds[LED_COUNT];

unsigned long lastSelect = 0;

// --- Utilities ---
unsigned long randRange(unsigned long a, unsigned long b) {
  return a + (unsigned long)(random(0, 10000)) * (b - a) / 10000ul;
}

// Start fading out a given LED (non-blocking)
void startFadeOut(Led &L) {
  if (L.state == LS_ON) {
    L.state = LS_FADING_OUT;
    L.transStart = millis();
    L.transDur = FADE_MS;
  }
}

// Start fading in a given LED (non-blocking)
void startFadeIn(Led &L) {
  if (L.state == LS_OFF_WAIT) {
    L.state = LS_FADING_IN;
    L.transStart = millis();
    L.transDur = FADE_MS;
  }
}

// Update LED transient (call frequently from loop)
void updateLed(Led &L, unsigned long now) {
  switch (L.state) {
    case LS_ON:
      // ensure full brightness
      if (L.brightness != FULL_BRIGHT) {
        L.brightness = FULL_BRIGHT;
        analogWrite(L.pin, L.brightness);
      }
      break;

    case LS_FADING_OUT: {
      unsigned long dt = now - L.transStart;
      if (dt >= L.transDur) {
        L.brightness = 0;
        analogWrite(L.pin, 0);
        // set off wait duration
        unsigned long offMs = randRange(OFF_MIN_MS, OFF_MAX_MS);
        L.offUntil = now + offMs;
        L.state = LS_OFF_WAIT;
      } else {
        float p = (float)dt / (float)L.transDur;
        uint8_t b = (uint8_t)((1.0 - p) * (float)FULL_BRIGHT);
        L.brightness = b;
        analogWrite(L.pin, L.brightness);
      }
      break;
    }

    case LS_OFF_WAIT:
      if (now >= L.offUntil) {
        startFadeIn(L);
      }
      break;

    case LS_FADING_IN: {
      unsigned long dt = now - L.transStart;
      if (dt >= L.transDur) {
        L.brightness = FULL_BRIGHT;
        analogWrite(L.pin, L.brightness);
        L.state = LS_ON;
      } else {
        float p = (float)dt / (float)L.transDur;
        uint8_t b = (uint8_t)(p * (float)FULL_BRIGHT);
        L.brightness = b;
        analogWrite(L.pin, L.brightness);
      }
      break;
    }
  }
}

// Pick up to `count` unique LEDs that are currently ON and start fading them out
void pickAndStartFadeOut(uint8_t count) {
  // gather indices of LEDs eligible (state == LS_ON)
  uint8_t avail[LED_COUNT];
  uint8_t n = 0;
  for (uint8_t i = 0; i < LED_COUNT; ++i) {
    if (leds[i].state == LS_ON) {
      avail[n++] = i;
    }
  }
  if (n == 0) return;

  // shuffle by selecting random indices
  for (uint8_t k = 0; k < count && n > 0; ++k) {
    uint8_t pickIndex = random(0, n);
    uint8_t ledIndex = avail[pickIndex];
    startFadeOut(leds[ledIndex]);
    // remove picked element from avail
    avail[pickIndex] = avail[n - 1];
    --n;
  }
}

void setup() {
  // seed random with an unconnected analog pin for some entropy
  randomSeed(analogRead(A0));

  for (uint8_t i = 0; i < LED_COUNT; ++i) {
    leds[i].pin = LED_PINS[i];
    leds[i].state = LS_ON;
    leds[i].brightness = FULL_BRIGHT;
    leds[i].transStart = 0;
    leds[i].transDur = FADE_MS;
    leds[i].offUntil = 0;
    pinMode(leds[i].pin, OUTPUT);
    analogWrite(leds[i].pin, leds[i].brightness);
  }

  lastSelect = millis();
}

void loop() {
  unsigned long now = millis();

  // update all LEDs
  for (uint8_t i = 0; i < LED_COUNT; ++i) {
    updateLed(leds[i], now);
  }

  // Try selecting three LEDs at configured interval
  if (now - lastSelect >= SELECT_INTERVAL_MS) {
    pickAndStartFadeOut(3);
    lastSelect = now;
  }

  // small sleep to reduce CPU usage
  delay(10);
}
