from flask import Flask, render_template, request, url_for, flash, redirect
from flask_assets import Bundle, Environment

from Laws.ExpectUtility import ExpectedUtility
from ArgumentGraph import ArgumentGraph
from Scenario import Scenario
from ScenarioFactory import ScenarioFactory

app = Flask(__name__)
assets = Environment(app)
js = Bundle('cytoscape.min.js', 'displayGraph.js')
assets.register('js_all', js)

envList = ['coinFlip', 'library', 'trolley']


@app.route('/', methods=('GET', 'POST'))
def hello():
    if request.method != "POST":
        return getDefaultEnv('coinFlip')

    env = request.form.get('envName')
    print('env is ' + str(env))
    if request.form.get('changeEnv') == 'True':
        return getDefaultEnv(env)
    
    s = Scenario()
    if env=='coinFlip':
        ScenarioFactory.createCoinActions(s)
    elif env=='library':
        ScenarioFactory.createLibaryActions(s)
    else:
        ScenarioFactory.createTrolleyActions(s)

    conUtil = request.form.get('conUtil') == 'on'
    if conUtil:
        createUtilities(request, s)
        s.addConsideration(ExpectedUtility())
    if request.form.get('conDeon') == 'on':
        # Process literals
        print("Do deon")
    
    g = ArgumentGraph(s)
    return render_template('index.html',
    envName=env,
    conUtil=conUtil,
    nodeList=g.getNodeList(),
    edgeList=g.getEdgeList(),
    argList=s.getArgumentList(),
    envList=envList,
    utilClasses=s.Utilities,
    literalList=list(s.InitState.keys())
    )

def getDefaultEnv(env):
    s = Scenario()
    if env == 'coinFlip':
        ScenarioFactory.createCoinActions(s)
    elif env=='library': 
        ScenarioFactory.createLibaryActions(s)
    else:
        ScenarioFactory.createTrolleyActions(s)
    s.addConsideration(ExpectedUtility())
    g = ArgumentGraph(s)

    return render_template('index.html',
        envName=env,
        conUtil=True,
        nodeList=g.getNodeList(),
        edgeList=g.getEdgeList(), 
        argList=s.getArgumentList(),
        envList=envList,
        utilClasses=s.Utilities,
        literalList=list(s.InitState.keys()))


def createUtilities(request, scenario):
    scenario.Utilities = []
    removes =  request.form.getlist('Remove[]')
    literals = request.form.getlist('Literal[]')
    states = request.form.getlist('State[]')
    utilities = request.form.getlist('Utility[]')
    classes = request.form.getlist('Class[]')
    print('heyas')
    for i in range(len(literals)):
        print('hello')
        print(removes[i])
        if removes[i]=='false':
            state = states[i]=='True'
            scenario.addUtility(int(classes[i]), literals[i], state, int(utilities[i]))
    
    

