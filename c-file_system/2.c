#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

int main (int argc, char * argv[])
{
	int res;

	if (argc != 2)
	{
		fprintf (stderr, "usage %s <file>\n", argv[0]);
		exit (1);
	}

	res = unlink (argv[1]);
	
	if (res == 0)
	{
		fprintf (stdout, "File %s deleted successfully\n", argv[1]);
	}
	else
	{
		fprintf (stderr, "%s\n", strerror(errno));
		exit (-1);
	}

	return 0;

}
