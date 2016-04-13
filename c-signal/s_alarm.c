#include <stdio.h>
#include <unistd.h>

int main(void)
{
	fprintf (stdout, "Set alarm for 5 seconds\n");
	alarm (5);

	while (1)
	{
		fprintf (stdout, "Idle...\n");
		sleep (1);
	}

	return 0;
}
