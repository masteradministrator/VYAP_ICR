var express = require('express');
var app = express();

app.use(express.static(__dirname + '/templates'));

app.listen(9000);

