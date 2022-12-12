from OutcomeFinder import OutcomeFinder
from OutcomeArguer import OutcomeArguer

of = OutcomeFinder()
actionBranches =  of.FindOutcomes('Scenarios/CoinFlip.json')

oa = OutcomeArguer(actionBranches)


