

const mainDiv = document.getElementById('infoEndPoint');
const displayUl = document.createElement('ul');
displayUl.setAttribute('class', 'container w-50 ')

const btn = document.getElementById('btn1');
btn.addEventListener('click', request);

mainDiv.appendChild(displayUl);





function request() {
  fetch('https://www.boredapi.com/api/activity/')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    displayUl.innerHTML = 
      `<li class="bg-dark d-flex justify-content-center rounded mt-5 p-3 text-warning">
        <h3>${data.activity}</h3>
      </li>`;
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
};
