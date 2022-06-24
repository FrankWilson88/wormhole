function tab(page,item){
  content = document.getElementsByClassName("content");
  for (i = 0; i < content.length; i++){
    content[i].style.display = "none";
  }
  btn = document.getElementsByClassName("btn");
  for (i = 0; i < btn.length; i++){
    btn[i].style.background = "";
  }
  document.getElementById(page).style.display = "block";
  item.style.background = "#0d276";
}
document.getElementById("default").click();
console.log("Tab Feature is loaded");