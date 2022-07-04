var menu = document.getElementById("openMobileMenu");
function openMenu(){
  if (menu.style.display == "block"){
    menu.style.display = "none";
  }
  else{
    menu.style.display = "block";
  }
}

var width = window.outerWidth;
var pTag = document.getElementById("greeting");
if (width <= "599"){
  pTag.style.display = "none";
}
else{
  pTag.style.display = "block";
}

var mobile = document.getElementById("mobileDropdown");
function openDropdown(){
  if (mobile.style.display == "block"){
    mobile.style.display = "none";
  }
  else {
    mobile.style.display = "block";
  }
}

console.log("Mobile Menu Feature is Loaded")
