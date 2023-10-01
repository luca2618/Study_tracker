 console.log("hello")
// chrome.tabs.onUpdated.addListener(function() {
//     onWindowLoad();
// });
    
// function onWindowLoad() {
//     chrome.tabs.executeScript(null, {
//         file: "contentscript.js"
//     }, function() {
//         if (chrome.extension.lastError) {
//             htmlcontent = 'There was an error injecting script : \n' + chrome.extension.lastError.message;
//         }
//     });
// }
    
// chrome.runtime.onMessage.addListener( function(request, sender) {
//     if (request.action == "getSource") {
//         htmlcontent = request.source;
//         //call whatever function from here on so that htmlcontent will have the selected tab's content.
//     }
// });

// chrome.tabs.onActivated.addListener(function(activeInfo) {
//     console.log(activeInfo.tabId);
//     console.log('tab changed');
// });

// chrome.experimental.webNavigation.onCommitted(function(details){
//     console.log(details);
// });

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    switch (request.contentScriptQuery) {
        case "userLogin":
            fetch("https://localhost:8000/classify")
                .then((response) => response.json())
                .then((json) => sendResponse("kerk"));
            break;
    }
    return true;
});