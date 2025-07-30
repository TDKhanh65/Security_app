from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from commands import caesar, xor, polyalphabetic, opt, hoanvi
from commands.thongke import decrypt
import base64


app = Flask(__name__, static_folder='./frontend')
CORS(app)

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')
@app.route('/encrypt/<method>', methods=['POST'])
def encrypt(method):
    try:
        if method == 'caesar':
            text = request.json.get('text', '')
            shift = int(request.json.get('key', 0))
            result = caesar.encrypt(text, shift)

        elif method == 'xor':   
            text = request.json.get('text', '')
            key = request.json.get('key', '')
            result = xor.encrypt(text, key)

        elif method == 'base64':
            text = request.json.get('text', '')
            encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
            result = encoded

        elif method == 'hoanvi':
            chuoi = request.json.get('chuoi', '')
            thu_tu = request.json.get('thu_tu', [])
            result = hoanvi.encrypt(chuoi, thu_tu)


        elif method == 'polyalphabetic':
            text = request.json.get('text', '')
            key = request.json.get('key', '')
            result = polyalphabetic.encrypt(text, key)

        elif method == 'opt':
            text = request.json.get('text', '')
            key = request.json.get('key', '')
            result = opt.encrypt(text, key)

        else:
            return jsonify({'error': f'Phương thức không hỗ trợ: {method}'}), 400

        return jsonify({'method': method, 'encrypted': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/decrypt/<method>', methods=['POST'])
def decrypt(method):
    try:
        if method == 'caesar':
            text = request.json.get('text', '')
            shift = int(request.json.get('key', 0))
            result = caesar.decrypt(text, shift)

        elif method == 'xor':
            text = request.json.get('text', '')
            key = request.json.get('key', '')
            result = xor.decrypt(text, key)

        elif method == 'base64':
            import base64
            text = request.json.get('text', '')
            decoded = base64.b64decode(text.encode('utf-8')).decode('utf-8')
            result = decoded

        elif method == 'hoanvi':
            chuoi = request.json.get('chuoi', '')
            thu_tu = request.json.get('thu_tu', [])
            result = hoanvi.decrypt(chuoi, thu_tu)

        elif method == 'polyalphabetic':
            text = request.json.get('text', '')
            key = request.json.get('key', '')
            result = polyalphabetic.decrypt(text, key)

        elif method == 'opt':
            text = request.json.get('text', '')
            key = request.json.get('key', '')
            result = opt.decrypt(text, key)
        
        elif method == 'thongke':
            chuoi = request.json.get('chuoi', '')
            ket_qua = decrypt(chuoi)
            return jsonify({'thongke': ket_qua})

        else:
            return jsonify({'error': f'Phương thức không hỗ trợ: {method}'}), 400

        return jsonify({'method': method, 'decrypted': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5502))
    app.run(host='0.0.0.0', port=port)

