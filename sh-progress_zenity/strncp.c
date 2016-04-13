#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*
 * strncp, (c) Noprianto, 2006
 * BSD
 */

/*
 * return 0: success
 * return 1: length of source string (argv[1]) is less or equal then given length (argv[2])
 * return 2: general error
 */

int main(int argc, char ** argv)
{
	
	int len;
	
	if (argc != 3)
	{
		return 2;
	};
	
	len = atoi (argv[2]);
	char * out = (char * ) malloc (len * sizeof (char *) + 1); 

	if ( strlen ( argv[1] ) <= len)
	{
		return 1;
	}

	out = strncpy (	out, argv [1], len);

	fprintf(stdout, out);

	free (out);

	return 0;
}
