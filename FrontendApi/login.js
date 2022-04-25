let form = document.getElementById('login-form')

// Catch event from user action
form.addEventListener('submit', (e) => {  
    e.preventDefault()              // prevent submit information on url (password won't appear on url bar in browser) 
    
    let formData = {
        'username': form.username.value,
        'password': form.password.value
    }

    fetch('http://127.0.0.1:8000/api/users/token/', {
        method:'POST',
        headers:{
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData)
    })
        .then(response => response.json())
        .then(data => {
            console.log('DATA', data.access)
            if (data.access) {
                localStorage.setItem('token', data.access)
                window.location = 'file:///C:/Users/Tony%20SigmaWolf/Desktop/Projects/DevLog-Frontend/projects-list.html'
            } else {
                alert('Username or Password is not correct')
            }
        })
})