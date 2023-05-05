function toggleHidden(x) {
    if (x.matches) { // If media query matches
        document.getElementsByClassName('toggle')[0].hidden = false;
    }
    else{
        document.getElementsByClassName('toggle')[0].hidden = true;
    }
}
var x = window.matchMedia("(max-width: 1000px)")
toggleHidden(x) // Call listener function at run time
x.addListener(toggleHidden) // Evento para ser verificado a todo tempo


function toggleActive() {
    document.getElementsByTagName('header')[0].classList.toggle('ativar');
}


