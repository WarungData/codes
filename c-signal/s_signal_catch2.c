#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>

int quit = 0;

void signal_handler (int signal)
{
	fprintf (stdout, "\nCaught signal number %d\n", signal);

	if (signal == 3)
	{
		quit = 1;
		fprintf (stdout, "Will quit.\n");
	}
	else
	{
		quit = 0 ;
		fprintf (stdout, "I don't care.\n");
	}
}

int main(void)
{
	struct sigaction signal_action;

	pid_t pid;

	pid = getpid();

	signal_action.sa_handler = signal_handler;
	signal_action.sa_flags = SA_NODEFER;

	sigaction (SIGINT, &signal_action, NULL);
	sigaction (SIGTERM, &signal_action, NULL);
	sigaction (SIGQUIT, &signal_action, NULL);

	fprintf (stdout,"I am %d. Try send me some signals...\n", pid);

	while (quit == 0)
	{

	}

	return 0;
}
