#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <unistd.h>

int main (int argc, char * argv[])
{
	
	int res;
	char buf[256];

	if (argc != 2)
	{
		fprintf (stderr, "usage %s <dir>\n", argv[0]);
		exit (1);
	}

	res = chdir (argv[1]);

	if (res != 0)
	{
		fprintf (stderr, "%s\n", strerror (errno));
		exit (1);
	}
	else
	{
		getcwd (buf, sizeof (buf));
		fprintf (stdout, "CWD: %s\n", buf);
	}

	return 0;

}
