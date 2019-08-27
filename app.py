from flask import Flask
from flask import request
from apis.file_download import download_file_threaded

app = Flask(__name__)

@app.route('/download', methods = ['GET'])
def download():
    url_of_file = request.args.get('url')
    
    print (url_of_file)
    url_data = {}
    url_data['url'] = url_of_file
    size = download_file_threaded.apply_async(kwargs=url_data)
    print('size')
    return str(size)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)