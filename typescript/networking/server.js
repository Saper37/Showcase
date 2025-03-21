"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// Node.js networking functionality
var servernet = require("net");
var handler_funcs_1 = require("./handler_funcs");
var selip = process.env.TARGETIP;
var selport = Number(process.env.TARGETPORT);
var ownerip = process.env.OWNERIP;
var ownerport = process.env.OWNERPORT;
function serverfunc(message) {
    var message_temp = "";
    while (message != "stop") {
        message_temp = (0, handler_funcs_1.server_handler)(message);
        message = String(message_temp);
    }
}
var serverconnection = "";
var server = servernet.createServer(function (serverconnection) {
    serverconnection.on("end", function () {
        console.log("disconnected");
        server.close();
    });
    serverconnection.on("data", function (data) {
        console.log(" serverconnection data event. data is " + data + " is it NaN " + isNaN(data));
        if (!isNaN(data)) {
            var message = (0, handler_funcs_1.server_handler)(data);
            serverconnection.write(message);
        }
    });
    //serverconnection.write( "hello" )
    //var message = ""
    serverconnection.pipe(serverconnection);
});
selport = 8080;
selip = "localhost";
server.listen({ port: selport, host: selip }, function () {
    console.log("listening");
});
