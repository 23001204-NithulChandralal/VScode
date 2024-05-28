// Import the Express. js framework
const express = require('express');
// Create an instance of the Express application. This app variable will be used to define routes and configure the server
const app = express();
// Specify the port for the server to listen on
const port = 3000;
 
// Middleware for JSON parsing
app.use(express.json());
 
// In-memory data for students
let students = [
    { id: 1, name: 'Peter Tan', age: 20 },
    { id: 2, name: 'Mary Lim', age: 22 },
    { id: 3, name: 'John Ho', age: 21 }
];
 
// Routes for CRUD operations
app.get('/students', function(req, res) { //get http method
// Respond with the list of students in JSON format
    res.json(students);
});
 
// Start the server and listen on the specified port
app.listen(port, () => {
// Log a message when the server is successfully started
    console.log(`Server is running at http://localhost:${port}/students`);
});