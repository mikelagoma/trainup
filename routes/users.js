var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get('/create', function(req, res) {//, next) {
  console.log(req.query.firstName);
  var db = req.db;
  var collection = db.get('visitors');
  console.log('insertig into ' + collection.toString());
  collection.insert({
      "firstName" : req.query.firstName,
      "lastName" : req.query.lastName,
      "pictureUrl" : req.query.pictureUrl
  }, function (err, doc) {
      if (err) {
          // If it failed, return error
          res.send("There was a problem adding the information to the database.");
      }
      else {
          // And forward to success page
          // res.redirect("chat/" + 1);
          res.send('User added to db');
      }
  });
  // res.send('asdsad')
});

router.get('/list', function(req, res) {
  var db = req.db;
  var collection = db.get('visitors');
  // var users = collection.find().toArray();
  // if (users.length > 0) { printjson (users[0]); }
  // res.render(users)
  var users = Array()
  collection.find({},{},function(e,docs){
  //     return users;
  // });
      users.push(docs);
      res.send(docs)
      // res.render('visitorList', {
      //   'visitors' : docs
      // });
  });
  console.log(JSON.stringify(users));
  // res.render(users);
});

module.exports = router;
