// aweosome mute all on element play solution =>
// https://stackoverflow.com/questions/42297703/multiple-audio-auto-stop-other-when-current-is-playing-with-javascript

document.addEventListener('play', function(e){
    // get all <audio> tag elements in the page.
    var allAudios = document.getElementsByTagName('audio');
    // Iterate through all players and pause them, except for
    // the one who fired the "play" event ("target")
    for(var i = 0; i<allAudios.length; i++){
        if(allAudios[i] != e.target){
            allAudios[i].pause();
        }
    }
}, true);