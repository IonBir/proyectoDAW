class UI{
    constructor(){
        this.movie = document.getElementById('movie');
    }

    showMovie(movie){
        
      let output = "";
  
      movie.forEach(function(movie) {
        
        var url=movie.poster_path;
        output += `
        <div class="card-view">
        <div class="card-header ">
        <a href="/movie/${movie.id}">
        <img src="http://image.tmdb.org/t/p/original${url}" style="height: 100%;"  alt=""><img/>
        </a>
        </div>
        <div class="card-movie-content">
        <div class="card-movie-content-head">
        <a href="/movie/${movie.id}">
        <h3 class="card-movie-title">${movie.title}</h3>
        </a>
        <div class="ratings"><span>${movie.vote_average}</span>/10</div>
        </div>
        <div class="card-movie-info">
        <div class="movie-running-time">
        <label>Release Date</label>
        <span>${movie.release_date}</span>
        </div>
        
        </div>
        </div>
        </div>
        `;
        console.log
      });
      
      document.getElementById('row').innerHTML = output;
    }

  showMovie_byId(movie){
    let output = " ";
      
      var url=movie.poster_path;

      var url_=url.slice(1,-4);
      
      output += `
      
      <div class="card_left">
        <img src="http://image.tmdb.org/t/p/original${url}" alt=""><img/>
      </div>
      <div class="card_right">
        <h1>${movie.title}</h1>
        <div class="card_right__snipet">
          <ul>
            <li>${movie.release_date}</li>
            <li>${movie.runtime} min.</li>
            <li>${movie.genres[0].name}</li>

            <li><i" id ="star" onclick="favorite(${movie.id},'${movie.title}', '${movie.genres[0].name}', '${url_}')"class="far fa-star"></i></li>
          </ul>
          <div class="card_right__review">
            <p>${movie.overview}</p>
            
          </div>
          
          <div id ="actors"></div>
        </div>
      </div>
    
    
      `;
  
    document.getElementById('card').innerHTML = output;
  }


  showCredits(credits){
    let output = `<div class="mb-2">
    <div class="row">`;
    
    for(var i=0;i<5;i++){
      var image = credits.cast[i].profile_path;
    output += `     
    <div class="col-md-2 style:"padding:left=10;">
    <span onclick="actor(${credits.cast[i].id})"style="display:inline;"><img class="rounded-circle" src="http://image.tmdb.org/t/p/original${image}" height="75" width="75"></span>
    <br><br>
    </div>
`;
    }
output+=`</div>
</div>`
document.getElementById('actors').innerHTML = output;
}



showReviews(review)
{
  let output = " ";
  for(var i=0;i<review.length;i++){
    output+= `<div class="col-md-10">
    <p>
        <a class="float-left" href=""><strong>${review[i][2]}</strong></a>
        
   </p>
   <div class="clearfix"></div>
    <p>${review[i][4]}</p>
</div>`
  }
  console.log(review.length)
  document.getElementById('reviews_insert').innerHTML = output;
}

    
   


    showActor_byId(actor,movie){
      let output = " ";
        
        var url=actor.profile_path;
        output += `
        <div class="row row-eq-height no-gutters">
        <div class="col-md-6 col-lg-3"><img src="http://image.tmdb.org/t/p/original${url}" height="450" width="293"></div>
        <div class="col-md-6 col-lg-9">
            <div class="d-flex flex-column">
                <div class="d-flex flex-row justify-content-between align-items-center p-5 bg-dark text-white">
                    <h3 class="display-5">${actor.name}</h3>
                </div>
                <div class="p-3 bg-black text-white">
                    <h6>${actor.biography}</h6>
                </div>
                <div class="p-1 bg-black text-white">
                    <br><br>
                </div>
                
            </div>
        </div>
    </div>
    </div>
        
        `;
    
        let output_movie = "";
  
        movie.forEach(function(movie) {
          
          var url=movie.poster_path;
          output += `
          <div class="card-view">
          <div class="card-header ">
          <a href="/movie/${movie.id}">
          <img src="http://image.tmdb.org/t/p/original${url}" style="height: 100%;"  alt=""><img/>
          </a>
          </div>
          <div class="card-movie-content">
          <div class="card-movie-content-head">
          <a href="/movie/${movie.id}">
          <h3 class="card-movie-title">${movie.title}</h3>
          </a>
          <div class="ratings"><span>${movie.vote_average}</span>/10</div>
          </div>
          <div class="card-movie-info">
          <div class="movie-running-time">
          <label>Release Date</label>
          <span>${movie.release_date}</span>
          </div>
          <div class="movie-running-time">
          <label>Running time</label>
          <span>${movie.runtime}</span>
          </div>
          </div>
          </div>
          </div>
          `;
          console.log
        });
        
        document.getElementById('row').innerHTML = output_movie;

      document.getElementById('actor').innerHTML = output;


      
    


    } 
  
  
  }

    
