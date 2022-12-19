from OutcomeFinder import OutcomeFinder
from ArgumentGraphBuilder import ArgumentGraphBuilder
from Laws.ExpectedUtility import ExpectedUtility

of = OutcomeFinder()
actionBranches =  of.FindOutcomes('Scenarios/CoinFlip.json')

oa = ArgumentGraphBuilder(actionBranches)


oa.ToString()

