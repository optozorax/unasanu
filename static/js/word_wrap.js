function cloneAttributes(element, sourceNode) {
  let attr;
  let attributes = Array.prototype.slice.call(sourceNode.attributes);
  while(attr = attributes.pop()) {
    element.setAttribute(attr.nodeName, attr.nodeValue);
  }
}

window.addEventListener('DOMContentLoaded', () => {
	let re = /^[ \t]+/;
	document.querySelectorAll(".main-content pre code").forEach((code) => {
		let first_elem_in_line = true;
		let table = null;
		let tr = null;
		let td1 = null;
		let td2 = null;
		let span1 = null;
		let span2 = null;
		let new_code = document.createElement("code");
		new_code.classList = code.classList;
		cloneAttributes(new_code, code);
		new_code["data-lang"] = code["data-lang"];
		code.querySelectorAll("span").forEach((span) => {
			let string = span.innerHTML;
			let last_elem_in_line = string.endsWith("\n");

			if (first_elem_in_line) {
				table = document.createElement("span");
				tr = document.createElement("span");
				td1 = document.createElement("span");
				td2 = document.createElement("span");
				span1 = document.createElement("span");
				span1_hidden = document.createElement("span");
				span2 = span.cloneNode();

				table.classList.add("table");
				tr.classList.add("tr");
				td1.classList.add("td");
				td2.classList.add("td");

				td1.classList.add("no-copy");
				span1_hidden.classList.add("hidden-copy");

				let matched = string.match(re);
				if (matched == null) {
					matched = [""];
				}

				span1.innerHTML = matched[0];
				span1_hidden.innerHTML = matched[0];
				span2.innerHTML = string.slice(matched[0].length);

				td1.appendChild(span1);
				td2.appendChild(span1_hidden);
				td2.appendChild(span2);

				span1 = null;
				span2 = null;
			} else {
				let span3 = span.cloneNode();
				span3.innerHTML = span.innerHTML;
				td2.appendChild(span3);
			}

			if (last_elem_in_line) {
				tr.appendChild(td1);
				tr.appendChild(td2);
				table.appendChild(tr);
				new_code.appendChild(table);

				table = null;
				td1 = null;
				td2 = null;
				span1 = null;
				span2 = null;
			}
			first_elem_in_line = last_elem_in_line;
		});
		code.parentNode.replaceChild(new_code, code);
	});
});
