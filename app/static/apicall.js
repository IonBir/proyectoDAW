const apicall = new MovieDB;
const ui = new UI;

const searchMovie = document.getElementById('searchMovie');

searchMovie.addEventListener('keyup',(e)=>{
    const userText = e.target.value;
    if(userText!== ''){
        apicall.getMovie(userText)
        .then(data =>{
           
           ui.showMovie(data.movie.results);
        })
        .catch(error =>console.log(error.message))
    }
})

