#!/usr/bin/node
function count() {
	const num_of_args = process.argv.length;
	if (num_of_args <= 2) {
		console.log('No argument');
	} else if (num_of_args === 3) {
		console.log('Argument found');
	} else {
		console.log('Arguments found');
	}
}
count();
