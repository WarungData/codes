#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>

int quit = 0;

void signal_handler_int(void)
{
	fprintf (stdout, "I am handling SIGINT\n");
	fprintf (stdout, "I don't care.\n");
	quit = 0;
}

void signal_handler_term(void)
{
	fprintf (stdout, "I am handling SIGTERM\n");
	fprintf (stdout, "I don't care.\n");
	quit = 0;
}

void signal_handler_quit(void)
{
	fprintf (stdout, "I am handling SIGQUIT\n");
	fprintf (stdout, "Will quit.\n");
	quit = 1;

}

void signal_handler (int signal)
{
	switch (signal) 
	{
		case 2: signal_handler_int();
			break;
		case 3: signal_handler_quit();
			break;
		case 15: signal_handler_term();
			break;

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
