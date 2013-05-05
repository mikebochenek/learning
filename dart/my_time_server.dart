library time_server;

import "dart:io";

const HOST = "localhost";
const PORT = 18181;

void main() {
  HttpServer.bind(HOST, PORT).then((HttpServer server) {
    server.listen(requestReceivedHandler);
  });

  print("Serving the current time on http://${HOST}:${PORT}.");
}

void requestReceivedHandler(HttpRequest request) {
  print("Request: ${request.method} ${request.uri} at ${new DateTime.now()}");

  request.response.headers.set(
      HttpHeaders.CONTENT_TYPE, "text/html; charset=UTF-8");
  request.response.write(createHtmlResponse());
  request.response.close().catchError(print);
}

String createHtmlResponse() {
  return
'''
<html>
  <style>
    body { background-color: white; }ap
    p { background-color: white; border-radius: 8px;
        border:solid 1px #555; text-align: center; padding: 0.5em;
        font-family: "Lucida Grande", Tahoma; font-size: 18px; color: #555; }
  </style>
  <body>
    <p>Current time: ${new DateTime.now()}</p>
  </body>
</html>
''';
}
