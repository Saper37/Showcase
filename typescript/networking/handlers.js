"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.server_handler = server_handler;
exports.middle_handler = middle_handler;
exports.client_handler = client_handler;
function server_handler(message) {
    var value = +message.toString();
    if (Number.isNaN(value))
        return "stop";
    //console.log( "Server handler" + " input is " + message + "  Value is " + value )
    return String(value * 2);
}
function middle_handler(input) {
    var value = +input.toString();
    if (Number.isNaN(value))
        return "stop";
    //console.log( "middle handler Value is " + value )
    return String(value + 3);
}
function client_handler(input) {
    var value = +input.toString();
    if (Number.isNaN(value))
        return "stop";
    //console.log( "Client handler" + " input is " + input + "  Value is " + value )
    return String(value + 1);
}
