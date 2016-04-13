#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <sys/sendfile.h>

int main (int argc, char * argv[])
{

	int len;

	int f1;
	int f2;

	struct stat stat_buf;
	off_t offset = 0;

	if (argc != 3)
	{
		fprintf (stderr, "usage %s <src_file> <dst_file>\n", argv[0]);
		exit (1);
	}

	f1 = open (argv[1], O_RDONLY);
	if (f1 == -1)
	{
		fprintf (stderr, "%s\n", strerror(errno));
		exit (2);
	}
	fstat (f1, &stat_buf);

	f2 = open (argv[2], O_WRONLY | O_CREAT, stat_buf.st_mode);
	if (f2 == -1)
	{
		fprintf (stderr, "%s\n", strerror(errno));
		exit (3);
	}

	len = sendfile (f2, f1, &offset, stat_buf.st_size);
	if (len == -1)
	{
		fprintf (stderr, "%s\n", strerror (errno));
		exit (4);
	}

	close (f1);
	close (f2);

	return 0;

}
