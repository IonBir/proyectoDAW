const apicall_ = new MovieDB;
const ui_ = new UI;
var id=document.getElementById('my-data').getAttribute("data-name");
var actorid=document.getElementsByClassName('span');
console.log(id);
function movie(id){
    apicall_.getMovie_byId(id)
        .then(data =>{
          
           ui_.showMovie_byId(data.movie);
           ui_.showCredits(data.movie_credits);
           console.log(data.movie_credits);
        })
        .catch(error =>console.log(error.message))
    
}

function review(id){
    fetch(`${window.origin}/reviews`,{
        method:"POST",
        credentials:"include",
        body:JSON.stringify({
            id:`${id}`
        }),
        cache:"no-cache",
        headers:new Headers({
            "content-type":"application/json"
        })
    })
    .then(result =>{
        
        
        r=result.json()
       
    .then(r =>{
       
        ui_.showReviews(r)
    })
    })
      
    
}

function showAlert(message,className){
    const div=document.createElement('div');
    div.className = `alert alert-${className}`;
    div.appendChild(document.createTextNode(message));
    const parent =document.getElementById('message');
    parent.appendChild(div);
    setTimeout(function(){
        document.querySelector('.alert').remove();
      }, 2000);
}
function addReview(){
    
}
    

window.onload=function(){
    movie(id);
    review(id);
    
}


function actor(id){
    window.location.href=`/actor/${id}`;


}

function favorite(movie_id,movie_name,genre,poster){
    console.log(movie_name);
    fetch(`${window.origin}/favorite`,{
        method:"POST",
        credentials:"include",
        body:JSON.stringify({
            id:movie_id,
            name:movie_name,
            genre:genre,
            image:poster
            
        }),
        cache:"no-cache",
        headers:new Headers({
            "content-type":"application/json"
        })
    })
    .then(result =>{
        
       
        r=result.json()
        
    
    .then(r =>{
        if(r==true){
            document.getElementById("star").className = "fas fa-star";
            showAlert('Added to favorites','success')
        }
        else if(r==false){
        document.getElementById("star").className = "far fa-star";
        showAlert('Removed from favorites','danger')
        }
        else{
            document.getElementById("star").className = "far fa-star";
            showAlert('You need to be logged in','danger')
        }
    })
})
}

  