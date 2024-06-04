<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ConnectFour Game AI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        header {
            background: #50b3a2;
            color: #fff;
            padding-top: 30px;
            min-height: 70px;
            border-bottom: #e8491d 3px solid;
        }
        header a {
            color: #fff;
            text-decoration: none;
            text-transform: uppercase;
            font-size: 16px;
        }
        header ul {
            padding: 0;
            list-style: none;
        }
        header li {
            display: inline;
            padding: 0 20px 0 20px;
        }
        .content {
            padding: 20px;
            background: #fff;
            margin: 20px 0;
        }
        h1, h2, h3 {
            color: #50b3a2;
        }
        pre {
            background: #f4f4f9;
            padding: 10px;
            border-left: 3px solid #e8491d;
            overflow: auto;
        }
        footer {
            background: #50b3a2;
            color: #fff;
            text-align: center;
            padding: 10px 0;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <header>
        <div class="container">
            <h1>ConnectFour Game AI</h1>
        </div>
    </header>

    <div class="container">
        <div class="content">
            <p>Welcome to the ConnectFour Game AI repository! This project features an AI agent that plays the ConnectFour game using a minimax algorithm with alpha-beta pruning. This project was made as part of the Artificial Intelligence class at the University of South Carolina under the supervision of Professor Forest Agostinelli.</p>

            <h2>Table of Contents</h2>
            <ul>
                <li><a href="#features">Features</a></li>
                <li><a href="#installation">Installation</a></li>
                <li><a href="#usage">Usage</a></li>
                <li><a href="#contributors">Contributors</a></li>
            </ul>

            <h2 id="features">Features</h2>
            <ul>
                <li>ConnectFour game environment</li>
                <li>AI agent using minimax algorithm with alpha-beta pruning</li>
                <li>Human vs AI, AI vs AI (random moves), and visualization of gameplay</li>
                <li>Heuristic evaluation for AI decision-making</li>
            </ul>

            <h2 id="installation">Installation</h2>
            <p><strong>Clone the repository</strong></p>
            <pre><code>git clone https://github.com/your-username/connectfour-game-ai.git
cd connectfour-game-ai
</code></pre>

            <h2 id="usage">Usage</h2>
            <p><strong>How To Run</strong></p>
            <pre><code>python3 run_connect_four.py</code></pre>

            <h2 id="contributors">Contributors</h2>
            <p><strong>Forest Agostinelli</strong></p>
            <p>foresta@cse.sc.edu (<a href="mailto:foresta@cse.sc.edu">research homepage</a>).</p>
        </div>
    </div>

    <footer>
        <p>ConnectFour Game AI &copy; 2023</p>
    </footer>

</body>
</html>
