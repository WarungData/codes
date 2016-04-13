/*
 * (c) Noprianto, 2007
 * GPL
 */

#include <stdio.h>
#include <lua.h>
#include <lauxlib.h>
#include <string.h>


int main(int argc, char * argv[])
{

	char plugin_name[255];
	char plugin_author[255];
	char plugin_copyright_string[255];
	char plugin_license[16];

	lua_State *L;

	L = lua_open();
	luaL_openlibs(L);

	fprintf (stdout, "[host] Selamat datang di C\n");
	fprintf (stdout, "[host] Mendapatkan properti plugin\n");

	luaL_loadfile(L,"4.lua");

	lua_call (L,0,0);

	lua_getfield (L,LUA_GLOBALSINDEX, "plugin_name");
	lua_getfield (L,LUA_GLOBALSINDEX, "plugin_author");
	lua_getfield (L,LUA_GLOBALSINDEX, "plugin_copyright_string");
	lua_getfield (L,LUA_GLOBALSINDEX, "plugin_license");
	
	strcpy (plugin_name, lua_tostring(L,-4));
	strcpy (plugin_author, lua_tostring(L,-3));
	strcpy (plugin_copyright_string, lua_tostring(L,-2));
	strcpy (plugin_license, lua_tostring(L,-1));

	fprintf (stdout, "\t[host] Nama plugin: %s\n", plugin_name); 
	fprintf (stdout, "\t[host] Pembuat plugin: %s\n", plugin_author); 
	fprintf (stdout, "\t[host] Copyright plugin: %s\n", plugin_copyright_string); 
	fprintf (stdout, "\t[host] Lisensi plugin: %s\n", plugin_license); 


	lua_close (L);;

	fprintf (stdout, "[host] Kembali ke C\n");

	return 0;
};
