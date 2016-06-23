function load() {
	element=document.getElementsByClassName("unloader")[0];
    element.className="loader";
}
function load_list() {
	element=document.getElementsByClassName("unloader-list")[0];
    element.className="loader";
}

function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}