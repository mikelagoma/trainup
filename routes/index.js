var express = require('express');
var router = express.Router();
var request = require('request');
var roleToSkills = require('../public/data/skills.json')
var skillToResources = require('../public/data/resources.json')

/* GET home page. */
router.get('/', function(req, res, next) {
  var IN_KEY = process.env.LI_CLIENT_ID;
  res.render('login', { title: 'Express test', IN_KEY: IN_KEY });
});

router.get('/role', function(req, res, next) {
  res.render('whatjob.html');
});

router.get('/level', function(req, res, next) {
  res.render('selectlevel.html');
});

router.post('/level', function(req, res, next) {
  res.render('skills.html', { skillToResources : skillToResources,
                              roleToSkills : roleToSkills });
});

router.get('/skills', function(req, res, next) {
  console.log(roleToSkills.fields[0].positions)
  res.render('skills.html', { skillToResources : skillToResources,
                              roleToSkills : roleToSkills });
});

router.post('/skills', function(req, res, next) {
  res.render('resources.html');
});

router.get('/mvp', function(req, res, next) {
  res.render('mvp.html');
});

function callbackFunction(){
  console.log('callback');
};

module.exports = router;
