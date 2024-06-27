const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')
const fs = require('fs')
const csv = require('csv-parser')
const path = require('path')


const app = express();
app.use(bodyParser.json());
app.use(cors());

app.get('/data',(req,res)=>{
    const filepath = path.join(__dirname,'data.csv');
    const results = [];

    fs.createReadStream(filepath)
        .pipe(csv())
        .on('data', (data) => results.push(data))
        .on('end', () => {
            res.json(results);
        });
});
 

const port = 5000;
app.listen(port,()=>{
    console.log("Server running on LocalHost 5000")
});
