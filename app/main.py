import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<id>')
def hello_world(id):
    try:
        import contentTest1
        return contentTest1.main(id)

    except Exception as e:
        pass
    return 'OH NO!\n'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
