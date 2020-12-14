// Javascript solution sources:
// https://stackoverflow.com/a/46258190/13673831
// https://www.codeinwp.com/snippets/add-event-listener-to-multiple-elements-with-javascript/
// https://stackoverflow.com/questions/20616430/html5-javascript-play-pause-button
// https://stackoverflow.com/questions/27258169/how-can-i-stop-and-resume-a-live-audio-stream-in-html5-instead-of-just-pausing-i

// let isStreaming = false;
// let playButtons = document.querySelectorAll("play_button");
//
// function playRadio() {
//     let radioURL = document.createElement("audio");
//     radioURL.src = "{{ station.url }}";
//     radioURL.play()}
//     // if (isStreaming === false) {
//     //     radioURL.play()
//     //     isStreaming = true
//     //     console.log("playing")
//     // } else {
//     //     radioURL.pause()
//     //     setTimeout(function () {
//     //         radioURL.load() // This stops the stream from downloading
//     //     })
//     //     console.log("stopped")
//     //     isStreaming = false;
//     // }
// // }
//
// for (i of playButtons) {
//     i.addEventListener("click", playRadio())
// }


// function Play_Audio(){
//   var audioElement = document.createElement("audio",);
//   audioElement.src = stationUrl;
//   document.getElementById("play_button").addEventListener("click", function(music){
//     audioElement.play();
//   }, false);
// }
// Play_Audio();
//
//
// //
//
//
// playRadio();



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