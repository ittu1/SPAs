const express = require('express');
const stripe = require('stripe')('sk_test_51LfVbOELdcnNg3anRKppOQxdNoYv6PiuOpiCkEk1ZIQjg51uArznRHbTDZ84y90ntY0wKVRdB1n9kMnYss5sRe8K00AVijtm7j')
const bodyParser = require('body-parser');
const exphbs = require('express-handlebars');

const app = express();

// Handlebars Middleware
app.engine('handlebars',exphbs.engine({defaultlayout:'main'}));
app.set('view engine', 'handlebars');

// Body Parser Middleware
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));

// Set Static Folder
app.use(express.static(`${__dirname}/public`));


// Index Route
app.get('/', (req, res) => {
   res.render('index'); 
});

const port = process.env.PORT || 5000;

app.listen(port, () => {
    console.log(`Server Started on port ${port}`);

});




