function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

document.addEventListener("DOMContentLoaded", function () {
  // Faz textarea aumentar a altura automaticamente
  // Fonte: https://www.geeksforgeeks.org/how-to-create-auto-resize-textarea-using-javascript-jquery/#:~:text=It%20can%20be%20achieved%20by,height%20of%20an%20element%20automatically.
  let textareas = document.getElementsByClassName("autoresize");
  for (let i = 0; i < textareas.length; i++) {
    let textarea = textareas[i];
    function autoResize() {
      this.style.height = "auto";
      this.style.height = this.scrollHeight + "px";
    }

    textarea.addEventListener("input", autoResize, false);
  }

  // Sorteia classes de cores aleatoriamente para os cards
  let cards = document.getElementsByClassName("card");
  for (let i = 0; i < cards.length; i++) {
    let card = cards[i];
    card.className += ` card-color-${getRandomInt(
      1,
      5
    )} card-rotation-${getRandomInt(1, 11)}`;
  }
});

document.addEventListener("DOMContentLoaded", function () {
// Funcao Night Mode !!!
var nightModeStatus = localStorage.getItem('night-mode')
console.log(nightModeStatus)
const nightModeToggle = document.getElementById('night-mode-toggle');

const body = document.getElementById('body');
const form = document.getElementById('form');
const formTitle = document.getElementById('formTitle');
const formDetails = document.getElementById('formDetails');
const cards = document.getElementsByClassName('card');
const cardTitle = document.getElementsByClassName('card-title');
const cardContent = document.getElementsByClassName('card-content');

if (nightModeStatus === 'true') {
  console.log('nighto modo');
  console.log(body.classList)
  body.classList.toggle('night-mode');
  form.classList.toggle('form-card-night-mode');
  formTitle.classList.toggle('form-card-night-mode');
  formDetails.classList.toggle('form-card-night-mode');
  for(let i = 0; i < cards.length; i++) {
    let colorNumber = cards[i].classList.item(1).split('-')[2];
    console.log(colorNumber);
    cards[i].classList.toggle(`card-color-${colorNumber}-night-mode`);
  }
  Array.from(cardTitle).forEach(el => el.classList.toggle('card-font-color-night-mode'));
  Array.from(cardContent).forEach(el => el.classList.toggle('card-font-color-night-mode'));
};

nightModeToggle.addEventListener('click', () => {
    if (nightModeStatus === 'false') {
      localStorage.setItem('night-mode', 'true');  
    } 
    else if (nightModeStatus === null) {
      localStorage.setItem('night-mode', 'true');
    }
    else {
      localStorage.setItem('night-mode', 'false');
    }
    location.reload();
});
});