from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define the health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health endpoint to return JSON status."""
    return jsonify({"status": "healthy"}), 200

# Run the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 8080 )
