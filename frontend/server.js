var express = require('express');
var app = express();

app.use(express.static(__dirname + '/templates'));

app.listen((process.env.PORT || 9000));

