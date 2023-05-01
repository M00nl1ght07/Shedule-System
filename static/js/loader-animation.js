function showHideDiv(div){
    var x = document.getElementById("hide");

    if (x.style.display == 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }

    if (x.style.display == 'block') {
        setTimeout(function() {
            x.style.display = 'none';
        }, 16000) // 3000 - миллисек - задержка
    }

    return false;
}