from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/bfhl', methods=['POST', 'GET'])
def bfhl():
    if request.method == 'GET':
        return jsonify({
            "operation_code": 1
        })

    if request.method == 'POST':
        data = request.json.get("data")
        file_b64 = request.json.get("file_b64")

        # Process data: Separate numbers, alphabets, and find the highest lowercase alphabet
        numbers = [x for x in data if x.isdigit()]
        alphabets = [x for x in data if x.isalpha()]
        lower_case_alphabets = [x for x in data if x.islower()]

        highest_lowercase_alphabet = max(lower_case_alphabets) if lower_case_alphabets else None

        # File handling
        file_valid = False
        file_mime_type = None
        file_size_kb = None
        if file_b64:
            try:
                file_data = base64.b64decode(file_b64)
                file_size_kb = len(file_data) / 1024
                file_valid = True
                file_mime_type = "application/octet-stream"  # You can detect actual MIME type if needed
            except Exception:
                file_valid = False

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else [],
            "file_valid": file_valid,
            "file_mime_type": file_mime_type,
            "file_size_kb": file_size_kb
        }

        return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
