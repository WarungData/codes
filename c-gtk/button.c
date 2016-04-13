#include <gtk/gtk.h>

int main(int argc, char * argv[])
{
	GtkWidget *window, *button;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_widget_set_size_request (window, 400, 100);

	button = gtk_button_new_with_label ("Klik saya");

	gtk_container_add (GTK_CONTAINER (window), button);

	gtk_widget_show_all (window);

	gtk_main();

	return 0;

};

