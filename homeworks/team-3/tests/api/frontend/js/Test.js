function Test(url,container) {
	this.url = url;
	this.init = function(){
		$.get(this.url,this.render);
		/*give init callbac  = this.render*/
	}
	this.container = document.getElementById(container)
	this.render = function(...arg){
		this.container.innerHTML = `<div>${arg}</div>`
	}
	return this;
}

