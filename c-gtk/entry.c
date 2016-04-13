#include <gtk/gtk.h>

int main(int argc, char * argv[])
{
	GtkWidget *window, *entry;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_widget_set_size_request (window, 400, 100);

	entry = gtk_entry_new ();
	gtk_entry_set_visibility (GTK_ENTRY (entry), FALSE);
	gtk_entry_set_invisible_char (GTK_ENTRY (entry), '*');

	gtk_container_add (GTK_CONTAINER (window), entry);

	gtk_widget_show_all (window);

	gtk_main();

	return 0;

};

