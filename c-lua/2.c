/*
 * (c) Noprianto, 2007
 * GPL
 */

#include <stdio.h>
#include <string.h>
#include <lua.h>
#include <lauxlib.h>


int main(int argc, char * argv[])
{

	char  nama[255];
	
	lua_State *L;

	if (argc != 2)
	{
		fprintf (stderr, "usage: %s <name>\n", argv[0]);
		return 1;
	}

	L = lua_open();
	luaL_openlibs(L);

	fprintf (stdout, "[host] Selamat datang di C\n");

	luaL_loadfile(L,"2.lua");

	strcpy (nama, argv[1]);
	lua_pushstring (L, nama);
	lua_setfield (L, LUA_GLOBALSINDEX, "myname");
	lua_call (L, 0, 0);

	lua_close (L);;

	fprintf (stdout, "[host] Kembali ke C\n");

	return 0;
};
