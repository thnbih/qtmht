from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)  # Cho phép tất cả các nguồn truy cập

# Cấu hình kết nối MySQL
db = mysql.connector.connect(
    host="192.168.96.1",
    port="3308",
    user="user",
    password="123456789",
    database="diem_thi"
)

@app.route('/tra-cuu', methods=['GET'])
def tra_cuu():
    ma_sinh_vien = request.args.get('ma_sinh_vien')
    cursor = db.cursor()
    cursor.execute("SELECT diem FROM diem_thi WHERE ma_sinh_vien = %s", (ma_sinh_vien,))
    result = cursor.fetchone()
    if result:
        return jsonify({"ma_sinh_vien": ma_sinh_vien, "diem": result[0]})
    else:
        return jsonify({"error": "Không tìm thấy sinh viên"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
