
import { client_handler, middle_handler, server_handler } from "../handlers"

describe( "handler test", ( ) => {
    test( "client handler returns stop", ( ) => { expect( client_handler( "stop" ) ).toBe( "stop" ) })
    test( "server handler returns stop", ( ) => { expect( server_handler( "stop" ) ).toBe( "stop" ) })

    test( "client handler number input", ( ) => { expect( client_handler( 1 ) ).toBe( "2" ) })
    test( "server handler number input", ( ) => { expect( server_handler( 2 ) ).toBe( "4" ) })

    test( "client handler non-sense input", ( ) => { expect( client_handler( "hdfsdjk" ) ).toBe( "stop" ) })
    test( "server handler non-sense input", ( ) => { expect( server_handler( "hsdflskl" ) ).toBe( "stop" ) })
    
    test( "middle handler returns stop", ( ) => { expect( middle_handler( "stop" ) ).toBe( "stop" ) })
    test( "middle handler number input", ( ) => { expect( middle_handler( 1 ) ).toBe( "4" ) })
    test( "middle handler non-sense input", ( ) => { expect( middle_handler( "hdfsdjk" ) ).toBe( "stop" ) })
}
)