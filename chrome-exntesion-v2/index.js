// chrome.runtime.onInstalled.addListener(
//     function(){
//         console.log("Hey from index");
//     }
// )

// In popup.js
console.log("Hey from index")
chrome.storage.local.get("data",function(res) {
    console.log("res",res["data"])
});
// chrome.storage.local.get("time",function(res) {
//     console.log(res["time"])
// });

document.getElementById("container").appendChild("<h1>Hey</h1>")

// console.log(chrome.histroy)
// chrome.runtime.sendMessage({ message: "Hello from the index!" });


//https://short-funny.com/