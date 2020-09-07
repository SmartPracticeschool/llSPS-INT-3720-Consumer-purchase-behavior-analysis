from flask import Flask , render_template , request
import pickle
app = Flask(__name__)
model = pickle.load(open('project.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template('index1.html')
@app.route('/login', methods = ["POST"])
def login():
    pid = request.form["pid"]
    st = request.form["st"]
    age = request.form["age"]
    oc = request.form["oc"]
    pca = request.form["pca"]
    pcb = request.form["pcb"]
    pcc = request.form["pcc"]
    G = request.form["G"]
    if(G == "Male"):
        s2 = 0
    if(G == "Female"):
        s2 = 1
    cc = request.form["cc"]
    if(cc == "1"):
        c2,c3 = 0,0
    if(cc == "2"):
        c2,c3 = 1,0
    if(cc == "3"):
        c2,c3 = 0,1
    ms = request.form["ms"]
    if(ms == "married"):
        m2 = 0
    if(ms == "unmarried/divorced"):
        m2 = 1
    total = [[int(pid),s2,int(age),int(oc),c2,c3,int(float(st)),m2,int(float(pca)),int(float(pcb)),int(float(pcc))]]
    p = model.predict(total)
    p = p[0][0]
    c = "THE PURCHASE IS = "+str(p)
    return render_template('index1.html',label = c)
if __name__=='__main__':
    app.run(debug = True)