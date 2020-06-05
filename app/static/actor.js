const apicall__ = new MovieDB;
const ui__ = new UI;
var id=document.getElementById('my-data').getAttribute("data-name");
var actorid=document.getElementsByClassName('span');



function actor(id){
    apicall__.Actor_byId(id)
        .then(data =>{
           
           
           
           ui__.showActor_byId(data.actor,data.movie.results);
        })
        .catch(error =>console.log(error.message))
    

}

window.onload=function(){
    actor(id);
   
 
    
}
