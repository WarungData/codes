/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

/**
 *
 * @author user
 */
public class TestThreadStop 
{
    static class ThreadStop extends Thread
    {
        private boolean finish = false;
        private int counter = 0;
        
        public void run()
        {
            while (! finish)
            {
                WorkerThread w = new WorkerThread();            
                w.work(1, 10, Thread.currentThread().getName()+counter);
                counter++;
            }
        }
        
        public void setStop()
        {
            finish = true;
        }
    }
    
    static void main() 
    {
        ThreadStop t = new ThreadStop();
        t.setName("MyThread");
        t.start();
        
        //
        for (int i=0; i<4; i++)
        {
            System.out.println(Thread.currentThread().getName() + ":" + i);
            try 
            {
                Thread.sleep(400);
            } 
            catch (InterruptedException ex) 
            {
                break;
            }
        }
        
        //
        System.out.println("Hentikan thread!");
        t.setStop();
        try 
        {
            Thread.sleep(1000);
        } 
        catch (InterruptedException ex) 
        {
        }
        System.out.println("Masih hidup? " +  t.isAlive());
    }    
}
