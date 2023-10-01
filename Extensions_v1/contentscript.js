
// console.log("hello from contentscript")
// function update(){
//     chrome.storage.local.set({})
//     chrome.storage.local.set({})
// }


// console.log(DOMtoString())

// function DOMtoString() {
//     selector = document.documentElement;
//     return selector.outerHTML;
// }


function DOMtoString(document_root) {
    return document.body.innerText ;
    }
    
    chrome.extension.sendMessage({
    action: "getSource",
    source: DOMtoString(document)
    });