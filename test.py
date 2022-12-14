from OutcomeFinder import OutcomeFinder
from ArgumentGraphBuilder import ArgumentGraphBuilder

of = OutcomeFinder()
actionBranches =  of.FindOutcomes('Scenarios/TrolleySituation.json')

oa = ArgumentGraphBuilder(actionBranches)

oa.ToString()

