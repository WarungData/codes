/*
 * (c) Noprianto, 2007
 * GPL.
 */

#include <stdio.h>
#include <lua.h>
#include <lauxlib.h>
#include <string.h>


int main(int argc, char * argv[])
{

	char plugin_name[255];
	char field_name[255];
	char plugin_return[255];
	char temp[255];
	int plugin_argc;
	
	int i;

	char inputs[255];
	float inputf;
	char results[255];
	float resultf;

	/* -1=undefined, 0=number, 1=string*/
	int argv_type[255];

	lua_State *L;
	
	if (argc != 2)
	{
		fprintf (stderr, "usage: %s <plugin_file>\n", argv[0]);
		return 1;
	}


	L = lua_open();
	luaL_openlibs(L);

	fprintf (stdout, "[host] Selamat datang di C\n");
	fprintf (stdout, "[host] Bekerja dengan plugin: %s\n", argv[1]);

	luaL_loadfile(L,argv[1]);

	lua_call (L,0,0);

	lua_getfield (L,LUA_GLOBALSINDEX, "plugin_name");
	lua_getfield (L,LUA_GLOBALSINDEX, "plugin_return");
	lua_getfield (L,LUA_GLOBALSINDEX, "plugin_argc");
	
	strcpy (plugin_name, lua_tostring(L,-3));
	strcpy (plugin_return, lua_tostring(L,-2));
	plugin_argc = lua_tonumber(L,-1);

	fprintf (stdout, "[host] Nama plugin: %s\n", plugin_name); 
	fprintf (stdout, "[host] Jumlah argumen: %d\n", plugin_argc); 
	fprintf (stdout, "[host] Return type: %s\n", plugin_return); 

	argv_type[0] = -1;

	for (i=1; i<=plugin_argc; i++)
	{
		sprintf (field_name, "plugin_argv_%d", i);
		lua_getfield (L,LUA_GLOBALSINDEX, field_name);
		strcpy (temp, lua_tostring(L,-1));
		
		if (strcmp (temp, "number") == 0)
		{
			argv_type[i] = 0;
		}
		else if (strcmp (temp, "string") == 0)
		{
			argv_type[i] = 1;
		}


	}

	lua_getfield (L,LUA_GLOBALSINDEX, "plugin_main");

	for (i=1; i<=plugin_argc; i++)
	{
		if (argv_type[i] == 0)
		{
			strcpy(temp, "number");
		}
		else if (argv_type[i] == 1)
		{
			strcpy(temp, "string");
		};

		fprintf (stdout, "\t[host] Masukkan argumen ke %d [tipe: %s]: ", i,temp); 

		if (strcmp (temp, "number") == 0)
		{
			fscanf (stdin, "%f", &inputf);
			fprintf (stdout, "\t[host] Anda memasukkan: %f \n", inputf); 
			lua_pushnumber (L, inputf);
		}
		else if (strcmp (temp, "string") == 0)
		{
			fscanf (stdin, "%s", inputs);
			fprintf (stdout, "\t[host] Anda memasukkan: %s \n", inputs); 
			lua_pushstring (L, inputs);
		}


	}

	if (lua_pcall (L, plugin_argc, 1,0) != 0)
	{
		fprintf (stderr, "Kesalahan menjalankan plugin: %s\n", lua_tostring(L, -1));
	}

	if (strcmp (plugin_return,"number") == 0)
	{
		resultf = lua_tonumber (L, -1);
		fprintf (stdout, "[host] Return value: %f \n", resultf); 
	}
	else if (strcmp (plugin_return, "string") == 0)
	{
		strcpy(results, lua_tostring (L, -1));
		fprintf (stdout, "[host] Return value: %s \n", results); 
	}

	lua_close (L);;

	fprintf (stdout, "[host] Kembali ke C\n");

	return 0;
};
