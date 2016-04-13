#include <stdio.h>
#include <signal.h>
#include <sys/types.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>

int main(int argc, char * argv[])
{

	pid_t pid;
	int sig;
	int ret;

	if (argc != 3)
	{
		fprintf (stderr, "Usage %s <pid> <signal_number>\n", argv[0]);
		exit (1);
	}

	pid = atoi (argv[1]);
	sig = atoi (argv[2]);

	ret = kill (pid, sig);
	if (ret != 0)
	{
		fprintf (stderr, "%s\n", strerror(errno));
		exit (errno);
	}
	else
	{

		fprintf (stdout, "%s\n", strerror(errno));
	}

	return 0;

}
