speaks = [{"name": "Alex", "lang": "en-US"}]
const msg = new SpeechSynthesisUtterance();
msg.volume = 1; // 0 to 1
msg.rate = 1; // 0.1 to 10
msg.pitch = 1; // 0 to 2

const voice = speaks[0];
console.log(`Voice: ${voice.name} and Lang: ${voice.lang}`);
voice.voiceURI = voice.name;
msg.lang = voice.lang;

function textSpeak(ev){
    var name = ev.name;
    msg.text = document.getElementById(name).textContent;
    speechSynthesis.speak(msg);
}