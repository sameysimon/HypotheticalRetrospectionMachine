from OutcomeFinder import OutcomeFinder
from ArgumentGraph import ArgumentGraph
from Laws.ExpectedUtility import ExpectedUtility

of = OutcomeFinder()
actionBranches =  of.FindOutcomes('Scenarios/TrolleySituation.json')


oa = ArgumentGraph(actionBranches)
oa.ToString(actionBranches)
oa.findMostAccepted(actionBranches)

