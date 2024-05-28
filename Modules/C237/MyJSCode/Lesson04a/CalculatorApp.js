const http = require('http');

// Calculator functions
function calculate(operation, operand1, operand2 = 0) {
    let result = 0;
    switch (operation) {
        case "+":
            result = operand1 + operand2;
            break;
        case "-":
            result = operand1 - operand2;
            break;
        case "*":
            result = operand1 * operand2;
            break;
        case "/":
            result = operand1 / operand2;
            break;
        case "exp":
            result = Math.pow(operand1, operand2);
            break;
        case "sqrt":
            result = Math.sqrt(operand1);
            break;
        default:
            result = "Invalid operation";
    }
    return result;
}

function displayResult(operation, operand1, operand2 = 0) {
    let result = calculate(operation, operand1, operand2);
    let resultString = operand1 + " " + operation + (operand2 != 0 ? " " + operand2 : "") + " = " + result;
    return resultString;
}

// Creating HTTP server
const server = http.createServer((req, res) => {
    const url = req.url;
    if (url === '/') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Welcome to the homepage!');
    } else if (url === '/contact') {
        res.writeHead(200, { 'Content-Type': 'text/plain' });
        res.end('Contact Page');
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('404 Not Found');
    }
});

// Starting the server
const port = 3000;
server.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});

// Testing calculator functions
console.log(displayResult("+", 5, 3));
console.log(displayResult("-", 5, 3));
console.log(displayResult("*", 5, 3));
console.log(displayResult("/", 5, 3));
console.log(displayResult("exp", 5, 3));
console.log(displayResult("sqrt", 16));
