"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var node_1 = require("./node");
var myhandler_1 = require("./myhandler");
var myinterpreter_1 = require("./myinterpreter");
var handler_funcs_1 = require("./handler_funcs");
var process = require("process");
main: (function () {
    var serverinfo = [process.env.serverip, process.env.serverport];
    var clientinfo = [process.env.clientip, process.env.clientport];
    var targetinfo = [process.env.targetip, process.env.targetport];
    var ishttp = process.env.ishttp;
    var addressfamily = process.env.addressfamily;
    var connectiontype = process.env.connectiontype;
    var encode = process.env.encode;
    var handler;
    var type = "";
    if (serverinfo[0] != "" && clientinfo[0] != "") {
        handler = handler_funcs_1.middle_handler;
        type = "middle";
    }
    else if (serverinfo[0] != "" && clientinfo[0] == "") {
        handler = handler_funcs_1.server_handler;
        type = "server";
    }
    else if (serverinfo[0] == "" && clientinfo[0] != "") {
        handler = handler_funcs_1.client_handler;
        type = "client";
    }
    else {
        handler = undefined;
    }
    var infos = [serverinfo, clientinfo, targetinfo, ishttp, addressfamily, connectiontype, encode];
    var myHandler = new myhandler_1.MyHandler(type, handler);
    var interpreter = new myinterpreter_1.MyInterpreter();
    var mynode = new node_1.Node(infos, myHandler, interpreter);
    mynode.start();
});
