#include <stdio.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>

int main (int argc, char * argv[])
{
	
	int res;

	if (argc != 2)
	{
		fprintf (stderr, "usage %s <dir>\n", argv[0]);
		exit (1);
	}

	res = mkdir (argv[1], S_IRWXU);

	if (res != 0)
	{
		fprintf (stderr, "%s\n", strerror (errno));
		exit (1);
	}

	return 0;

}
