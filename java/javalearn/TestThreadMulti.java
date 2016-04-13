/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

/**
 *
 * @author user
 */
public class TestThreadMulti 
{
    static class ThreadMulti extends Thread
    {
        private int n;
        private int delay;
        private WorkerThread worker;
        
        ThreadMulti(WorkerThread worker, int n, int delay)
        {
            this.n = n;
            this.delay = delay;
            this.worker = worker;
        }
        
        public void run()
        {
            worker.work(n, delay, Thread.currentThread().getName());
        }
    }
    
    static class ThreadMulti2 extends Thread
    {
        private int n;
        private int delay;
        
        ThreadMulti2(int n, int delay)
        {
            this.n = n;
            this.delay = delay;
        }
        
        public void run()
        {
            WorkerThread.workStatic(n, delay, Thread.currentThread().getName());
        }
    }
    
    static void main() 
    {
        /*
        //cara biasa, pakai instance kelas WorkerThread
        WorkerThread worker = new WorkerThread();
        for (int i=0; i<3; i++)
        {
            ThreadMulti t = new ThreadMulti(worker, i+1, (i+1)*1000);
            t.setName("MyThread-" + i);
            t.start();
        }*/
        
        //cara pakai method static dari WorkerThread
        for (int i=0; i<3; i++)
        {
            ThreadMulti2 t = new ThreadMulti2(i+1, (i+1)*1000);
            t.setName("MyThread-" + i);
            t.start();
        }        
        
        //
        for (int i=0; i<8; i++)
        {
            System.out.println(Thread.currentThread().getName() + ":" + i);
            try 
            {
                Thread.sleep(700);
            } 
            catch (InterruptedException ex) 
            {
                break;
            }
        }
    }    
}
