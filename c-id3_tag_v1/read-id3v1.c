#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
 * read-id3v1.c
 * Noprianto, December 2006
 * GPL
 */

void print_usage()
{
    fprintf (stdout, "read-id3v1 v0.0.2\n");
    fprintf (stdout, "Noprianto, 2006, http://www.noprianto.com/id3.php\n");
    fprintf (stdout, "usage: read-id3v1 <all|title|artist|album|year|comment|trackno|genre> <mp3_file>\n");
}

int main(int argc, char ** argv)
{
   char * tag = calloc (4, sizeof (char)); 
   char * title = calloc (31,  sizeof (char)); 
   char * artist = calloc (31, sizeof (char)); 
   char * album = calloc (31, sizeof (char)); 
   char * year = calloc (5, sizeof (char)); 
   char * comment = calloc (30, sizeof (char)); 
   char * trackno = calloc (3, sizeof (char)); 
   char * genre = calloc (2, sizeof (char)); 

   FILE * f;
   
   if (argc != 3)
   {
       print_usage();
       return 1;
   }
   else
   {

       f = fopen (argv[2], "r");
       if (f == NULL)
       {
           fprintf (stderr, "Cannot open file\n");
           return 2;
       }

       fseek (f, -128, SEEK_END);

       fread (tag, 1, 3, f);
       fread (title, 1, 30, f);
       fread (artist, 1, 30, f);
       fread (album, 1, 30, f);
       fread (year, 1, 4, f);
       fread (comment, 1, 29, f);
       fread (trackno, 1, 1, f);
       fread (genre, 1, 1, f);

       fclose (f);

       
       if ( strcmp(argv[1], "title") == 0 || strcmp (argv[1], "all") == 0)
       {
           fprintf (stdout, "%s\n", title);
       }
       
       if ( strcmp(argv[1], "artist") == 0 || strcmp (argv[1], "all") == 0)
       {
           fprintf (stdout, "%s\n", artist);
       }
       
       if ( strcmp(argv[1], "album") == 0 || strcmp (argv[1], "all") == 0)
       {
           fprintf (stdout, "%s\n", album);
       }
       
       if ( strcmp(argv[1], "year") == 0 || strcmp (argv[1], "all") == 0)
       {
           fprintf (stdout, "%s\n", year);
       }
       
       if ( strcmp(argv[1], "comment") == 0 || strcmp (argv[1], "all") == 0)
       {
           fprintf (stdout, "%s\n", comment);
       }
       
       if ( strcmp(argv[1], "trackno") == 0 || strcmp (argv[1], "all") == 0)
       {
           fprintf (stdout, "%d\n", trackno[0]);
       }
       
       if ( strcmp(argv[1], "genre") == 0 || strcmp (argv[1], "all") == 0)
       {
           fprintf (stdout, "%d\n", genre[0]);
       }
   }
   
   free (tag);
   free (title);
   free (artist);
   free (album);
   free (year);
   free (comment);
   free (trackno);
   free (genre);

   return 0;
}
