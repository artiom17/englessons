var id;

function getcustomervoice(ev){
    id=ev.name;
    var change_text = document.getElementById(id);
    var sentence = document.querySelector("[rel=" + id + "]");

    window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    var recognition = new SpeechRecognition();
    recognition.interimResults = true;
    recognition.lang = 'en-US';

    recognition.onresult = function (event) {
        var result = event.results[event.resultIndex];
        var res = result[0].transcript;
        change_text.value = res[0].toUpperCase() + res.slice(1) + sentence.textContent[sentence.textContent.length - 1];
    };

    recognition.start();
}