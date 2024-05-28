const express = require('express');
const app = express();
const port = 3000;

// In-memory data
let products = [
    { id: 1, name: 'Bread', quantity: 100, price: 1.50 },
    { id: 2, name: 'Apples', quantity: 75, price: 0.80 },
    { id: 3, name: 'Bananas', quantity: 50, price: 3.50 },
    { id: 4, name: 'Milk', quantity: 80, price: 1.80 }
];

app.get('/', (req, res) => {
    res.send('Welcome to SupermarketApp!');
});

// Middleware to parse JSON bodies
app.use(express.json());

// Read ALL products
app.get('/inventory', (req, res) => {
    res.json(products);
});

// Create a new product
app.post('/inventory', (req, res) => {
    const newProduct = req.body;
    newProduct.id = products.length ? products[products.length - 1].id + 1 : 1; // Generate new id
    products.push(newProduct);
    res.status(201).json(newProduct);
});

// Read ONE product
app.get('/inventory/:id', (req, res) => {
    const productId = parseInt(req.params.id, 10);
    const product = products.find(p => p.id === productId);
    if (product) {
        res.json(product);
    } else {
        res.status(404).send('Product not found');
    }
});

// Update a product
app.put('/inventory/:id', (req, res) => {
    const productId = parseInt(req.params.id, 10);
    const productIndex = products.findIndex(p => p.id === productId);
    if (productIndex !== -1) {
        products[productIndex] = { ...products[productIndex], ...req.body };
        res.json(products[productIndex]);
    } else {
        res.status(404).send('Product not found');
    }
});

// Delete a product
app.delete('/inventory/:id', (req, res) => {
    const productId = parseInt(req.params.id, 10);
    const productIndex = products.findIndex(p => p.id === productId);
    if (productIndex !== -1) {
        const deletedProduct = products.splice(productIndex, 1);
        res.json(deletedProduct[0]);
    } else {
        res.status(404).send('Product not found');
    }
});

// Start the server
app.listen(port, () => {
    console.log(`SupermarketApp listening at http://localhost:${port}`);
});
