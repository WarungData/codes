#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <sys/types.h>

int main(void)
{
	long int random_number;

	fprintf (stdout, "Set alarm for 1 second\n");
	fprintf (stdout, "Looking for odd number\n");

	alarm (1);
	
	srandom (time(0) * getpid());

	while (1)
	{

		random_number = random();
		
		fprintf (stdout, " %ld ", random_number);

		if (random_number % 2 == 1)
		{
			fprintf (stdout, "\nFound number %ld\n", random_number);
			fprintf (stdout, "\nAlarm cancelled.\n");
			alarm (0);
			return 0;
		}
	}

	return 1;
}
