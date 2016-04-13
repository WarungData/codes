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

	char temp[255];
	char plugin_name_temp[255];

	int i;

	fprintf (stdout, "[host] Selamat datang di C\n");
	fprintf (stdout, "[host] Simulasi mendaftarkan menu dan menjalankan fungsi utama plugin\n");

	for (i=1; i<=3; i++)
	{
		sprintf (temp, "5-%d.lua", i);

		lua_State *L;

		L = lua_open();
		luaL_openlibs(L);

		luaL_loadfile(L,temp);

		lua_call (L,0,0);

		lua_getfield (L,LUA_GLOBALSINDEX, "plugin_name");
		
		strcpy (plugin_name_temp, lua_tostring(L,-1));
		
		fprintf (stdout, "\n\n[host] Mendaftarkan menu plugin baru: %s\n", plugin_name_temp); 
		fprintf (stdout, "Menjalankan plugin %s\n", plugin_name_temp); 

		lua_getfield (L, LUA_GLOBALSINDEX, "plugin_main");
		
		lua_call (L,0,0);

		fprintf (stdout, "Selesai Menjalankan plugin %s\n", plugin_name_temp); 

		lua_close (L);;


	}


	fprintf (stdout, "[host] Kembali ke C\n");

	return 0;
};
