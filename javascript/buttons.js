const yes = document.querySelector('yes');
const no = document.querySelector('no');

yes.addEventListener('click', () =>{
  console.log("i've been clicked")
  document.querySelector("yesnobuttons").style.visibility = "hidden";
  document.querySelector("userinput").style.visibility = "visible";

});
