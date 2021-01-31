//   video

const myVideo = document.getElementById('myVideo');
const nextVideo = document.getElementById('next');
const prevVideo = document.getElementById('prev');

nextVideo.addEventListener('click', nextVideos);


const vido = ["video1.mp4", "video2.mp4", "video3.mp4", "video4.mp4", "video5.mp4", "video6.mp4"];


// next vdo
let vidPlaying = 0;

function nextVideos() {

    if (vidPlaying < vido.length) {
        vidPlaying++;
    } else {
        vidPlaying = 0;

    }
    myFunction();

}
//next video


function myFunction() {
    myVideo.src = "../course/cvideo/" + vido[vidPlaying];
}




// Label

var userSelection = document.getElementsByClassName('label-cls');

for (let i = 0; i < userSelection.length; i++) {
    userSelection[i].addEventListener("click", function() {

        myVideo.src = "../course/cvideo/" + vido[i];
    })
}





//  label