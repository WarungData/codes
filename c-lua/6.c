/*
 * (c) Noprianto, 2007
 * GPL
 */

#include <stdio.h>
#include <lua.h>
#include <lauxlib.h>


int main(void)
{

	lua_State *L;
	L = lua_open();
	luaL_openlibs(L);

	fprintf (stdout, "[host] Selamat datang di C\n");
	fprintf (stdout, "[host] I/O dilakukan oleh plugin\n");

	luaL_loadfile(L,"6.lua");
	lua_call (L, 0, 0);

	lua_close (L);;

	fprintf (stdout, "[host] Kembali ke C\n");

	return 0;
};
