var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
  var IN_KEY = process.env.LI_CLIENT_ID;
  res.render('login.html');//, { title: 'Express test', IN_KEY: IN_KEY });
});

function callbackFunction(){
  console.log('callback')
};

module.exports = router;
