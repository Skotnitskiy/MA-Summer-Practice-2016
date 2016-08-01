
window.onload = initTesting;

function initTesting(argument) {
	var mainTest = Test('http://localhost:5000/api/v1/tests/1','container');
	mainTest.init();
}