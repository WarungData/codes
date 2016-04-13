/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

/**
 *
 * @author user
 */
public class TestThreadJoin 
{
    private static final int MAX = 3;
    
    static class ThreadJoin extends Thread
    {
        private int n;
        private int delay;
        
        ThreadJoin(int n, int delay)
        {
            this.n = n;
            this.delay = delay;
        }
        
        public void run()
        {
            WorkerThread w = new WorkerThread();
            w.work(n, delay, Thread.currentThread().getName());
        }
    }
    
    static void main() 
    {
        ThreadJoin[] t = new ThreadJoin[MAX];
        for (int i=0; i<MAX; i++)
        {
            t[i] = new ThreadJoin(i+1, i*1000);
            t[i].setName("MyThread-" + i);
            t[i].start();
        }
        
        //
        for (int i=0; i<5; i++)
        {
            System.out.println(Thread.currentThread().getName() + ":" + i);
            try 
            {
                Thread.sleep(200);
            } 
            catch (InterruptedException ex) 
            {
                break;
            }
        }
        
        //
        for (int i=0; i<MAX; i++)
        {
            try 
            {
                t[i].join();
            } 
            catch (InterruptedException ex) 
            {
            }
        }
        System.out.println(Thread.currentThread().getName() + " selesai terakhir");
    }    
}