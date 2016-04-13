#include <stdio.h>
#include <signal.h>

int main(void)
{
	sigset_t sigset;
	
	sigemptyset (&sigset);

	sigaddset (&sigset, SIGINT);

	if (sigismember (&sigset, SIGTERM))
	{
		fprintf (stdout, "SIGTERM in signal mask\n");
	}
	else
	{

		fprintf (stdout, "SIGTERM NOT in signal mask\n");
	};


	if (sigismember (&sigset, SIGINT))
	{
		fprintf (stdout, "SIGINT in signal mask\n");
	}
	else
	{

		fprintf (stdout, "SIGINT NOT in signal mask\n");
	};


	return 0;
}
