from Laws.ExpectedUtility import ExpectedUtility
from Laws.DeontologicalBanList import DeontologicalBanList
from ArgumentGraph import ArgumentGraph
from Scenario import Scenario
from ScenarioFactory import ScenarioFactory

def main():
    s = Scenario()
    ScenarioFactory.createKentCoinActions(s)
    s.addConsideration(ExpectedUtility())
    #s.addConsideration(DeontologicalBanList(forebidden={"getApple": True}))
    g = ArgumentGraph(s)
    g.getNodeList()
    g.getEdgeList()
    print(g.ToString())
    print(g.getMostAccepted())

if __name__ == "__main__":
    main()
