"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Node = void 0;
var Node = /** @class */ (function () {
    function Node(infos, handler, interpreter) {
        this.infos = [];
        this.myhandler = handler;
        this.interpreter = interpreter;
        this.infos = infos;
    }
    Node.prototype.start = function () {
        if (this.infos[0][0] != "" && this.infos[1][0] != "")
            this.myhandler.middle_func();
        else if (this.infos[0][0] == "" && this.infos[1][0] != "")
            this.myhandler.client_func();
        else if (this.infos[0][0] != "" && this.infos[1][0] == "")
            this.myhandler.server_func();
    };
    Node.prototype.stop = function () {
        this.myhandler.stop();
    };
    return Node;
}());
exports.Node = Node;
