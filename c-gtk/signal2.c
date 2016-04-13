#include <gtk/gtk.h>

static void destroy (GtkWidget *window, gpointer data)
{
	gtk_main_quit ();
};

static void button_clicked (GtkButton *button, GtkWidget *entry)
{
	g_print ("%s\n", gtk_entry_get_text (GTK_ENTRY (entry)) );
};

int main(int argc, char * argv[])
{
	GtkWidget *window, *entry, *button, *vbox;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_window_set_title (GTK_WINDOW(window), "Hello World");

	g_signal_connect (G_OBJECT (window), "destroy", G_CALLBACK (destroy), NULL);

	entry = gtk_entry_new ();

	button = gtk_button_new_with_mnemonic ("_Get Data");
	g_signal_connect (G_OBJECT (button), "clicked", G_CALLBACK (button_clicked), (gpointer) entry);

	vbox = gtk_vbox_new (TRUE, 5);

	gtk_box_pack_start_defaults (GTK_BOX (vbox), entry);
	gtk_box_pack_start_defaults (GTK_BOX (vbox), button);

	gtk_container_add (GTK_CONTAINER (window), vbox);

	gtk_widget_show_all (window);

	gtk_main();

	return 0;

};

