function logInFunc() {
  if (localStorage.getItem('access')) {
    document.getElementById('mainContainer').style.display = 'none';
    document.getElementById('logedInContainer').style.display = 'block';
  }
}

async function getUserData() {
  try {
    const response = await fetch('http://127.0.0.1:8000/me/', {
      headers: {
        'authorization': 'Bearer ' + localStorage.getItem('access')
      }
    })
    const json = await response.json();
    console.log(json);
    if (json.first_name && json.last_name) {
      document.getElementById('mainContainer').style.display = 'none';
      document.getElementById('paraForName').innerText = `Hey ${json.first_name} ${json.last_name}`;
      document.getElementById('logedInContainer').style.display = 'block';
    }
  } catch (error) {
    console.error(error);
  }
}

async function postUserData(event) {
  try {
    event.preventDefault();
    const formData = new FormData(event.target);
    const response = await fetch('http://127.0.0.1:8000/sign_up/', {method: 'POST', body: formData});
    console.log(response, 1);
    const body = {"username": formData.get('username'), "password": formData.get('password')};
    const response2 = await fetch('http://127.0.0.1:8000/api/token/', {method: 'POST', body: new URLSearchParams(body)});
    const json2 = await response2.json();
    localStorage.setItem('access', json2.access);
    localStorage.setItem('refresh', json2.refresh);
    window.open('http://127.0.0.1:5500/front/log_in.html','_self')
    await getUserData()
  } catch (error) {
    console.log(error);
  }
}

window.onload = () => {
  getUserData()
};

async function getTokens(event) {
  try {
    event.preventDefault();
    formData = new FormData(event.target);
    const response = await fetch('http://127.0.0.1:8000/api/token/', {method: 'POST', body: formData});
    console.log(response, 3);
    const json = await response.json();
    console.log(json, 4);
    localStorage.setItem('access', json.access);
    localStorage.setItem('refresh', json.refresh);
    await getUserData()
  } catch (error) {
      console.error(error);
  }
}

function deleteLocalStorage() {
  localStorage.clear()
  window.location.reload()
}