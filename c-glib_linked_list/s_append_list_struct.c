#include <stdio.h>
#include <glib.h>

typedef struct
{
	char * username;
	char * shell;
} user;

int main(void)
{
	GSList * slist = NULL, *curr = NULL;

	g_fprintf (stdout, "Jumlah node: %d\n", g_slist_length (slist));

	g_fprintf (stdout, "\tmenambahkan node user1\n");
	user * user1 = g_new (user, 1);
	user1 -> username = "user1";
	user1 -> shell = "/bin/bash";
	slist = g_slist_append (slist, user1);
	
	g_fprintf (stdout, "\tmenambahkan node user2\n");
	user * user2 = g_new (user, 1);
	user2 -> username = "user2";
	user2 -> shell = "/bin/zsh";
	slist = g_slist_append (slist, user2);

	g_fprintf (stdout, "Jumlah node: %d\n", g_slist_length (slist));
	
	g_fprintf (stdout, "Iterasi: \n");

	for (curr = slist; curr; curr = curr -> next)
	{

		g_fprintf (stdout, "username: %s\n", ((user *) curr -> data) -> username );
		g_fprintf (stdout, "shell: %s\n", ((user *) curr -> data) -> shell );
		g_fprintf (stdout, "\n");
	}

	g_slist_free (slist);

	g_free (user1);
	g_free (user2);

	return 0;

};

