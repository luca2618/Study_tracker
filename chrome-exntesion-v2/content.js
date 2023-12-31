

var body = document.body;

// chrome.runtime.onMessage.addListener(
//   function(request, sender, sendResponse) {
//     // if(sender.status ===  "complete") {
//       if (request.text == "getStuff") {
//         console.log('test sent');
//         sendResponse({type: "test"});
//       }
//     // }
// });

  // chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  //   done = {
  //     sent: true
  //   }
  //   if (message === 'scrape-again') {
  //     console.log("scrape-again'")
  //     sendResponse(done);
  //   }
  // });

  async function getFoo() {
    return "bar"
  }

  async function sendFoo(sendResponse) {
    const foo = await getFoo()
    sendResponse({ foo })
  }

  chrome.runtime.onMessage.addListener(
    console.log("I am here"),
    function (request, sender, sendResponse) {
      if (request.type === "scrape-again") {
        sendFoo(sendResponse)
        return true
      }
    }
  );

  function getAllData(){
    if(body){
      //   chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
      //     let url = tabs[0].url;
      //     // use `url` here inside the callback because it's asynchronous!
      //     console.log(url);
      // });
          
          // Get all the text content within the <body> element
          var data = getAllTextContent(body);
  
        try{
          (async () => {
        
          const rawResponse = await fetch('http://localhost:8000/classify?data='+data, {
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
            },
            body: ""
          });
          const content = await rawResponse.json();
          console.log("Content is ",content);
          const today = new Date();
          const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
          console.log(time)
          // chrome.storage.local.get("dataObject",function(res) {
          //   console.log("Object is",res)
          // });
        

        // const obj = {
        //   data: dataArr.push(2),
        //   time: "123231"
        // };
  
          // chrome.storage.local.set({
          //       dataObject: content
          // }, function () {
          //     chrome.tabs.executeScript({
          //         file: "index.js"
          //     });
          // });
        //   chrome.storage.local.get("dataObject",function(res) {
        //     console.log("Object is",res)
        // });

        // const obj = {
        //   data: dataArr.push(2),
        //   time: "123231"
        // };
        // var countProd = 0;
        // chrome.storage.local.get("countProd", function(res){
        //   console.log("where",res["countProd"])
        //   if(typeof(res[countProd])===undefined){
        //     res["countProd"] = 1
        //   }
        //   if(res["countProd"] && content==="productive"){
        //     countProd  = res["data"] + 1;
        //     console.log("ifcount is",countProd)

        //     chrome.storage.local.set({
        //       data: [ countProd,  countUnprod]
        // }, function () {
        //     chrome.tabs.executeScript({
        //         file: "index.js"
        //     });
        // });
        //   }
        // })
if(content==="productive"){
  chrome.storage.local.get(["prod"]).then((result) => {
    console.log("Value currently is " + result.prod);
    if (typeof(result.prod) === 'undefined'){
        
        chrome.storage.local.set({ prod: 0 }).then(() => {
            console.log("Value is set to 0");
          });
        chrome.storage.local.get(["prod"]).then((result) => {
        console.log("Value currently is " + string(result.prod));
        });
}else{
chrome.storage.local.set({ prod: result.prod+1 }).then(() => {
  console.log("Value is set to prod");
});

chrome.storage.local.set({ current: "productive" }).then(() => {
  console.log("Value is set to ");
});

}
  });
}else{
  chrome.storage.local.get(["unprod"]).then((result) => {
    console.log("Value currently is " + result.unprod);
    if (typeof(result.unprod) === 'undefined'){
        
        chrome.storage.local.set({ unprod: 0 }).then(() => {
            console.log("Value is set to 0");
          });
        chrome.storage.local.get(["unprod"]).then((result) => {
        console.log("Value currently is " + string(result.unprod));
        });
}else{
chrome.storage.local.set({ unprod: result.unprod+1 }).then(() => {
  console.log("Value is set to unprod");
});
chrome.storage.local.set({ current: "unproductive" }).then(() => {
  console.log("Value is set to ");
});

}
  });
}
        


      
  
 
  
          })()
        }catch(error){
        console.log(error)
      };
      }
  }


  setInterval(() => {
    getAllData();
  }, 5000);

      
      // Function to recursively get all text content within an element
      function getAllTextContent(element) {
        var text = '';
      
        // Check if the element is a text node (nodeType 3) or an element node (nodeType 1)
        if (element.nodeType === 3) {
          // Text node, add its text content
          text += element.textContent;
        } else if (element.nodeType === 1) {
          // Element node, recursively traverse its child nodes
          for (var i = 0; i < element.childNodes.length; i++) {
            text += getAllTextContent(element.childNodes[i]);
          }
        }
      
      return text;
}