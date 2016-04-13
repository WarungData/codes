#include <gtk/gtk.h>

int main (int argc, char *argv[])
{
	GtkWidget *window, *toggle_button;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_widget_set_size_request (window, 400, 100);

	toggle_button = gtk_toggle_button_new_with_mnemonic ("_Toggle :)");

	gtk_container_add (GTK_CONTAINER (window), toggle_button);

	gtk_widget_show_all (window);

	gtk_main ();

	return 0;
};
