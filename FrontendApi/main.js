let loginBtn = document.getElementById('login-btn')
let logoutBtn = document.getElementById('logout-btn')

let token = localStorage.getItem('token')

if (token) {
    loginBtn.remove()
} else {
    logoutBtn.remove()
}


logoutBtn.addEventListener('click', (e) =>{
    e.preventDefault()
    localStorage.removeItem('token')
    window.location = "file:///C:/Users/Tony%20SigmaWolf/Desktop/Projects/DevLog-Frontend/login.html"

})
let projectUrl = 'http://127.0.0.1:8000/api/projects/'

let getProjects = () => {

    fetch(projectUrl)
        .then(response => response.json())
        .then(data => {
        console.log(data)
        buildProjects(data)
        })
}

let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById('projects--wrapper')
    projectsWrapper.innerHTML = ''      // Clear old project items after event appear
    for (let i = 0; projects.length > i; i++) {
        let project = projects[i]
        
        // Create html element
        let projectCard = `
            <div class="project--card">
                <img src="http://127.0.0.1:8000${project.featured_image}">
                
                <div>
                    <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
                        <strong class="vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
                    </div>
                    <i>${project.vote_ratio}% Possitive feedback </i>
                    <p>${project.description.substring(0,150)}</p>
                </div>
            </div>
        `

        projectsWrapper.innerHTML += projectCard    // append project card to render data from api
    }

    addVoteEvents()
}


let addVoteEvents = () => {
    let voteBtns = document.getElementsByClassName('vote--option')  // Get element by class name from a class(vote--option) in div tag 
    

    // Loop to check if an event of click was trigger
    // use console.log to check if an event occurs
    // This is a basic interaction of front end which can be add to web project 
    // There are many type of listener aka event check build in javascript
    for (let i = 0; voteBtns.length > i; i++) {
        voteBtns[i].addEventListener('click', (e) => {
            let token = localStorage.getItem('token')
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project
            
            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
                method:'POST', 
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({'value' : vote})
            })
                .then(response => response.json())
                .then(data => {
                    console.log('success:', data)
                    getProjects()
                })
        })
    }
}


getProjects()