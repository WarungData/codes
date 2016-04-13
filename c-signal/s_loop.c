#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main(void)
{
	int pid;

	pid = getpid();

	while (1)
	{
		fprintf (stdout, "\nI am process with ID: %d. Send me some signals...", pid);

		sleep (1);
	}	

	return 0;
}
