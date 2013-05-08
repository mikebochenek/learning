/** 
 * http://stackoverflow.com/questions/13298140/how-to-upload-a-file-in-dart
 */
import 'dart:html';

main() {
  InputElement uploadInput = query('#upload');
  uploadInput.on.change.add((e) {
    // read file content as dataURL
    final files = uploadInput.files;
    if (files.length == 1) {
      final file = files[0];
      final reader = new FileReader();
      reader.on.load.add((e) {
        sendDatas(reader.result);
      });
      reader.readAsDataURL(file);
    }
  });
}

/// send data to server
sendDatas(dynamic data) {
  final req = new HttpRequest();
  req.on.readyStateChange.add((Event e) {
    if (req.readyState == HttpRequest.DONE &&
        (req.status == 200 || req.status == 0)) {
      window.alert("upload complete");
    }
  });
  req.open("POST", "http://127.0.0.1:8080/upload");
  req.send(data);
}
