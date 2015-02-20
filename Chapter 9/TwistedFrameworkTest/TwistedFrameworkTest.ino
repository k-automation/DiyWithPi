/*
      Twisted Framework Test example
      This is a test example that sends a test message 
      to the twisted server launched on the Raspberry Pi
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

  delay(1000);

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
}

void loop()
{
   //Nothing to do here
  
}
