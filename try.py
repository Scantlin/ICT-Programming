from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template with dark mode support
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask Web App</title>
    <style>
        :root {
            --bg-color: #f8f9fa;
            --text-color: #212529;
            --card-bg: #ffffff;
            --primary-color: #0d6efd;
            --hover-color: #0b5ed7;
        }
        
        .dark-mode {
            --bg-color: #1a1a1a;
            --text-color: #f8f9fa;
            --card-bg: #2d2d2d;
            --primary-color: #0d6efd;
            --hover-color: #0b5ed7;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 0;
            transition: all 0.3s ease;
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        .card {
            background-color: var(--card-bg);
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 2rem;
            margin-top: 2rem;
        }
        
        h1 {
            color: var(--primary-color);
            margin-bottom: 1.5rem;
        }
        
        .btn {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            transition: background-color 0.3s;
        }
        
        .btn:hover {
            background-color: var(--hover-color);
        }
        
        .mode-toggle {
            position: fixed;
            top: 20px;
            right: 20px;
        }
        
        .counter {
            font-size: 1.5rem;
            margin: 1rem 0;
        }
    </style>
</head>
<body class="{{ 'dark-mode' if dark_mode else '' }}">
    <div class="mode-toggle">
        <button class="btn" onclick="toggleDarkMode()">
            {{ '☀️ Light Mode' if dark_mode else '🌙 Dark Mode' }}
        </button>
    </div>
    
    <div class="container">
        <div class="card">
            <h1>Flask Web App</h1>
            <p>Welcome to this responsive web application with dark mode support!</p>
            
            <div class="counter">
                Button clicks: {{ click_count }}
            </div>
            
            <form method="post">
                <button type="submit" name="action" value="increment" class="btn">
                    Click Me
                </button>
            </form>
        </div>
    </div>
    
    <script>
        function toggleDarkMode() {
            fetch('/toggle_dark_mode', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
            }).then(() => window.location.reload());
        }
    </script>
</body>
</html>
"""

# App state
app_state = {
    'click_count': 0,
    'dark_mode': False
}

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST' and request.form.get('action') == 'increment':
        app_state['click_count'] += 1
    
    return render_template_string(
        HTML_TEMPLATE,
        click_count=app_state['click_count'],
        dark_mode=app_state['dark_mode']
    )

@app.route('/toggle_dark_mode', methods=['POST'])
def toggle_dark_mode():
    app_state['dark_mode'] = not app_state['dark_mode']
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)