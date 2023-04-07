from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    input_str = request.json['input_str']
    output_list = input_str.split()
    return jsonify({'output_list': output_list})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
