import flask
import subprocess
import flask_restful as fr
app = flask.Flask('PK')
api = fr.Api(app)
@app.route('/')
def index():
    return open('index.html').read()
class Generator(fr.Resource):
    def get(self):
        return subprocess.check_output('Caller.exe ins')
class Deleter(fr.Resource):
    def delete(self, id_):
        return subprocess.call("Caller.exe del " + id_)
api.add_resource(Generator, '/generate')
api.add_resource(Deleter, '/<string:id_>')
if __name__ == '__main__':
    app.run(debug=False)
