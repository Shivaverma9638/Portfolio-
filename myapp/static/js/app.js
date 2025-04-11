function showModal(){
  document.querySelector('.overlay').classList.add('showoverlay');
  document.querySelector('.loginform').classList.add('showlogginform');
}
var btnlogin =document.querySelector(".btn-login");
btnlogin.addEventListener("click",showModal);