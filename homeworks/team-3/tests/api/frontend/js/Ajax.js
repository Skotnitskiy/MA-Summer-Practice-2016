//ajax request methods
var $ = {};
$.get = function(url,cb){
	var res = url+'res';
	var xhr = new XMLHttpRequest();
	xhr.open('GET', encodeURI(url));
	xhr.onload = function() {
	    if (xhr.status === 200) {
	    	cb(xhr.responseText);
	    }
	    else {
	        alert('Request failed.  Returned status of ' + xhr.status);
	    }
	};
	//return res;
}
$.post = function(url,data,cb){}
$.put = function(url,data,cb){}
$.delete = function(url,cb){}

/*
var xhr = new XMLHttpRequest();
xhr.open('GET', encodeURI('https://jsonblob.com/api/jsonBlob/579a562be4b0dc55a4e88dbd'));
xhr.onload = function() {
    if (xhr.status === 200) {
        console.log(xhr.responseText);
        alert('User\'s name is ' + xhr.responseText);
    }
    else {
        alert('Request failed.  Returned status of ' + xhr.status);
    }
};
xhr.send();

xhr.open("POST", "https://jsonblob.com/api/jsonBlob/579a562be4b0dc55a4e88dbd", true); 
xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");                  
xhr.send(data);
*/