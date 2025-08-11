from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)

@app.route('/api/datetime', methods=['GET'])
def get_datetime():
    typ = request.args.get('type', 'both').lower()
    tz_name = request.args.get('tz', '').strip()

    try:
        if tz_name:
            tz = pytz.timezone(tz_name)
            now = datetime.now(tz)
        else:
            now = datetime.now()
    except Exception:
        now = datetime.utcnow()

    if typ == 'date':
        value = now.strftime('%Y-%m-%d')
    elif typ == 'time':
        value = now.strftime('%H:%M:%S')
    else:
        value = now.strftime('%Y-%m-%d %H:%M:%S')

    return jsonify({'value': value})

if __name__ == '__main__':
    app.run(debug=True)