#include <gtk/gtk.h>

int main(int argc, char * argv[])
{
	GtkWidget *window, *label1, *label2, *label3, *hbox, *vbox;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_widget_set_size_request (window, 400, 100);

	label1 = gtk_label_new ("Hello World :)");
	label2 = gtk_label_new ("): dlroW olleH");
	label3 = gtk_label_new ("World Hello :)");

	hbox = gtk_hbox_new(TRUE, 5);
	gtk_box_pack_start_defaults (GTK_BOX (hbox), label1);
	gtk_box_pack_start_defaults (GTK_BOX (hbox), label2);

	vbox = gtk_vbox_new (TRUE, 5);
	gtk_box_pack_start_defaults (GTK_BOX (vbox), hbox);
	gtk_box_pack_start_defaults (GTK_BOX (vbox), label3);

	gtk_container_add (GTK_CONTAINER (window), vbox);

	gtk_widget_show_all (window);

	gtk_main();

	return 0;

};

