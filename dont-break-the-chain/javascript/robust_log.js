/**
 * Source code for all the working examples in this book (along with some 
 * extras that never made it into the text) is available for download from 
 * the book’s web page at www.manning.com/SecretsoftheJavaScriptNinja. 
 */
function log () {
  try {
    console.log.apply(console, arguments);
  } catch(e) { 
    try {
      opera.postError.apply(opera, arguments); 
    } catch(e) {
      alert(Array.prototype.join.call( arguments, "" ));
    }
  }
}
