from flask import Flask, make_response, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')


@app.route('/qrcode', methods=['POST'])
def generate_qrcode():
    code = request.form['code']
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    #response = make_response(img_io.getvalue())
    img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
    #img_base64.headers['Content-Type'] = 'image/png'
    return render_template('qrcode_display.html', img_base64=img_base64)
    #return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)



# @app.route('/qrcode/<code>', methods=['POST'])
# def generate_qrcode(code):
#     qr = qrcode.QRCode(version=1, box_size=10, border=5)
#     qr.add_data(code)
#     qr.make(fit=True)
#     img = qr.make_image(fill_color="black", back_color="white")
#     img_io = BytesIO()
#     img.save(img_io, 'PNG')
#     img_io.seek(0)
#     response = make_response(img_io.getvalue())
#     response.headers['Content-Type'] = 'image/png'
#     return response