/*
      Raspberry Pi Buzzer Trigger example
      This is a test example that sends a test message 
      to trigger a buzzer on the Raspberry Pi
*/
#include <Ethernet.h>
#include <SPI.h>

//MAC Address of the Arduino
byte mac[] = { 0x90, 0xA2, 0xDA, 0x0F, 0x02, 0xFC };
//IP Address of the Raspberry Pi
IPAddress server( 192, 168, 1, 89); 

EthernetClient client;

void setup()
{
  Ethernet.begin(mac);
  Serial.begin(9600);

}

void loop()
{
   Serial.println("connecting...");

  if (client.connect(server, 8000)) {
    Serial.println("connected");
    client.println("Hello, World!");
    client.println();
    //Lets wait for the client to read and 
    //echo the message
    //Note: A second's delay is a bit excessive
    delay(1000);
    //If there is a response from the server
    //echo back the message
     Serial.println("Server says:");
     while(client.available()) {
      char c = client.read();
      Serial.print(c);
    }
    client.stop();
    Serial.println("Client Disconnected");
  } else {
    Serial.println("connection failed");
  }
  
  //Wait for 60 minutes
  for(uint8_t i=0;i<60;i++){
    for(uint8_t j=0;j<60;j++){
      delay(1000);
    }
  }
  
}
