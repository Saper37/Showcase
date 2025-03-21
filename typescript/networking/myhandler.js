"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.MyHandler = void 0;
var handler_funcs_1 = require("./handler_funcs");
var network = require("net");
var MyHandler = /** @class */ (function () {
    function MyHandler(type, handler) {
        this.serverconnection = "";
        switch (type) {
            case "client":
                this.handler = handler_funcs_1.client_handler;
                break;
            case "server":
                this.handler = handler_funcs_1.server_handler;
                break;
            case "middle":
                this.handler = handler_funcs_1.middle_handler;
                break;
            default:
                break;
        }
    }
    MyHandler.prototype.server_func = function (server, info, interpreter) {
        var selport = info[0];
        var selip = info[1];
        var node_server = network.createServer(function (serverconnection) {
            serverconnection.on("end", function () {
                server.close();
            });
            serverconnection.on("data", function (data) {
                var message = "stop";
                if (!isNaN(data)) {
                    data = interpreter.encode(data);
                    message = this.handler(data);
                    serverconnection.write(message);
                }
                else if (data == "stop") {
                    serverconnection.write(message);
                    serverconnection.close();
                }
            });
            serverconnection.pipe(serverconnection);
            server.listen({ port: selport, host: selip });
        });
    };
    MyHandler.prototype.middle_func = function (server, info, interpreter) {
        // server definition
        var selport = info[0];
        var selip = info[1];
        var node_server = network.createServer(function (serverconnection) {
            serverconnection.on("end", function () {
                server.close();
            });
            serverconnection.on("data", function (data) {
                var message = "stop";
                if (!isNaN(data)) {
                    data = interpreter.decode(data);
                    message = this.handler(data);
                    message = interpreter.encode(message);
                    serverconnection.write(message);
                }
                else if (data == "stop")
                    serverconnection.write(message);
            });
            serverconnection.pipe(serverconnection);
            server.listen({ port: selport, host: selip });
        });
        // Client definition
        var client = network.connect({ port: selport }, { host: selip }, function () {
            client.on("data", function (response) {
                var message = response;
                message = interpreter.encode(message);
                message = this.handler(message);
                message = interpreter.decode(message);
                if (message == "stop")
                    client.end();
                else {
                    client.write(message);
                }
            });
            client.on("end", function () {
                console.log("disconnected");
            });
        });
    };
    MyHandler.prototype.client_func = function (info, interpreter) {
        var selport = info[0];
        var selip = info[1];
        var client = network.connect({ port: selport }, { host: selip }, function () {
            client.on("data", function (response) {
                var message = response;
                message = interpreter.encode(message);
                message = this.handler(message);
                message = interpreter.decode(message);
                if (message == "stop")
                    client.end();
                else {
                    client.write(message);
                }
            });
            client.on("end", function () {
                console.log("disconnected");
            });
        });
    };
    return MyHandler;
}());
exports.MyHandler = MyHandler;
