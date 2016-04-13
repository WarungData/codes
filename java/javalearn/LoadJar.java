/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.io.File;
import java.lang.reflect.Method;
import java.net.URL;
import java.net.URLClassLoader;

/**
 *
 * @author user
 */
class LoadJar
{
    static void main()
    {
        try
        {
            //module1.jar dalam direktori aktif
            URL mod = new File("module1.jar").toURI().toURL();
            URL[] mods = {mod};

            //gunakan class loader dengan parent default
            //untuk method non static, bisa gunakan parent this.getClass().getClassLoader()
            URLClassLoader child = new URLClassLoader(mods);
            
            //dapatkan class module1.Main
            Class cls = Class.forName("module1.Main", true, child);
            
            //dapatkan method init dalam class tersebut (non static)
            Method method = cls.getDeclaredMethod("init");
            
            //buat instance baru
            Object obj = cls.newInstance();
            
            //panggil method
            Object res = method.invoke(obj);
        }
        catch (Exception ex)
        {
            ex.printStackTrace(System.err);
            return;
        }
    }
}
