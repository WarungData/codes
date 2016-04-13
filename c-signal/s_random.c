#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void print_random_number(void)
{
	int number;

	number = rand();

	fprintf (stdout, "\nRandom number: %d", number);
}

void signal_handler (int signal)
{
	print_random_number();
}

int main(void)
{
	int pid;

	struct sigaction signal_action;

	pid = getpid();
	
	signal_action.sa_handler = signal_handler;	
	signal_action.sa_flags = 0;
	
	sigaction (SIGUSR1, &signal_action, NULL);

	fprintf (stdout, "I am process with ID: %d. Waiting for signal USR1...\n\n", pid);

	while (1)
	{
	}

	return 0;
}

