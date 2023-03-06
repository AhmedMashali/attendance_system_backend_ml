var express = require('express'); 
var bodyParser = require('body-parser');
// request-promise is used to send http request
// Note that this package is deprecated!!
var request = require('request-promise'); 
var fs = require('fs')


var app = express(); 
  
app.use(bodyParser.json()); 
app.use(bodyParser.urlencoded({ extended: false }));


// Endpoint for sending data to the model and get data from it
app.get('/postdatatoFlask', async (req, res) => { 
    
    // data to be sent to the model => (token image of the class and the images of indviduals)
    var data = fs.readFileSync('img/test_class_6.jpeg', 'base64');
    
    // multiple data can be sent like this:
    // var data = { // this variable contains the data you want to send 
    //     data1: "foo",
    //     data2: "bar"
    // }

    var options = { 
        method: 'POST', 
        uri: 'http://127.0.0.1:5000/postdata', 
        body: data, 
        json: true // Automatically stringifies the body to JSON 
    }; 
     
    var returndata;
    // Send request with the data to the model
    var sendrequest = await request(options) 
    .then((parsedBody) => {
        // parsedBody contains the data sent back from the Flask server 
        // console.log(parsedBody); 
        returndata = parsedBody.newdata.slice(2, -1); 
        // Use this data
        fs.writeFileSync("img/ahmed_mohamed.jpg", parsedBody.newdata.slice(2, -1) , 'base64');
    })
    .catch((err) => { 
        console.log(err);
    }); 
    res.send(returndata);

}); 
  
app.listen(3000); 