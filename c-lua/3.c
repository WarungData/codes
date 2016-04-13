/*
 * (c) Noprianto, 2007
 * GPL
 */

#include <stdio.h>
#include <lua.h>
#include <lauxlib.h>


int main(int argc, char * argv[])
{

	lua_State *L;

	L = lua_open();
	luaL_openlibs(L);

	fprintf (stdout, "[host] Selamat datang di C\n");
	fprintf (stdout, "[host] Tanggal dan jam akan didapatkan dari plugin\n");

	luaL_loadfile(L,"3.lua");

	lua_call (L, 0, 0);

	lua_close (L);;

	fprintf (stdout, "[host] Kembali ke C\n");

	return 0;
};
