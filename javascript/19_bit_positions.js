var fs = require('fs');

function bit(x, p) {
	return (x & 1 << p - 1) >> p - 1;
}

fs.readFileSync(process.argv[2]).toString().split('\n').forEach(function (line) {
	if (line == '') {
		return;
	}

	var tokens = line.split(',');
	var x  = parseInt(tokens[0]),
		p0 = parseInt(tokens[1]),
		p1 = parseInt(tokens[2]);

	console.log(bit(x, p0) == bit(x, p1));
});

