let previous_top = 0;
let can_change = true;
let scroll_user = 0;
let toc_toggled = false;
let all_elements = null;
let all_links = null;
let toc_element = null;
let link_by_id = {};
let current_id = null;

function toc_update() {
	let big_screen = window.matchMedia('(min-width: 75rem)').matches;

	if (!can_change) return;

	let first = true;
	let answer = null;
	all_elements.forEach((element) => {
		let rect = element.getBoundingClientRect();
		let id = element.getAttribute("id");
		let hidden = rect.top == 0 && rect.bottom == 0 && rect.left == 0 && rect.right == 0;
		if (!hidden) {
			let pos = rect.top;

			if (pos > 10 && first) {
				answer = id;
			} else if (pos < 10) {
				answer = id;
			}
			first = false;
		}
	});

	if ((answer != null && answer != current_id) || scroll_user != 0) {
		current_id = answer;
		all_links.forEach((x) => {
			x.classList.remove("active");
			x.classList.remove("selected");
		});
		let sel = link_by_id["#" + answer];
		sel.classList.add('active');

		let parent = sel.parentElement;
		while (true) {
			if (parent.tagName.toLowerCase() == "li") {
				parent.children[0].classList.add('selected');
				parent = parent.parentElement;
			} else if (parent.tagName.toLowerCase() == "ul") {
				// do nothing
				parent = parent.parentElement;
			} else {
				break;
			}
		}

		if (big_screen) {
			let rect = sel.getBoundingClientRect();
			let top = rect.top - window.innerHeight / 2. + previous_top + scroll_user;
			if (top > 20) {
				previous_top = top;
				scroll_user = 0;
				top = -top;
				toc_element.style["transform"] = `translateY(${top}px)`;
			} else {
				previous_top = 20;
				scroll_user = 0;
				toc_element.style["transform"] = ``;
			}

			can_change = false;
			setTimeout(function() {
				can_change = true;
			}, 320)
		}
	}
}

window.addEventListener('DOMContentLoaded', () => {
	let toc_elements = {};
	toc_element = document.querySelector('.section-nav');

	all_links = document.querySelectorAll(`.section-nav a`);
	all_links.forEach((x) => {
		toc_elements[x.getAttribute("href")] = true;
		link_by_id[x.getAttribute("href")] = x;
	});
	all_elements = Array.from(document.querySelectorAll('h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]')).filter((x) => toc_elements["#" + x.getAttribute("id")]);

	toc_update();

	toc_element.addEventListener("wheel", (e) => {
		let big_screen = window.matchMedia('(min-width: 75rem)').matches;
		if (!big_screen) return;

		e.preventDefault();
		scroll_user = scroll_user + e.deltaY / 2;
		let top = -(previous_top + scroll_user);
		toc_element.style["transform"] = `translateY(${top}px)`;
	});

	document.addEventListener("scroll", (e) => {
		toc_update();
	});

	window.addEventListener('resize', (e) => {
		toc_update();
	});
});
