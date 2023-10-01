chrome.tabs.onActivated.addListener(function (activeInfo) {
  console.log("Hey from Service Worker")
  
chrome.tabs.onUpdated.addListener(async function (tabId, changeInfo, tab) {
  if (activeInfo.tabId === tabId && changeInfo.url) {
     console.log(`URL has changed to ${changeInfo.url}`)
     console.log("tab is ",tab);
     //if url changes then send the request to the api from content
     const response =  await chrome.runtime.sendMessage('scrape-again');
     console.log(response);
    //  chrome.runtime.sendMessage('scrape-again', (response) => {
    //   console.log('received user data', response);
    // });

    //  (async () => {
    //     const response = await chrome.runtime.sendMessage('', "message");
    //     console.log(response);
    //   })();
     
    //  chrome.tabs.sendMessage(tab.id, {text:"getStuff"}, function(response) {
      
    //   if(response.type == "test"){
    //     console.log('test received');
    //   }
    // });
  }
})

})