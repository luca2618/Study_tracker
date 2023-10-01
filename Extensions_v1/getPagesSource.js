function DOMtoString(document_root) {
    return document.body.innerText ;
    }
    
    chrome.extension.sendMessage({
    action: "getSource",
    source: DOMtoString(document)
    });