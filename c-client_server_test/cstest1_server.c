#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#define PORT 27111
#define MAXLEN 255

int main()
{
	int sock;
	int bindres;
	int yes = 1;
	int maxlen = 255;
	char msg[maxlen];
	int cli_len;
	int rc;
	struct sockaddr_in serv_addr, cli_addr;

	sock = socket (PF_INET, SOCK_DGRAM, 0);
	if (sock < 0)
	{
		perror ("sock");
		exit (errno);
	}

	serv_addr.sin_family  = AF_INET;
	serv_addr.sin_addr.s_addr = htonl (INADDR_ANY);
	serv_addr.sin_port = htons (port);

	if (setsockopt (sock, SOL_SOCKET, SO_REUSEADDR, &yes, sizeof (int)) < 0)
	{
		perror ("setsockopt");
		exit (errno);
	}

	bindres = bind ( sock, (struct sockaddr *) &serv_addr, sizeof (serv_addr) );
	if (bindres < 0)
	{
		perror ("bind");
		exit (errno);
	}

	fprintf (stdout, "cstest1_server started.\nWaiting on port: %d\n", port);

	while (1)
	{
		memset (msg, 0x0, maxlen);

		cli_len  = sizeof (cli_addr);
		rc = recvfrom (sock, msg, maxlen, MSG_DONTWAIT, (struct sockaddr *) &cli_addr, &cli_len);
		if (rc > 0 && strlen (msg) > 0)
		{
			fprintf (stdout, "%s\n", msg);
		}
	}

	return 0;

}
