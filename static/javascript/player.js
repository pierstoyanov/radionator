// //Play button solution from https://stackoverflow.com/a/46258190/13673831
//
// //https://stackoverflow.com/questions/20616430/html5-javascript-play-pause-button
//
// function playRadio () {
//   document.getElementById("play_button").addEventListener("click")
// }
//
//
//
//
//
// var radioStreaming = false;
//
// function setRadio(){
//   var radioURL = document.createElement("audio");
//   radioURL.src = "http://46.10.150.243/njoy.mp3";
//   // document.getElementById("play_radio").addEventListener("click", function(music){
//   //   radioURL.play();
//   // }, true);
//
//   radioURL.onStreaming = function () {
//     isStreaming = true;
//   };
//   radioURL.notStreaming = function () {
//     isStreaming = false;
//   };
//
// }
//
// function togglePlay() {
//   isStreaming ? radioURL.play() : radioURL.stop()
// }
//
// function playRadio() {
//   setRadio();
//   document.getElementById("play_radio").addEventListener("click", function(music){
//     togglePlay(setRadio);
//   }, true);
// }
//
// playRadio();
//
//
//
//
//
//
//
//
// function play_pause() {
//   var radioPlayer = document.getElementById('play_radio')
//   if (radioPlayer.paused) {
//     radioPlayer.play();
//     $('.play-button'.hide());
//     $('.pause-button'.show());
//   }
//   else {
//     radioPlayer.pause();
//     $('.play-button'.show());
//     $('.pause-button'.hide());
//   }
// }