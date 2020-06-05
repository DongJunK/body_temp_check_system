#include <stdio.h>
#include <stdlib.h>

#include "iotmakers.h"

int main()
{
    char *configFile = "./config/iot_config.txt";
    rc = im_init_with_config_file(configFile);
    if( rc < 0){
        printf("fail im_init_with_config_file()\n");
        return -1;
    }

    
    im_release();
    return 0;
}