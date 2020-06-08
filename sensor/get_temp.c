#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include "wiringPi.h"
#include "wiringPiI2C.h"

#define SLAVE_Address 0x3A

const char* get_temp()
{
    int rtc, i;
    int rawTemp[2];
    int count = 0;
    float max=0;
    float sensorTemp[20], objTemp[20];
    char* result = malloc(sizeof(char)*30);

    wiringPiSetup();

    delay(1000);

    if((rtc=wiringPiI2CSetup(SLAVE_Address)) == -1)
    {
        fprintf(stderr, "Unable to initalize I2C : %s\n",strerror(errno));
        return "False";
    }

    while(1){
        for(i=0;i<2;++i){
            rawTemp[i] = wiringPiI2CReadReg16(rtc,0x06+i);
            delay(1);
        }
        sensorTemp[count] = (float)rawTemp[0]*0.02 - 273.15;
        objTemp[count] = (float)rawTemp[1]*0.02 - 273.15;

        //printf("SenT:%3.2f, Obj:%3.2f\n",sensorTemp[count],objTemp[count]);

        delay(500);
		++count;
        if(count == 10) break;
    }

    for(i=0;i<10;++i)
    {
        if(max < objTemp[i])
        {
            max = objTemp[i];
        }
    }
    sprintf(result,"%f",max);

    //printf("%s\n",result);
    return result;
}
