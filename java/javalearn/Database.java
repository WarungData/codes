/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package javalearn;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

/**
 *
 * @author user
 */
class Database
{
    static void main()
    {
        //load driver
        try
        {
            Class.forName(JavaLearn.DBDRIVER);
        } catch (ClassNotFoundException ex)
        {
            ex.printStackTrace(System.err);
            return;
        }
        
        //connection
        Connection conn;
        try
        {
            conn = DriverManager.getConnection(JavaLearn.DBCONN);
            System.out.println(conn);
        } catch (SQLException ex)
        {
            ex.printStackTrace(System.err);
            return;
        }
        
        //create table
        Statement stmt1;
        try
        {
            stmt1 = conn.createStatement();
            stmt1.executeUpdate("create table a(a integer)");
        } catch (SQLException ex)
        {
            ex.printStackTrace(System.err);
            return;
        }
        
        //insert row, demo prepared statement
        PreparedStatement stmt2;
        try
        {
            stmt2 = conn.prepareStatement("insert into a(a) values(?)");
            stmt2.setInt(1, 12345);
            stmt2.executeUpdate();
        } catch (SQLException ex)
        {
            ex.printStackTrace(System.err);
            return;
        }        
        
        //select
        Statement stmt3;
        try
        {
            stmt3 = conn.createStatement();
            ResultSet rs = stmt3.executeQuery("select * from a");
            while (rs.next())
            {
                System.out.println(rs.getString(1));
            }
        } catch (SQLException ex)
        {
            ex.printStackTrace(System.err);
            return;
        }
    }
}
