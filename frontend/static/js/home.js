let links = document.getElementById("links")
let slides = document.getElementsByClassName("health-image");
let timeLabel = document.getElementById("time")

setTimeout(() => showSlides(0), 3000);
function display(i) {
    if (i === links.children.length) return

    links.children[i].style.margin = '0'
    setTimeout(() => display(i + 1), 100);
}

function showSlides(slideIndex) {
  time = 3000;
  if (slideIndex === 0) {
    slides[0].style.width = '30vw';
    slides[slides.length - 1].style.width = '0vw';
    slideIndex++;
    time = 0;
  }
  else {
    let prev = slideIndex - 1;
    let i = 0
    let interval = setInterval(() => {
      if (i == 31) {
        clearInterval(interval);
        slideIndex++;
        if (slideIndex === slides.length) {
          slideIndex = 0;
        }
        return;
      }
      slides[slideIndex].style.width = i + 'vw';
      slides[prev].style.width = (30 - i) + 'vw';
      i++;
    }, 15);
  }
  setTimeout(() => showSlides(slideIndex), time);
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
