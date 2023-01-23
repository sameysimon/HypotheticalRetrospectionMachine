from Laws.ExpectUtility import ExpectedUtility
from ArgumentGraph import ArgumentGraph
from Scenario import Scenario
from ScenarioFactory import ScenarioFactory

s = Scenario()
ScenarioFactory.createLibaryActions(s)
s.addConsideration(ExpectedUtility())
g = ArgumentGraph(s)
g.getNodeList()
g.getEdgeList()
g.ToString()