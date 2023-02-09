
function formSubmitHandler(event) {
  event.preventDefault();
  document.getElementById("pro").value = "";
  document.getElementById("qty").value = "";

  const fd = new FormData(event.target);
  const div = document.createElement("div");
  const item = document.createElement("li");
  const list = document.getElementById('products');
  const button = document.createElement('button');
  const para = document.createElement('p');

  item.appendChild(div);
  item.setAttribute('class', 'container d-flex justify-content-center align-items-center row-col-2 m-0')
  div.setAttribute('class', 'container m-auto d-flex justify-content-center align-items-center')
  para.setAttribute('class', 'list-group-item rounded m-auto mx-4 d-inline-block col-7');
  button.setAttribute('class', 'btn-sm btn-outline-secondary border border-1 btn-close col-2 mx-5 p-2');
  button.setAttribute('id', 'btn-close');

  list.appendChild(item);

  let str = ""

  for (const pair of fd.entries()) {
    str += `${pair[0]}: ${pair[1]}     `;
    div.appendChild(para);
    div.appendChild(button);
  }
  para.textContent = str;
  button.addEventListener('click', () => div.remove());
}





