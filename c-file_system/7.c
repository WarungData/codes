#include <stdio.h>
#include <string.h>
#include <errno.h>

int main (int argc, char * argv[])
{
	
	int res;

	if (argc != 3)
	{
		fprintf (stderr, "usage %s <old_path> <new_path>\n", argv[0]);
		exit (1);
	}

	res = rename (argv[1], argv[2]);

	if (res != 0)
	{
		fprintf (stderr, "%s\n", strerror (errno));
		exit (1);
	}

	return 0;

}
