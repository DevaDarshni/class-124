from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[
    {
        'id':1,
        'title':u'favorite food',
        'description':u'pani puri,pav bhaji,pancake',
        'done':False
    },
    {
        'id':2,
        'title':u'favorite colour',
        'description':u'pink,blue,yellow',
        'done':False
    },
    {
        'id':3,
        'title':u'favorite colour',
        'description':u'pink,blue,yellow',
        'done':False
    },
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task={
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    } 
    tasks. append(task) 
    return jsonify({
        "status":"sucess",
        "message":"tasks add sucessful"
    }) 

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })    
if(__name__ == "__main__"):
    app.run(debug=True)