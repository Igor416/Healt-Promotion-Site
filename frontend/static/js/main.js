let links = document.getElementById("links")
let timeLabel = document.getElementById("time")

function display(i) {
    if (i === links.children.length) return

    links.children[i].style.margin = '0'
    setTimeout(() => display(i + 1), 100);
}

function adjustTime(val) {
  let vals = {
    0: '1 неделя',
    1: '2 недели',
    2: '1 месяц',
    3: '2 месяца',
    4: '3 месяца',
    5: 'полгода',
    6: 'год',
    7: '2 года',
    8: '3 года',
    9: '5+ лет'
  }
  val = Math.floor(val / 10)
  timeLabel.innerText = vals[val]
}
