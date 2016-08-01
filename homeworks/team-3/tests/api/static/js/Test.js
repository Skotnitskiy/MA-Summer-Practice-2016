function Test(url, container) {
    this.url = url;
    this.refresh = function () {
        this.questionID = 1;
        this.profession = '';
        this.professions = {};
    };
    this.init = function () {
        $.get(this.url, this.setStore);
        this.refresh();
    };
    this.setStore = function (data) {
        this.store = data;

        this.state = data['main-questions'];
        if (this.state === undefined) {
            this.state = data['questions'];
        }
        this.render();
    }
    this.container = document.getElementById(container);
    /**
     *
     * if next this.questionID exit -> count professions and stop
     * else this.questionID+=1 and add to choosen proffesion = one and rerender
     *
     * @param e
     * */
    this.onSubmit = function (e) {
        this.questionID += 1;
        if (this.professions[this.profession]) {
            this.professions[this.profession] += 1;
        } else {
            this.professions[this.profession] = 1;
        }
        this.render();
    };
    this.onClick = function (t) {
        this.profession = t.value;
    };
    this.renderTest = function () {
        var currentState = this.state[this.questionID];
        var answers = '';
        for (var key in currentState.answers) {
            if (currentState.answers.hasOwnProperty(key)) {
                var value = '';
                for (a in currentState.answers[key]){
                    if(a!=='answer'){
                        value = a;
                    }
                }
                answers += `
                <input type="radio" value="${value}" name="prof" onclick="onClick(this);"> ${currentState.answers[key]['answer']}</br>
                `;
            }
        }
        return `
			<div>
				${currentState.body}
				<form onsubmit="event.preventDefault(); onSubmit(event);">
				    ${answers}
				    <input type="submit" value="Submit">
                </form>
			</div>
		`
    };
    this.renderAnswer = function () {
        var result = ['', 0];
        for (key in this.professions) {
            if (this.professions[key] > result[1]) {
                // console.log(key);
                result[1] = this.professions[key];
                result[0] = key;
            }
        }

        if (this.store['next']) {
            this.setStore(this.store['next'][result[0]]);
            this.refresh();
            return this.renderTest();
        }
        if (this.store['results']) {
            return `
                <div>
                    ${this.store['results'][result[0]]}
                </div>
            `
        }

    };
    this.render = function () {
        this.container.innerHTML = this.state[this.questionID] ? this.renderTest() : this.renderAnswer();
    };
    return this;
}

