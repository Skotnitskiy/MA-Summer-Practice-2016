
window.onload = initTesting;

function initTesting(argument) {
	var mainTest = Test('/api/v1/tests/id_test/questions','container');
	mainTest.init();
}