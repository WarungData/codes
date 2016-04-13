
plugin_name = "where do you want to go today? :p"
plugin_author = "Noprianto"
plugin_copyright_string = "(c) Noprianto, 2007"
plugin_license = "GPL"


plugin_return = "number"
plugin_argc = 3
plugin_argv_1 = "string"
plugin_argv_2 = "string"
plugin_argv_3 = "string"


function plugin_main(s1,s2,s3)
	print (os.date()  .. " " .. s1)
	print (os.date()  .. " " .. s2)
	print (os.date()  .. " " .. s3)
	return 0
end
