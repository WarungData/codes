#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>

void signal_handler (int signal)
{
	fprintf (stdout, "\nCaught signal number %d\n", signal);

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

	fprintf (stdout,"I am %d. Sleeping for 10 secs. Try send me some signals...\n", pid);

	sleep (10);

	return 0;
}
