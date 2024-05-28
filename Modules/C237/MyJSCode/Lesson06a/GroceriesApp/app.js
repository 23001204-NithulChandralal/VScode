const express = require('express');
const app = express();

// Setting EJS as the view engine
app.set('view engine', 'ejs');

// Sample data
const snacksList = ['Chips', 'Cookies', 'Candy', 'Popcorn'];
const dairyList = ['Milk', 'Cheese', 'Yogurt', 'Butter'];

app.get('/groceries', (req, res) => {
    res.render('groceries', { snacksList, dairyList });
});

// Start the server
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
    console. log(`Server running at http://localhost:${PORT}/groceries`);
});