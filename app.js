// app.js

const express = require('express');
const loggerMiddleware = require('./loggerMiddleware');

const app = express();

// Use middleware
app.use(loggerMiddleware);

// Define routes
app.get('/', (req, res) => {
    res.send('Hello, World!');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
