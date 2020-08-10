var id;


function translateText(ev) {
    id=ev.target.name;
    var translationText = document.getElementById(id);
    translationText.classList.add('active');
    ev.target.remove();
}

function allowDrop(ev){
    ev.preventDefault();
}
function dragStart(ev){
    id=ev.target.id;
    ev.dataTransfer.setData("text", ev.target.textContent);

    //alert(id);
}
function drop(ev){
    ev.preventDefault();
    ev.target.append(document.getElementById(id));
    var data = ev.dataTransfer.getData("text");
    var textSelection = document.createTextNode(data);
    ev.target.appendChild(textSelection);
    var oldval = ev.target.value;
    var newval = oldval + data;
    ev.target.value = newval;
}
function passText(ev){
    ev.preventDefault();
    id=ev.target.id;
    var name = ev.target.name;
    var getWordMain = document.getElementById(id).textContent;
    var textSelection = document.createTextNode(getWordMain);
    var input_one;
    for (var i = 1; i <= 5; i++){
        input = document.getElementById("drop_" + i);
        if (name == input.id){
            input_one = input
            input_one.appendChild(textSelection);
            var oldval = input_one.value;
            var newval = oldval + getWordMain;
            input_one.value = newval;
            document.getElementById(id).remove();
            return input_one
        }
    }
}