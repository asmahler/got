function background(){
var images = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg'];
var background = document.querySelector('body');
var random = Math.floor(Math.random() * 5);
	background.style.backgroundImage = "url(/static/images/"+images[random]+")";
		
	}

window.onload = function(){
	background();
}