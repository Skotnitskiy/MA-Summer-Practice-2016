function Test(url, container) {
    this.url = url;
    this.refresh = function () {
        this.questionID = 1;
        this.profession = '';
        this.professions = {};
        this.madeChoise = false;
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
    this.onSubmit = function () {
        if(this.madeChoise){
            this.questionID += 1;
        if (this.professions[this.profession]) {
            this.professions[this.profession] += 1;
        } else {
            this.professions[this.profession] = 1;
        }
        this.render();
            this.madeChoise = false;
        }
    };
    this.onClick = function (t) {
        this.madeChoise = true;
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
            <div class="header post-header">
                 <div class="header-wrapper">
                    <div class="wrapper wrapper-left">
                    </div>
                    <div class="header-middle">
                        <div class="title">${currentState.body}</div>
                    </div>
                    <div class="wrapper wrapper-right-check">
                        <div class="circle" onclick="onSubmit();">
                            <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 78.369 78.369">
                    <path d="M78.05 19.015l-48.592 48.59c-.428.43-1.12.43-1.548 0L.32 40.016c-.427-.426-.427-1.12 0-1.547l6.704-6.704c.428-.427 1.12-.427 1.548 0l20.113 20.112 41.113-41.113c.43-.427 1.12-.427 1.548 0l6.703 6.704c.427.427.427 1.12 0 1.548z" fill="white"/>
                </svg>
                        </div>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-3"></div>
                <div class="col-6">
                    ${answers}	    
                </div>
                <div class="col-3"></div>
            </div>
		`
    };
    this.renderAnswer = function () {
        var result = ['', 0];
        for (key in this.professions) {
            if (this.professions[key] > result[1]) {
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
                <div class="header post-header">
                 <div class="header-wrapper">
                    <div class="wrapper wrapper-left">
                    </div>
                    <div class="header-middle">
                        <div class="title">${this.store['results'][result[0]]}</div>
                    </div>
                    <div class="wrapper wrapper-right-check">
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-3"></div>
                <div class="col-6">
                    ${this.store['results'][result[0]]}	    
                </div>
                <div class="col-3"></div>
            </div>
            `
        }

    };
    this.render = function () {
        this.container.innerHTML = this.state[this.questionID] ? this.renderTest() : this.renderAnswer();
    };
    return this;
}

