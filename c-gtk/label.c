#include <gtk/gtk.h>

int main(int argc, char * argv[])
{
	GtkWidget *window, *label;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_widget_set_size_request (window, 400, 100);

	label = gtk_label_new ("Hello World :)");

	gtk_container_add (GTK_CONTAINER (window), label);

	gtk_widget_show_all (window);

	gtk_main();

	return 0;

};

