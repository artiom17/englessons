function check(){
    var yes = 0;
    var no = 0;
    var choice;
    for(var v = 1; v <= {{ test_grammar|length }}; v++){
        var q = document.forms['quiz'].elements['question' + v];
        for (var i = 0; i < q.length; i++) {
            if (q[i].checked) {
                choice = q[i].value;
            }
        }
        if (choice == "YES") {
            yes++;
        }
        if (choice == "NO") {
            no++;
        }
    }
    alert("Вы ответили на " + yes + " вопросов из " + (no + yes));
}