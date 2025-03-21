"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var net = require("net");
var handler_funcs_1 = require("./handler_funcs");
var selip = process.env.TARGETIP;
var selport = Number(process.env.TARGETPORT);
selip = "localhost";
selport = 8080;
//var selport = 100
var client = net.connect({ port: selport }, { host: selip }, function () {
    console.log("connected to the server, on port " + selport);
    var message = (0, handler_funcs_1.client_handler)("");
    client.write(message);
    console.log("client send message ");
});
client.on('data', function (response) {
    var data = response;
    data = data.toString();
    console.log("client on data. data is " + data + " is it NaN " + isNaN(data));
    if (!isNaN(data)) {
        data = (0, handler_funcs_1.client_handler)(data);
        console.log("client handler on data. data is " + data);
        if (data == "stop") {
            client.end();
        }
        else {
            client.write(data);
        }
    }
});
client.on("end", function () {
    console.log("disconneect from server");
});
