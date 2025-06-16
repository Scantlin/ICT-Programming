import pyqrcode
import png

def main():
    url = 'https://comsimwave.netlify.app/' #input what you gonna convert into qrcode
    img = pyqrcode.create(url)
    img.png('qrcode_result.png', scale=8)

if __name__ == '__main__':
    main()