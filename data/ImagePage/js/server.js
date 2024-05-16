const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = 3000;
const IMAGE_DIR = path.join(__dirname, 'data');

app.use(express.static('public'));

app.get('/images', (req, res) => {
    fs.readdir(IMAGE_DIR, (err, files) => {
        if (err) {
            console.log(err);
            return res.status(500).send('Server error');
        }
        const images = files.filter(file => /\.(jpg|jpeg|png|gif)$/i.test(file)).map(file => `/data/${file}`);
        res.json(images);
    });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});

