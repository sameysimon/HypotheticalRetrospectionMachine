from OutcomeFinder import OutcomeFinder
from ArgumentGraph import ArgumentGraph


from Laws.ExpectedUtility import ExpectedUtility
from Laws.DeontologicalBanList import DeontologicalBanList

from Scenario import Scenario
"""
s = Scenario('My New Scenario')
s.addAction('Jump', {'onGround': True}, ['InAir'], 0, -1)
s.addAction('Not Jump', {'onGround': True}, [], 0, -1)
m = s.addMech('InAir')
s.addToMech(m, 'and', 'onGround', 1, 'State', False)
s.addToMech(m, 'and', 'Gravity', 1, 'Mech', False)
m = s.addMech('Gravity')
s.addToMech(m, 'or', 'fly', 0.1, 'State', True)
s.addToMech(m, 'or', 'falling', 0.9, 'State', True)

s.addState('onGround', True)
s.addState('fly', False)
s.addState('falling', False)

s.addValue(1,'falling',1)
s.addValue(0,'fly', 1)

s.writeToJSON('newFile.json')
"""


jsonFile = 'Scenarios/TrolleySituation.json'
s = Scenario()
s.readFromJSON(jsonFile)
s.addConsideration(ExpectedUtility())

dbl = DeontologicalBanList()
dbl.addForebiddenLiteral('bystander', False)
s.addConsideration(dbl)


of = OutcomeFinder()
actionBranches =  of.FindOutcomes(s)
of.ToString()


oa = ArgumentGraph(actionBranches, s.Considerations)
oa.ToString(actionBranches)
oa.findMostAccepted(actionBranches)