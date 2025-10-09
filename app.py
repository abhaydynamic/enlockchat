
# 1. Installation Prerequisite:
# Before running this, you need to install Flask:
# >> pip install Flask

from flask import Flask, render_template, send_from_directory

# Initialize the Flask application instance
app = Flask(__name__, static_folder='static', static_url_path='/static')

# --- Configuration ---
# A secret key is required for security features like session management.
# IMPORTANT: In a production environment, this should be set via environment variables.
app.config['SECRET_KEY'] = 'a_secure_and_random_secret_key'
APP_TITLE = "Enlock Chat - Secure End-to-End Encrypted Messaging"

# --- Routes ---

# Define the main route ('/')
@app.route('/')
def chat_home():
    """
    This function serves the main chat interface template.
    """
    # Flask looks for templates inside a folder named 'templates'
    return render_template('chat_fixed.html', title=APP_TITLE)

# Serve manifest.json
@app.route('/manifest.json')
def manifest():
    """Serve the PWA manifest file."""
    return send_from_directory('static', 'manifest.json', mimetype='application/json')

# Serve service worker
@app.route('/sw.js')
def service_worker():
    """Serve the service worker file."""
    return send_from_directory('static', 'sw.js', mimetype='application/javascript')

# Serve favicon
@app.route('/favicon.ico')
def favicon():
    """Serve the favicon."""
    return send_from_directory('static', 'logo.png', mimetype='image/png')

# Handle offline page
@app.route('/offline.html')
def offline():
    """Serve offline page when app is offline."""
    return render_template('chat_fixed.html', title=APP_TITLE + " - Offline")

# --- Running the App ---
if __name__ == '__main__':
    # Run the app. debug=True enables hot reloading for development.
    print(f"Starting Flask application '{APP_TITLE}'...")
    print("🚀 Enlock Chat - Secure Messaging App")
    print("📱 PWA Features: ✓ Offline Support ✓ Install Prompt ✓ Push Notifications")
    print("🔒 Security: ✓ End-to-End Encryption ✓ Firebase Auth ✓ Secure Storage")
    print("")
    print("🌐 Open your browser to http://127.0.0.1:5000/")
    print("📱 For mobile testing: http://[your-ip]:5000/")
    print("")
    # The host='0.0.0.0' makes it accessible externally, good for environments like this.
    app.run(host='0.0.0.0', port=5000, debug=True)
