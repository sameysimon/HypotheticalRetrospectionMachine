from flask import Flask, render_template, request, url_for, flash, redirect
from flask_assets import Bundle, Environment

from Laws.ExpectedUtility import ExpectedUtility
from Laws.DeontologicalBanList import DeontologicalBanList
from ArgumentGraph import ArgumentGraph
from Scenario import Scenario
from ScenarioFactory import ScenarioFactory

app = Flask(__name__)
assets = Environment(app)
js = Bundle('cytoscape.min.js', 'displayGraph.js')
assets.register('js_all', js)

envList = ['CoinApple', 'library', 'trolley', 'PoeticCoinApple']


@app.route('/', methods=('GET', 'POST'))
def hello():
    if request.method != "POST":
        return getDefaultEnv('CoinApple')

    env = request.form.get('envName')
    if request.form.get('changeEnv') == 'True':
        return getDefaultEnv(env)
    
    s = Scenario()
    if env=='CoinApple':
        print('load coin')
        ScenarioFactory.createCoinActions(s)
    elif env=='library':
        print('load library')
        ScenarioFactory.createLibaryActions(s)
    elif env=='PoeticCoinApple':
        print('load poetic coin apple')
        ScenarioFactory.createKentCoinActions(s)
    else:
        print('load trolley')
        ScenarioFactory.createTrolleyActions(s)

    conUtil = request.form.get('conUtil') == 'on'
    conDeon = request.form.get('conDeon') == 'on'
    forebidden = {}
    if conUtil:
        print('Utilitarianism')
        createUtilities(request, s)
        s.addConsideration(ExpectedUtility())
        
    if conDeon:
        print("Deontology")
        forebidden = getForebidden(request)
        s.addConsideration(DeontologicalBanList(forebidden=forebidden))

    g = ArgumentGraph(s)
    print("Edge List")
    print(g.getEdgeList())
    return render_template('index.html',
    envName=env,
    conUtil=conUtil,
    conDeon=conDeon,
    nodeList=g.getNodeList(),
    edgeList=g.getEdgeList(),
    argList=s.getArgumentList(),
    forebidList=forebidden,
    envList=envList,
    utilClasses=s.Utilities,
    literalList=list(s.InitState.keys())
    )

def getDefaultEnv(env):
    print('Get Default Env')
    s = Scenario()
    if env == 'CoinApple':
        print('load coin')
        ScenarioFactory.createKentCoinActions(s)
    elif env=='library': 
        print('load library')
        ScenarioFactory.createLibaryActions(s)
    elif env=='PoeticCoinApple':
        print('load poetic coin apple')
        ScenarioFactory.createKentCoinActions(s)
    else:
        ScenarioFactory.createTrolleyActions(s)
    s.addConsideration(ExpectedUtility())
    g = ArgumentGraph(s)

    return render_template('index.html',
        envName=env,
        conUtil=True,
        conDeon=False,
        nodeList=g.getNodeList(),
        edgeList=g.getEdgeList(), 
        argList=s.getArgumentList(),
        forebidList={},
        envList=envList,
        utilClasses=s.Utilities,
        literalList=list(s.InitState.keys()))


def createUtilities(request, scenario):
    scenario.Utilities = []
    removes =  request.form.getlist('UtilRemove[]')
    literals = request.form.getlist('UtilLiteral[]')
    states = request.form.getlist('UtilState[]')
    utilities = request.form.getlist('UtilUtility[]')
    classes = request.form.getlist('UtilClass[]')
    
    for i in range(len(literals)):
        if removes[i]=='false':
            state = states[i]=='True'
            scenario.addUtility(int(classes[i]), literals[i], state, int(utilities[i]))
    
    
def getForebidden(request):
    forebidden = {}
    removes = request.form.getlist('DeonRemove[]')
    literals = request.form.getlist('DeonLiteral[]')
    states = request.form.getlist('DeonState[]')
    for i in range(0, len(literals)):
        if removes[i] == 'false':
            state = states[i]=='True'
            forebidden[literals[i]] = state
    print(forebidden)
    return forebidden