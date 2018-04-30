var express = require('express');
var router = express.Router();
var request = require('request');

/* GET home page. */
router.get('/', function(req, res, next) {
  var IN_KEY = process.env.LI_CLIENT_ID;
  res.render('login', { title: 'Express test', IN_KEY: IN_KEY });
});

router.get('/role', function(req, res, next) {
  res.render('whatjob.html')
});

router.get('/level', function(req, res, next) {
  res.render('selectlevel.html')
});

router.get('/skills', function(req, res, next) {
  res.render('skills.html')
});

router.post('/level', function(req, res, next) {
  res.render('skills.html')
});

function callbackFunction(){
  console.log('callback')
};

module.exports = router;
