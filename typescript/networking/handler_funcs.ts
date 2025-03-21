
export type handler_func = ( input: string ) => string | undefined

export function server_handler( message: string  ) : string{
    let value: number = +message.toString( )
    if( Number.isNaN( value ) )
        return "stop"
    //console.log( "Server handler" + " input is " + message + "  Value is " + value )
    return String( value * 2 )
        
}

export function middle_handler( input: string ): string{
    
    let value: number = +input.toString( )
    if( Number.isNaN( value ) )
        return "stop"
    //console.log( "middle handler Value is " + value )
    return String( value + 3 )
        
}

export function client_handler( input: string ): string{
    let value = +input.toString( )
    if( Number.isNaN( value ) )
        return "stop"
    //console.log( "Client handler" + " input is " + input + "  Value is " + value )
    return String( value + 1 )
    
    
}