const yes = document.querySelector('#yes');
const no = document.querySelector('#no');

yes.addEventListener('click', () =>{
  console.log("i've been clicked")
  document.querySelector("#yesnobuttons").style.visibility = "hidden";
  document.querySelector("#userinput").style.visibility = "visible";
  document.querySelector("#average").style.visibility = "visible";

  document.querySelector("#averageset").style.visibility = "hidden";

});
no.addEventListener('click', () =>{
  console.log("i've been clicked")
  document.querySelector("#yesnobuttons").style.visibility = "hidden";
  document.querySelector("#userinput").style.visibility = "hidden";
  document.querySelector("#average").style.visibility = "visible";

  document.querySelector("#averageset").style.visibility = "hidden";
});
