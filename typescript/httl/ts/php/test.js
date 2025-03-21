function hello(s) {
    console.log(s);
}
var message = "So this does something";
function greeting(fn) {
    fn(message);
}
var examplefunc = function (par1, par2, par3) {
    return "Example's id is  " + par1 + " Example's name is " + par2 + " Example's type is " + par3;
};
function getExample(id, name) {
    return {
        id: id,
        name: name
    };
}
greeting(hello);
var app = document.getElementById("app");
var app1 = document.getElementById("app1");
var p = document.getElementById("p");
var heading = document.createElement("h1");
heading.textContent = message;
var heading2 = document.createElement("h2");
heading2.textContent = message;
var heading3 = document.createElement("h3");
var nameinput = document.createElement("input");
nameinput.addEventListener("change", function () {
    var text = nameinput.value;
    if (text === "heheh" && heading3 !== null) {
        heading3.textContent = "mikä on niin hauskaa?";
    }
});
var example = getExample(3, "example");
heading3.textContent = examplefunc(example.id, example.name, typeof (example));
app === null || app === void 0 ? void 0 : app.appendChild(heading2);
app1 === null || app1 === void 0 ? void 0 : app1.appendChild(heading);
app === null || app === void 0 ? void 0 : app.appendChild(heading3);
app1 === null || app1 === void 0 ? void 0 : app1.appendChild(nameinput);
