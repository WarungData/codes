#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main()
{
	int port;
	int sock;
	int bindres;
	int yes = 1;
	int maxlen = 255;
	char msg[maxlen];
	int serv_len;
	int sd;
	struct sockaddr_in serv_addr, cli_addr;

	struct hostent *h;
	char * server_ip;

	port = 27111;

	strcpy (server_ip, "127.0.0.1");

	h = gethostbyname (server_ip);
	serv_addr.sin_family = h -> h_addrtype;
	memcpy ( (char *) &serv_addr.sin_addr.s_addr, h -> h_addr_list[0], h -> h_length);
	serv_addr.sin_port = htons (port);

	sock = socket (PF_INET, SOCK_DGRAM, 0);
	if (sock < 0)
	{
		perror ("sock");
		exit (errno);
	}


	cli_addr.sin_family  = AF_INET;
	cli_addr.sin_addr.s_addr = htonl (INADDR_ANY);
	cli_addr.sin_port = htons (0);

	bindres = bind ( sock, (struct sockaddr *) &cli_addr, sizeof (cli_addr) );
	if (bindres < 0)
	{
		perror ("bind");
		exit (errno);
	}

	while (1)
	{
		strcpy (msg, "TEST");

		serv_len = sizeof (serv_addr);	
		sd = sendto (sock, msg, maxlen, MSG_DONTWAIT, (struct sockaddr *) &serv_addr, &serv_len);

		sleep (1);
	}

	return 0;

}
