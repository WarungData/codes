#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>

int main(void)
{
	sigset_t sigset;
	
	pid_t pid;

	pid = getpid();

	sigfillset (&sigset);

	sigprocmask (SIG_BLOCK, &sigset, NULL);

	fprintf (stdout,"I am screen locker with ID: %d\n", pid);

	while (1);

	return 0;
}
