document.addEventListener("DOMContentLoaded", function() {
    // Get the <body> element
    var body = document.body;
  
    // Get all the text content within the <body> element
    var allText = getAllTextContent(body);
  
    // Print or use the text as needed
    console.log(allText);
  });
  
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