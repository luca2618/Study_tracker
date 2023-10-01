
console.log("hello from contentscript")
function update(){
    chrome.storage.local.set({course_spots: course_spots})
    chrome.storage.local.set({course_names: course_names})
}


console.log(DOMtoString())

function DOMtoString() {
    selector = document.documentElement;
    return selector.outerHTML;
}