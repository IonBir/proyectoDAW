const apicall__ = new MovieDB;
const ui__ = new UI;


function movie(id){
    apicall_.getMovie_byId(id)
        .then(data =>{
           console.log(data.movie.results);
           console.log(data);
           ui_.showMovie_byId(data.movie);
           ui_.showCredits(data.movie_credits);
           console.log(data.movie_credits);
        })
        .catch(error =>console.log(error.message))
    console.log(id);

}