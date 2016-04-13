/*
 * (c) Noprianto, 2007
 * GPL
 */

#include <stdio.h>
#include <lua.h>
#include <lauxlib.h>


int main(int argc, char * argv[])
{

	float bil;
	float result;
	
	lua_State *L;

	L = lua_open();
	luaL_openlibs(L);

	fprintf (stdout, "[host] Selamat datang di C\n");
	fprintf (stdout, "[host] I/O dengan C, proses oleh plugin\n");
	fprintf (stdout, "[host] Menghitung akar kuadrat\n");

	luaL_loadfile(L,"7.lua");
	lua_call (L,0,0);

	fprintf (stdout, "[host] Masukkan bilangan: ");
	fscanf (stdin, "%f", &bil);
	fprintf (stdout, "[host] Anda memasukkan: %f\n", bil);

	lua_getfield (L, LUA_GLOBALSINDEX, "akarkuadrat");
	lua_pushnumber (L, bil);
	lua_call (L, 1, 1);

	result = (float) lua_tonumber (L, -1);

	lua_close (L);;
	
	fprintf (stdout, "[host] Akar kuadrat dari %f adalah %f\n", bil,result);

	fprintf (stdout, "[host] Kembali ke C\n");

	return 0;
};
