/** 
 * http://stackoverflow.com/questions/13298140/how-to-upload-a-file-in-dart
 */
import 'dart:io';

main() {
  final server = new HttpServer();
  server.listen('127.0.0.1', 8080);
  server.addRequestHandler((request) => request.path == '/upload' 
      && request.method.toLowerCase() == 'post'
      , (HttpRequest request, HttpResponse response) {
    _readBody(request, (body) {

      // handle your dataURL
      // example with image : data:image/jpeg;base64,/9j/4S2YRXhpZgAATU0AK... 

      // return result
      response.statusCode = HttpStatus.CREATED;
      response.contentLength = 0;
      response.outputStream.close();
    });
  });
}

/// Read body of [request] and call [handleBody] when complete.
_readBody(HttpRequest request, void handleBody(String body)) {
  String bodyString = ""; // request body byte data
  final completer = new Completer();
  final sis = new StringInputStream(request.inputStream, Encoding.UTF_8);
  sis.onData = (){
    bodyString = bodyString.concat(sis.read());
  };
  sis.onClosed = () {
    completer.complete("");
  };
  sis.onError = (Exception e) {
    print('exeption occured : ${e.toString()}');
  };
  // process the request and send a response
  completer.future.then((_){
    handleBody(bodyString);
  });
}
