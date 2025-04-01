let slide_index = {};
let slide_count = {};

// Next/previous controls
function gallery_plus(gallery_n, plus) {
  let pos = (slide_count[gallery_n] + slide_index[gallery_n] + plus) % slide_count[gallery_n];
  gallery_show(gallery_n, pos);
}

// Thumbnail image controls
function gallery_set(gallery_n, image_n) {
  gallery_show(gallery_n, image_n);
}

function gallery_show(gallery_n, image_n) {
  slide_index[gallery_n] = image_n;
  for (var i = 0; i < slide_count[gallery_n]; i++) {
    let id_slide = "slide_" + gallery_n + "_" + i;
    let id_demo = "demo_" + gallery_n + "_" + i;
    let slide = document.getElementById(id_slide);
    let demo = document.getElementById(id_demo);
    if (i == image_n) {
      slide.style.display = "block";
      demo.className = "gallery-demo not-default gallery-active";
    } else {
      slide.style.display = "none";
      demo.className = "gallery-demo not-default";
    }
  }
}
