<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚀 My Modern App</title>
    <style>
        /* Global */
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
        }
        h1 {
            text-align: center;
            font-size: 42px;
            margin-top: 30px;
        }

        /* Container */
        .container {
            display: flex;
            min-height: 100vh;
        }

        /* Sidebar */
        .sidebar {
            width: 220px;
            background: linear-gradient(180deg, #141e30, #243b55);
            padding: 20px;
            box-sizing: border-box;
        }
        .sidebar h2 {
            color: white;
            text-align: center;
            margin-bottom: 30px;
        }
        .sidebar button {
            width: 100%;
            padding: 12px;
            margin-bottom: 10px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            background: linear-gradient(45deg, #ff512f, #dd2476);
            color: white;
            transition: 0.3s;
        }
        .sidebar button:hover {
            transform: scale(1.05);
            background: linear-gradient(45deg, #36d1dc, #5b86e5);
        }

        /* Main content */
        .main {
            flex: 1;
            padding: 30px;
            box-sizing: border-box;
        }

        /* Card style */
        .card {
            background: rgba(255,255,255,0.12);
            backdrop-filter: blur(12px);
            padding: 25px;
            border-radius: 18px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.3);
            margin-bottom: 20px;
        }

        input, textarea, select {
            width: 100%;
            padding: 10px;
            margin-top: 8px;
            margin-bottom: 15px;
            border-radius: 10px;
            border: none;
            box-sizing: border-box;
            font-size: 16px;
        }

        .result {
            margin-top: 15px;
            padding: 12px;
            border-radius: 10px;
            background-color: rgba(0,255,150,0.2);
            font-weight: bold;
        }

        .error {
            margin-top: 15px;
            padding: 12px;
            border-radius: 10px;
            background-color: rgba(255,0,0,0.2);
            font-weight: bold;
        }

    </style>
</head>
<body>

    <h1>🚀 Welcome to My Modern App</h1>
    <div class="container">
        <!-- Sidebar -->
        <div class="sidebar">
            <h2>📌 Navigation</h2>
            <button onclick="showPage('home')">Home</button>
            <button onclick="showPage('about')">About</button>
            <button onclick="showPage('contact')">Contact</button>
        </div>

        <!-- Main content -->
        <div class="main">
            <!-- Home Page -->
            <div id="home" class="card page">
                <h2>🧮 Interactive Calculator</h2>
                <label>Enter first number:</label>
                <input type="number" id="num1" value="0">
                
                <label>Enter second number:</label>
                <input type="number" id="num2" value="0">
                
                <label>Select operation:</label>
                <select id="operation">
                    <option>Add</option>
                    <option>Subtract</option>
                    <option>Multiply</option>
                    <option>Divide</option>
                </select>
                
                <button onclick="calculate()">Calculate</button>
                <div id="calcResult"></div>
            </div>

            <!-- About Page -->
            <div id="about" class="card page" style="display:none;">
                <h2>📖 About This App</h2>
                <p>This is a modern web application built using <strong>HTML, CSS & JavaScript</strong>.</p>
                <ul>
                    <li>✔ Beautiful modern UI</li>
                    <li>✔ Interactive calculator</li>
                    <li>✔ Multi-page navigation</li>
                    <li>✔ Fully client-side & responsive</li>
                </ul>
            </div>

            <!-- Contact Page -->
            <div id="contact" class="card page" style="display:none;">
                <h2>📩 Contact Me</h2>
                <label>Your Name:</label>
                <input type="text" id="name">
                <label>Your Email:</label>
                <input type="email" id="email">
                <label>Your Message:</label>
                <textarea id="message" rows="4"></textarea>
                <button onclick="sendMessage()">Send Message</button>
                <div id="contactResult"></div>
            </div>
        </div>
    </div>

    <script>
        function showPage(pageId) {
            const pages = document.querySelectorAll('.page');
            pages.forEach(p => p.style.display = 'none');
            document.getElementById(pageId).style.display = 'block';
        }

        function calculate() {
            const num1 = parseFloat(document.getElementById('num1').value);
            const num2 = parseFloat(document.getElementById('num2').value);
            const op = document.getElementById('operation').value;
            const resultDiv = document.getElementById('calcResult');

            let result;
            if (op === 'Add') result = num1 + num2;
            else if (op === 'Subtract') result = num1 - num2;
            else if (op === 'Multiply') result = num1 * num2;
            else if (op === 'Divide') {
                if (num2 === 0) {
                    resultDiv.innerHTML = '<div class="error">Cannot divide by zero!</div>';
                    return;
                }
                result = num1 / num2;
            }

            resultDiv.innerHTML = `<div class="result">Result: ${result}</div>`;
        }

        function sendMessage() {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();
            const contactDiv = document.getElementById('contactResult');

            if (name && email && message) {
                contactDiv.innerHTML = '<div class="result">Message sent successfully! 🚀</div>';
            } else {
                contactDiv.innerHTML = '<div class="error">Please fill all fields.</div>';
            }
        }
    </script>
</body>
</html>
