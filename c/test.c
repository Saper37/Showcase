
#include <netinet/in.h> // server
#include <arpa/inet.h>  // client
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>
#define PORT 8080

// server 
int main( int argc, char const* argv[ ] ){
    /*
    */
    int server_fd, new_socket;
    sszie_t valread;
    struct sockadd_in address;
    int opt = 1;
    socklen_t adrlen = sizeof( address );
    char buffer[ 1024 ] = { 0 };
    char* hello = "hello"

    /*
    */
    if( (server_fd = socket( AF_INET, SOCK_STREAM, 0 ) ) < 0 )
        exit( EXIT_FAILURE );
    /*
    */
    if( setsockopt( server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, & opt, sizeof( opt ))){
        perror( "setsockopt");
        exit( EXIT_FAILURE);
    }

    /*
    */
    address.sin_family = AF_INET;
    adress.sin_add.s_addr = INADDR_ANY;
    address.sin_port = htons( PORT );

    if( bind( server_fd, ( struct sockaddr*)&address, sizeof( address ) ) < 0 ) {
        perror( "bind" );
        exit( EXIT_FAILURE );
    }
    if( listen( server_fd, 3 ) < 0 ){
        perror( "listen");
        exit( EXIT_FAILURE )
    }
    if( ( new_socket = accept( server_fd, (struct sockaddr*)& address, &addrlen ) ) < 0 ){
        perror( "accept" )
        exit( EXIT_FAILURE )
    }
    valread = read( new_socket, buffer, 1024 - 1 );
    printf( "%s\n", buffer);
    send( new_socket, hello, strlen( hello ), 0 );
    pritnf( "Hello message sent\n" );
    close( new_socket );
    close( server_fd );
    
    return 0;
}

int main( ){
     /*
    */
    int staus, valread, client_fd;
    struct sockadd_in address;
    char buffer[ 1024 ] = { 0 };
    char* hello = "hello"
    char* ip = {"127.0.0.1"}

    /*
    */
    if( (client_fd_fd = socket( AF_INET, SOCK_STREAM, 0 ) ) < 0 )
        return  -1;
    
    /*
    */
    address.sin_family = AF_INET;
    address.sin_port = htons( PORT );

    if( inet_pton( AF_INET, ip, &serv_add.sin_addr <= 0) ) {
        return -1;
    }
    if( ( status = connect( client_fd, ( struct sockaddr*)&serv_addr, sizeof( serv_addr )) ) < 0 )
        return -1;
    
    send( client_fd, hello, strlen( hello ), 0 );

    valread = read( client_fd, buffer, 1024 - 1 );
    pritnf( "%s\n", buffer );
    close( client_fd );
    
    return 0;
}