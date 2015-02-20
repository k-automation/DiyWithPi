TCPClient client;
// IP Address of the Raspberry Pi
byte server[] = { 192, 168, 1, 89 }; 
void setup()
{
  Serial.begin(9600);

  while(!Serial.available()) SPARK_WLAN_Loop();


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
