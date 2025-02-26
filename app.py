from flask import Flask, render_template, request, jsonify
import csv
import os
import hashlib
from datetime import datetime

app = Flask(__name__)

# Define the path to the CSV file
csv_file_path = os.path.expanduser('OurData.csv')


# Home route for the form
@app.route('/')
def index():
    return render_template('index.html')


# Route to generate a unique number
@app.route('/generate', methods=['POST'])
def generate_unique_number():
    name = request.form.get('name', '').strip()
    names_of_children = request.form.get('names_of_children', '').strip()

    if name:
        hashed_name = hashlib.sha256(name.encode()).hexdigest()
        unique_number = hashed_name[:5]
        current_datetime = datetime.now()

        # Save data to CSV
        with open(csv_file_path, mode='a', newline='') as file:
            fieldnames = ["Name", "Names of Children", "Unique Number", "Date and Time"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # Add header if file is empty
            if os.stat(csv_file_path).st_size == 0:
                writer.writeheader()
            
            writer.writerow({
                "Name": name,
                "Names of Children": names_of_children,
                "Unique Number": unique_number,
                "Date and Time": current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            })

        return jsonify({"success": True, "unique_number": unique_number})

    return jsonify({"success": False, "error": "Name is required."})


# Route to display details based on the code
@app.route('/details', methods=['POST'])
def display_details():
    code = request.form.get('code', '').strip()

    if os.path.exists(csv_file_path):
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row.get("Unique Number", '').strip() == code:
                    return jsonify({
                        "success": True,
                        "details": {
                            "Name": row["Name"],
                            "Names of Children": row["Names of Children"],
                            "Unique Number": row["Unique Number"],
                            "Date and Time": row["Date and Time"]
                        }
                    })
    
    return jsonify({"success": False, "error": "No details found for the entered code."})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

