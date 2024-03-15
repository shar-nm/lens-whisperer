
let select = document.getElementById("select");
let list = document.getElementById("list");
let selectText = document.getElementById("selecttext");
let options = document.getElementsByClassName("options");
let inputField = document.getElementById("inputfield");

select.onclick = function() {
    list.classList.toggle("open");
}


for (option of options){
    option.onclick = function(){
        selectText.innerHTML = this.innerHTML;
        inputField.placeholder = "Search in  "  + selectText.innerHTML;
    }
}