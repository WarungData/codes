#include <gtk/gtk.h>

static void destroy (GtkWidget *window, gpointer data)
{
	gtk_main_quit ();
};

int main(int argc, char * argv[])
{
	GtkWidget *window;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_window_set_title (GTK_WINDOW(window), "Hello World");

	g_signal_connect (G_OBJECT (window), "destroy", G_CALLBACK (destroy), NULL);

	gtk_widget_show (window);

	gtk_main();

	return 0;

};

