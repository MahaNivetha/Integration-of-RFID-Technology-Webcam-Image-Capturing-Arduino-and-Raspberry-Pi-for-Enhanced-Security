#include <SPI.h> // SPI
#include <MFRC522.h> // RFID

#define SS_PIN 10
#define RST_PIN 9
    
// Déclaration 
MFRC522 rfid(SS_PIN, RST_PIN); 

byte nuidPICC[4];

const int buzzerPin = 2;

void setup() 
{ 
  // Init RS232
  Serial.begin(9600);

  // Init SPI bus
  SPI.begin(); 

  // Init MFRC522 
  rfid.PCD_Init(); 

  pinMode(buzzerPin, OUTPUT);
}
 
void loop() 
{

  noTone(buzzerPin);
  
  if ( !rfid.PICC_IsNewCardPresent())
    return;

  if ( !rfid.PICC_ReadCardSerial())
    return;
 
  for (byte i = 0; i < 4; i++) 
  {
    nuidPICC[i] = rfid.uid.uidByte[i];
  }

  for (byte i = 0; i < 4; i++) 
  {
    Serial.print(nuidPICC[i]);

  }
  Serial.println();
  tone(buzzerPin, 262, 500);
  delay(500);

  rfid.PICC_HaltA(); // Halt PICC
  rfid.PCD_StopCrypto1(); // Stop encryption on PCD
}
