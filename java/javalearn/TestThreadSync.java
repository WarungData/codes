/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

/**
 *
 * @author user
 */
public class TestThreadSync 
{
    static class ThreadSync extends Thread
    {
        private int delay;
        private WorkerThread worker;
        
        ThreadSync(WorkerThread worker, int delay)
        {
            this.delay = delay;
            this.worker = worker;
        }
        
        public void run()
        {
            synchronized(worker)
            {
                worker.workSync(delay, Thread.currentThread().getName());
            }
        }
    }
    
    static void main() 
    {
        WorkerThread worker = new WorkerThread();

        //
        for (int i=0; i<3; i++)
        {
            ThreadSync t = new ThreadSync(worker, 1000);
            t.start();
        }
    }    
}
