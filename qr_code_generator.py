import io
import qrcode

qr = qrcode.QRCode()
qr.add_data("https://www.youtube.com/watch?v=0JTqFG1ZMAw&t=3s")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())
