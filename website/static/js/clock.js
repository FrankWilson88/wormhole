function clock(){
  var day = new Date();
  var today = day.toDateString()
  var h = ("0" + day.getHours()).slice(-2);
  var m = ("0" + day.getMinutes()).slice(-2);
  var s = ("0" + day.getSeconds()).slice(-2);
  time = h + ':' + m + ':' + s;
  document.getElementById("clock").innerHTML = today + ' @ ' + time;
}
setInterval(clock, 1000);

document.getElementById('copyright').outerHTML = "2019-" + new Date().getFullYear();
console.log("Clock Feature is Loaded");
