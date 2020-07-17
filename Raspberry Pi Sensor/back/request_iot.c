#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <string>
#include <string.h>
#include "iotmakers.h"

using namespace std;

static void SigHandler(int sig)
{
	switch(sig)
	{
		case SIGTERM :
		case SIGINT :
			printf("accept signal SIGINT[%d]\n", sig);
			im_stop_service();
			break;
		default :
			;
	};
	return;
} 
static void set_SigHandler()
{
	signal(SIGINT,   SigHandler);	
	signal(SIGTERM,  SigHandler);	
}

/* ============================
main_sample1.c

- Sending the collection data
	im_send_numdata();
	im_send_strdata();
+=========================== */
extern "C" {
int send_log(char* rasp_id, char* person_id, char* temp)
{
	int i;
	int rc;
	string send_value = "";
   	send_value += rasp_id;
   	send_value += "_";
   	send_value += person_id;
	send_value += "_";
   	send_value += temp;
	
	char send_data[200];

	strcpy(send_data, send_value.c_str());	
	printf("%d\n",strlen(rasp_id));
	set_SigHandler();

	printf("im_init()\n");
	rc = im_init_with_config_file("./config/iot_config.txt");

	if ( rc < 0  )	{
		printf("fail im_init()\n");
		return -1;
	}

	im_set_loglevel(LOG_LEVEL_DEBUG);

	printf("im_start_service()...\n");
	rc = im_start_service();
	if ( rc < 0  )	{
		printf("fail im_start_service()\n");
		im_release();
		return -1;
	}

	rc = im_send_strdata("tempInfo", send_data, 0);
	if ( rc < 0  )	{
		printf("ErrCode[%d]\n", im_get_LastErrCode());
	}


	printf("im_stop_service()\n");
	im_stop_service();

	printf("im_release()\n");
	im_release();

	return 0;
}
}

int main(int argc, char* argv[])
{
	if(argc<4)
	{
		return 0;
	}
	send_log(argv[1],argv[2],argv[3]);
	return 0;
}

