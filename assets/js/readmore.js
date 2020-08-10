function readMoreFunc(element){
    var readmore = document.getElementById('readmore');
    var readescape = document.getElementById('dots');
    var btnReadMore = document.getElementById('btn_readmore');
    var btnReadMoreEscape = document.getElementById('btn_readmore_escape');
    if (element.id == 'btn_readmore'){
        readmore.classList.add('active');
        btnReadMore.classList.add('active');
        readescape.classList.add('active');
        btnReadMoreEscape.classList.add('active');
    }else{
        readmore.classList.remove('active');
        btnReadMore.classList.remove('active');
        readescape.classList.remove('active');
        btnReadMoreEscape.classList.remove('active');
    }
}