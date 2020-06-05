class MovieDB{
    constructor(){
        this.client_secret = '43e36c48434c49f4d6bd5a7e27bef9bb';
    
}

async getMovie(moviename) {
    const MovieResponse = await fetch(`https://api.themoviedb.org/3/search/movie?api_key=${this.client_secret}&query=${moviename}`);
    const movie = await MovieResponse.json();

    return{
        movie
    }
   
}
async getMovie_byId(id) {
    const MovieResponse = await fetch(`https://api.themoviedb.org/3/movie/${id}?api_key=${this.client_secret}`);
    const movie = await MovieResponse.json();
    const MovieResponseCredits = await fetch(`https://api.themoviedb.org/3/movie/${id}/credits?api_key=${this.client_secret}`);
    const movie_credits = await MovieResponseCredits.json();
    
    return{
        movie,
        movie_credits
    }
   
}


async Actor_byId(id) {
    const actorResponse = await fetch(`https://api.themoviedb.org/3/person/${id}?api_key=${this.client_secret}`);
    const actor = await actorResponse.json();
    const movieResponse= await fetch(`https://api.themoviedb.org/3/discover/movie?api_key=${this.client_secret}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_people=${id}`)
    const movie = await movieResponse.json();
    
    return{
        actor,
        movie
    }
   
}

async Popular_Movies(){
    const movieResponse= await fetch(`https://api.themoviedb.org/3/movie/popular?api_key=${this.client_secret}&language=en-US&page=1`);
    const movie = await movieResponse.json();

return {
    movie
}
}





async Discover_Movies(genre,year){
    if(genre == null){
        var search_genre=""
    }else{
        var search_genre=`&with_genres=${genre}`
    }
    if(year == null){
        var search_year=""
    }else{
        var search_year=`&primary_release_year=${year}`
    }
    const movieResponse= await fetch(`https://api.themoviedb.org/3/discover/movie?api_key=${this.client_secret}&language=en-US&sort_by=popularity.desc&include_adult=false&page=1${search_genre}${search_year}`);
    const movie = await movieResponse.json();

    return{
        movie
    }
}
}