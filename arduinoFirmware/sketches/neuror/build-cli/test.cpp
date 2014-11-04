#include "WProgram.h"
/*
       Neuror - Neuronal Door 
       Door Interface Sketch
       
*/


// Parametros de funcionamiento
    #define PinAnalogico 0
    #define TiempoEntreMuestras 20      // Valor en ms. + lo q toma enviar los 2/3/4/5 bytes por serial.
    #define Tolerancia 7
    #define PinLedIndicador 13
    
    int valorAD;
    int valorMinimo = 1023; // Para forzar una recalibracion
    int i = 0;
  
void setup() {
    Serial.begin(9600); 
    pinMode(PinLedIndicador, OUTPUT);  

    // Serial.println("READY!");
    digitalWrite(PinLedIndicador, HIGH);   // Mostar q ya empieza el programa
    delay(1000);                  
    digitalWrite(PinLedIndicador, LOW);    
    
    
    ////////////////////////////// RUTINA RECALIBRACION /////////////////////////////////////////////////// 
     valorAD = analogRead(PinAnalogico);
    
    if ((valorAD-valorMinimo) <= -(Tolerancia/2)) {  // Hay q recalibrar el minimo
        if ((1023-valorAD) > Tolerancia) {  // Si el minimo esta demasiado cerca del limite superior del CAD no hay q establecerlo tan cerca.
          valorMinimo = valorAD;
        }
        else {
          valorMinimo =1023 - Tolerancia -1;
        }
        digitalWrite(PinLedIndicador, LOW);
        delay(300);  
        digitalWrite(PinLedIndicador, HIGH);   // Prendemos el led para mostar q se recalibro
        delay(300);                  
        digitalWrite(PinLedIndicador, LOW);
        delay(300);   
        digitalWrite(PinLedIndicador, HIGH);   
        delay(300);                  
        digitalWrite(PinLedIndicador, LOW);
        delay(300);   
        digitalWrite(PinLedIndicador, HIGH);   
        delay(300);                  
        digitalWrite(PinLedIndicador, LOW);
        delay(300);  
    }
////////////////////////////// FIN RUTINA RECALIBRACION /////////////////////////////////////////////////// 
}
 
void loop() {

    valorAD = analogRead(PinAnalogico);
    
    if ((valorAD-valorMinimo) >= Tolerancia) {
    
        digitalWrite(PinLedIndicador, LOW);
        
        while((valorAD-valorMinimo) >= Tolerancia){                                                            
          Serial.print(valorAD);
          Serial.println();
          delay(TiempoEntreMuestras);
          valorAD = analogRead(PinAnalogico);
        } 
        
        Serial.print("x");  // Esto indica el fin da la transmision.
        Serial.println();
        digitalWrite(PinLedIndicador, HIGH);  
    }

    delay(10);    
  
}
