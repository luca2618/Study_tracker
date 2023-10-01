// chrome.runtime.onInstalled.addListener(
//     function(){
//         console.log("Hey from index");
//     }
// )

// In popup.js
console.log("Hey from index")
chrome.storage.local.get("data",function(res) {
    console.log(res["data"])
});
chrome.storage.local.get("time",function(res) {
    console.log(res["time"])
});
// console.log(chrome.histroy)
// chrome.runtime.sendMessage({ message: "Hello from the index!" });
