
window.onload = initTesting;

function initTesting(argument) {
	var mainTest = Test('https://psyc-tests.herokuapp.com/api/v1/tests/4','container');
	mainTest.init();
}