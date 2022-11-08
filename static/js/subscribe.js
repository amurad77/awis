
let form = document.getElementById('subscribe-form' );

let error_section =  document.getElementById('error-list');
form.addEventListener('submit', async function (e) {
    e.preventDefault();
    error_section.innerText = '';
    let form_data = {
        'email': form.email.value
    }
    let response = await fetch('http://localhost:8000/api/subscribe/', {
        headers: {
            'content-type': 'application/json',
            "X-CSRFToken": form.csrfmiddlewaretoken.value
        },
        method: 'POST',
        body: JSON.stringify(form_data)
    })
    let response_data = await response.json();
    let status = await response.ok;
    
    if(status === true){
        alert('Ugurla abone oldunuz');
        document.getElementById('mce-EMAIL').value = ''
    }
    else{
        for(let error of response_data.email) {
           error_section.innerHTML += `<li class="text-danger">${error}</li>`  
        }
    }

}) 






let form2 = document.getElementById('form-subscribe' );

let error_section2 =  document.getElementById('error-list2');
form2.addEventListener('submit', async function (e) {
    e.preventDefault();
    error_section2.innerText = '';
    let form_data = {
        'email': form2.email.value
    }
    let response = await fetch('http://localhost:8000/api/subscribe/', {
        headers: {
            'content-type': 'application/json',
            "X-CSRFToken": form.csrfmiddlewaretoken.value
        },
        method: 'POST',
        body: JSON.stringify(form_data)
    })
    let response_data = await response.json();
    let status = await response.ok;
    
    if(status === true){
        alert('Ugurla abone oldunuz');
        document.getElementById('mce-EMAIL2').value = ''
    }
    else{
        for(let error of response_data.email) {
           error_section2.innerHTML += `<li class="text-danger">${error}</li>`  
        }
    }

}) 