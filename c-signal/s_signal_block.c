#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>

int main(void)
{
	sigset_t sigset;
	
	pid_t pid;

	pid = getpid();

	sigemptyset (&sigset);

	sigaddset (&sigset, SIGINT);

	sigprocmask (SIG_BLOCK, &sigset, NULL);

	while (1)
	{
		fprintf (stdout,"I am %d. Try interrupt me...\n", pid);
	}

	return 0;
}
