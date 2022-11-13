const locationBtn = document.getElementById("butt");
locationBtn.addEventListener("click", ()=>{
if(navigator.geolocation){//if browser supports the geolocation
navigator.geolocation.getCurrentPosition(onsuccess,onerror);
}
else{
alert("Your browser not supports the geolocation");
}
});

function onsuccess(position){
const{latitude, longitude} =position.coords;//getting latitude and longitude from coords
 document.getElementById("lat").innerHTML=latitude;
 document.getElementById("lon").innerHTML=longitude;
 console.log(latitude);
}
function onerror(error){
infoTxt.innerHTML=error.message;
infoTxt.classList.add("error");
console.log("error")
}