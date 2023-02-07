"use strict"






const myIMG = document.getElementById('myIMG');
const myP = document.getElementById('myP');

const myB = document.getElementById('myB');
const showImgButton = document.getElementById('showImgButton')

let dateDisplay = false;
let imgDisplay = true;

myB.addEventListener('click', showDate);
showImgButton.addEventListener('click', showImg);



function showDate() {

  if (!dateDisplay) {
    myP.innerHTML = new Date().toLocaleDateString('he-IS');
    myB.innerHTML = 'Hide Date';
    dateDisplay = true;
  } else {
    myP.innerHTML = '';
    myB.innerHTML = 'Show Date';
    dateDisplay = false;
  }
}

function showImg() {

  if (imgDisplay) {
    myIMG.style.display = 'None';
    showImgButton.innerHTML = 'Hide Img';
    imgDisplay = false;
  } else {
    myIMG.style.display = 'block';
    showImgButton.innerHTML = 'Show Img';
    imgDisplay = true;
  }
}



