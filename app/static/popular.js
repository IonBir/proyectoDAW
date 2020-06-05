const apicall_ = new MovieDB;
const ui_ = new UI;

window.onload=function(){
    apicall_.Popular_Movies()
    .then(data =>{
        console.log(data);
        ui_.showMovie(data.movie.results);
    })
     
 }