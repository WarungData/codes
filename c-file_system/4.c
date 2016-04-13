#include <stdio.h>
#include <unistd.h>

int main (int argc, char * argv[])
{
	if (argc != 2)
	{
		fprintf (stderr, "usage %s <file>\n", argv[0]);
		exit (1);
	}

	if (access (argv[1], F_OK) == 0)
	{
		fprintf (stdout, "%s exists\n", argv[1]);
	}

	if (access (argv[1], R_OK) == 0)
	{
		fprintf (stdout, "%s is readable\n", argv[1]);
	}

	if (access (argv[1], W_OK) == 0)
	{
		fprintf (stdout, "%s is writeable\n", argv[1]);
	}
	
	if (access (argv[1], X_OK) == 0)
	{
		fprintf (stdout, "%s is executable\n", argv[1]);
	}

	return 0;

}
