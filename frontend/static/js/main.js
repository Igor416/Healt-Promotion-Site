let links = document.getElementById("links")


function display(i) {
    if (i === links.children.length) return

    links.children[i].style.margin = '0'
    setTimeout(() => display(i + 1), 100);
}
