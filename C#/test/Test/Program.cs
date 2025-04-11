// See https://aka.ms/new-console-template for more information

using System;
using System.ComponentModel;
using Microsoft.VisualBasic;
using System.Net.Sockets;

namespace myTest{
    public class Program{
        
        public void main( string[ ] args ){
            
            Console.WriteLine( "hello you from the program ");
        }
    }

    abstract class Handler{
        protected String type;
         public abstract void Init( );
         public abstract void Start( );
         public String getType( ){return this.type}
    }
    class ServerHandler : Handler{
        private String type = "server";
        public void Init( ){

        }
         public void Start( ){
            
   
    }
    class MiddleHandler : Handler{
        private String type = "middle";
        public override init( ){}
        public override start( ){}
    }
    class ClientHandler : Handler{
        private String type = "client";
        public override init( ){}
        public override start( ){}
    }

    abstract class Node{
        public virtual void init( ){}
        public virtual void start( ){}
    }

    class SocketNode : Node{
        private String[][] info;
        private Handler myhandler;
        SocketNode( String[][] info, Handler myhandler  ){
            this.info = info;
            this.myhandler = myhandler;
        }
        public override void init( ){
            if( String.Compare( this.info[ 0 ][0 ], "" ) != 1 && 
                String.Compare( this.info[ 1 ][ 0 ], "" ) != 1 ){

            }
        }

    }
}

