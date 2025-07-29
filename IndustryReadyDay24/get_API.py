from flask import Flask,request,jsonify
app=Flask(__name__)
data_store=[]
@app.route('/data',methods=['POST','GET'])
def handle_data():
    if request.method == 'POST':
        res_data = request.get_json()
        data_store.append(res_data)
        return jsonify({"message": "Data received", "Data": res_data}), 201
    else:
        return jsonify(data_store),200
if __name__  == "__main__":
    app.run(debug=True)