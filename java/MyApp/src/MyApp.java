import com.sun.source.tree.Scope;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.List;
import java.util.concurrent.atomic.AtomicBoolean;

import static java.lang.System.getenv;

/*
  The main function
 */
public class MyApp {
    public static void main( String[ ] args ) throws Exception{

        String[] serverinfo =  { getenv("serverip"), getenv("serverport") };
        String[] clientinfo = {getenv("clientip"), getenv("clientport")};
        String[] targetport = {getenv("targetip"), getenv("targetport")};
        String[] ishttp = { getenv("ishttp")};
        String[] socketinfo = {getenv("addressfamily"), getenv("connectiontype")};
        String[][] info = { serverinfo, clientinfo, targetport, ishttp, socketinfo };

        Handler myHandler;

        if( !serverinfo[ 0 ].equalsIgnoreCase("") && !clientinfo[ 0 ].equalsIgnoreCase( "" ) ) {
            myHandler = new MiddleHandler();
        }
        else if( !serverinfo[ 0 ].equalsIgnoreCase("") && clientinfo[ 0 ].equalsIgnoreCase( "" ) ) {
            myHandler = new ServerHandler();
        }
        else if( serverinfo[ 0 ].equalsIgnoreCase("") && !clientinfo[ 0 ].equalsIgnoreCase( "" ) ){
            myHandler = new ClientHandler();
        }
        else{
            throw new Exception( "Error with handler");
        }

        SocketNode node = new SocketNode( info, myHandler );
        node.init( );
        node.start( );
    }
}

/*
   Responsible for threads that run servers and clients
 */
class NodeThread extends Thread{
    protected Handler myhandler;
    NodeThread( Handler myhandler ) {
        this.myhandler = myhandler;
    }
    public Handler getMyhandler(){return this.myhandler;}
}
/*
   Specialized for server threads
 */
class ServerThread extends NodeThread{

    private Socket clientSocket;
    private PrintWriter output;
    private BufferedReader input;

    ServerThread( ServerHandler myhandler, ServerSocket server ){
        super( myhandler );
        try{
            this.clientSocket = server.accept( );
        }
        catch( Exception e ){
            System.out.println( e.getStackTrace() );
        }
    }
    public void run( ){
        String message = "", endvalue = "stop";
        int counter = 0;
        try {

            this.output = new PrintWriter(this.clientSocket.getOutputStream(), true);
            this.input = new BufferedReader(new InputStreamReader(this.clientSocket.getInputStream()));
        }
        catch( Exception e ){
            message = "";
            endvalue = "";
            System.out.println( e.getStackTrace() );
        }
        while( message != endvalue ){
            try{
                message = this.input.readLine( );
            }
            catch( Exception e ){
                String errorMessage = "";
                message = endvalue;
                System.out.println( "Error in run " + errorMessage );
            }

        }
    }
}
class ClientThread extends NodeThread{
    private DataInputStream input;
    private DataOutputStream output;

    ClientThread( ClientHandler myhandler, Socket client ){
        super( myhandler );
        try {
            output = new DataOutputStream( client.getOutputStream() );
        }
        catch( Exception e ){
            System.out.println( e.getStackTrace() );
        }
    }
    public void run( ){

    }
}

abstract class Node{
    public abstract void start();
    public abstract void init( );
}

class SocketNode extends Node{
    private String[ ][ ] info = {};
    private Socket clientSocket = null, serverSocket = null;
    private Handler myhandler = null;
    private List<Thread> servers = null;
    private List<Thread> clients = null;

    SocketNode( String[][] info, Handler myhandler ){
        this.info = info;
        this.myhandler = myhandler;
    }

    @Override
    public void init( ){

        String[ ] serverinfo = this.info[ 0 ];
        String[ ] clientinfo = this.info[ 1 ];
        String[ ] targetinfo = this.info[ 2 ];

        try{
            if( !serverinfo[ 0 ].equalsIgnoreCase("") &&
                !clientinfo[ 0 ].equalsIgnoreCase( "") ){
                ServerSocket server = new ServerSocket( Integer.valueOf( serverinfo[ 1 ] ) );
                ServerThread thread = new ServerThread( (ServerHandler) this.myhandler, server);
                this.servers.add( thread );

            }
            else if ( !serverinfo[ 0 ].equalsIgnoreCase("") &&
                    clientinfo[ 0 ].equalsIgnoreCase( "") ){
                Socket client = new Socket( clientinfo[ 0 ], Integer.valueOf( clientinfo[ 1 ] ) );
                ClientThread thread = new ClientThread( (ClientHandler) this.myhandler, client  );
                this.clients.add( thread );

            }
            else if ( serverinfo[ 0 ].equalsIgnoreCase("") &&
                    !clientinfo[ 0 ].equalsIgnoreCase( "") ){
                ServerSocket server = new ServerSocket( Integer.valueOf( serverinfo[ 1 ] ) );
                Socket client = new Socket( clientinfo[ 0 ], Integer.valueOf( clientinfo[ 1 ] ) );
                ServerThread serverThread = new ServerThread( ( ServerHandler ) this.myhandler, server );
                ClientThread clientThread = new ClientThread( ( ClientHandler ) this.myhandler, client );
                this.servers.add( serverThread );
                this.clients.add( clientThread );
            }
            else{
                throw new Exception("Error in init" );
            }
        }
        catch( Exception e ){
            System.out.println( e.getStackTrace() );
        }
        finally{

        }
    }
    @Override
    public void start( ){
        try{
            if( servers.size( ) > 0 ){
                for( Thread thread : this.servers )
                    thread.start( );
            }
            if( clients.size( ) > 0 ){
                for( Thread thread : this.clients ){
                    thread.start( );
                }
            }
        }
        catch( Exception e ){
            System.out.println( e.getStackTrace() );
        }
        finally{

        }
    }
}


abstract class Handler{
    protected String handlertype;
    public abstract String getType( );
}

class ServerHandler extends Handler{

    ServerHandler( ){
        this.handlertype = "server";
    }
    public String getType( ){ return this.handlertype; }

}

class MiddleHandler extends Handler{

    MiddleHandler( ){
        this.handlertype = "middle";
    }
    public String getType( ){ return this.handlertype; }
}

class ClientHandler extends Handler{
    ClientHandler( ){
        this.handlertype = "client";
    }
    public String getType( ){ return this.handlertype; }
}

