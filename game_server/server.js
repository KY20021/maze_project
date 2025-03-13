const express = require('express')
const hbs = require('hbs')
const app = express()
const port = process.env.PORT || 8080;
app.set('view engine', 'hbs')
// sendFile will go here
app.use(express.static('public'))

app.get('/', (req, res) => {
    res.render('index')
})

app.listen(port);
console.log('Server started at http://localhost:' + port);