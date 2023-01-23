import copy

from Scenario import Scenario
from Action import Action
from Path import Path
from Laws.ExpectUtility import ExpectedUtility
from ArgumentGraph import ArgumentGraph
from Edge import Edge

def createLibaryActions(s):
    actions = []
    a = Action(0,"RecommendClassBook", "StudentSeesBook", s)

    # Student uses book and passes:
    p = Path(0,copy.deepcopy(s.InitState), a)
    p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
    p.addMech(s.Mechanisms['BookTest'], 0.6, 'BookTest')
    p.AddToState('StudentDataCompromised', True, 1, s.Utilities)
    p.addMech(s.Mechanisms['GoodTest'], 1, 'GoodTest')
    p.AddToState('Passed', True, 0.7, s.Utilities)
    p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
    p.AddToState('OthersFindTest', False, 0.05, s.Utilities)
    a.addPath(p)
    

    p = Path(1,copy.deepcopy(s.InitState), a)
    p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
    p.addMech(s.Mechanisms['BookTest'], 0.6, 'BookTest')
    p.AddToState('StudentDataCompromised', True, 1, s.Utilities)
    p.addMech(s.Mechanisms['GoodTest'], 1, 'GoodTest')
    p.AddToState('Passed', True, 0.7, s.Utilities)
    p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
    p.AddToState('Secret', True, 0.95, s.Utilities)
    a.addPath(p)

    # Student uses book and fails:
    p = Path(2,copy.deepcopy(s.InitState), a)
    p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
    p.addMech(s.Mechanisms['BookTest'], 0.6, 'BookTest')
    p.AddToState('StudentDataCompromised', True, 1, s.Utilities)
    p.addMech(s.Mechanisms['GoodTest'], 1, 'GoodTest')
    p.AddToState('Failed', True, 0.3, s.Utilities)
    p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
    p.AddToState('OthersFindTest', True, 0.05, s.Utilities)
    a.addPath(p)
    p = Path(3,copy.deepcopy(s.InitState), a)
    p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
    p.addMech(s.Mechanisms['BookTest'], 0.6, 'BookTest')
    p.addMech(s.Mechanisms['GoodTest'], 1, 'GoodTest')
    p.AddToState('Failed', True, 0.3, s.Utilities)
    p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
    p.AddToState('Secret', True, 0.95, s.Utilities)
    a.addPath(p)

    # Student doesn't use book and passes
    p = Path(4,copy.deepcopy(s.InitState), a)
    p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
    p.addMech(s.Mechanisms['BlindTest'], 0.4, 'BlindTest')
    p.AddToState('StudentDataCompromised', True, 1, s.Utilities)
    p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
    p.AddToState('Passed', True, 0.3, s.Utilities)
    p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
    p.AddToState('OthersFindTest', True, 0.05, s.Utilities)
    a.addPath(p)
    p = Path(5,copy.deepcopy(s.InitState), a)
    p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
    p.addMech(s.Mechanisms['BlindTest'], 0.4, 'BlindTest')
    p.AddToState('StudentDataCompromised', True, 1, s.Utilities)
    p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
    p.AddToState('Passed', True, 0.3, s.Utilities)
    p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
    p.AddToState('Secret', True, 0.95, s.Utilities)
    a.addPath(p)

    # Student doesn't use book and fails
    p = Path(6,copy.deepcopy(s.InitState), a)
    p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
    p.addMech(s.Mechanisms['BlindTest'], 0.4, 'BlindTest')
    p.AddToState('StudentDataCompromised', True, 1, s.Utilities)
    p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
    p.AddToState('Failed', True, 0.7, s.Utilities)
    p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
    p.AddToState('OthersFindTest', True, 0.05, s.Utilities)
    a.addPath(p)
    p = Path(7,copy.deepcopy(s.InitState), a)
    p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
    p.addMech(s.Mechanisms['BlindTest'], 0.4, 'BlindTest')
    p.AddToState('StudentDataCompromised', True, 1, s.Utilities)
    p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
    p.AddToState('Failed', True, 0.7, s.Utilities)
    p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
    p.AddToState('Secret', True, 0.95, s.Utilities)
    a.addPath(p)
    s.Branches.append(a)

    a = Action(1,"DontRecommend", "BadTest", s)
    p = Path(8,copy.deepcopy(s.InitState), a)
    p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
    p.AddToState('Passed', True, 0.3, s.Utilities)
    a.addPath(p)

    p = Path(9,copy.deepcopy(s.InitState), a)
    p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
    p.AddToState('Failed', True, 0.7, s.Utilities)
    a.addPath(p)
    


    s.Branches.append(a)
    return actions
def createCoinActions(s):
    a = Action(0,"Apple", "ChooseApple", s)

    # Student uses book and passes:
    p = Path(0,copy.deepcopy(s.InitState), a)
    p.AddToState('madeChoice', True, 1, s.Utilities)
    p.AddToState('getApple', True, 1, s.Utilities)
    a.addPath(p)
    s.Branches.append(a)

    a = Action(1, "CoinFlip", "ChooseCoin", s)
    
    p = Path(1, copy.deepcopy(s.InitState), a)
    p.AddToState('madeChoice', True, 1, s.Utilities)
    p.addMech(s.Mechanisms['flipCoin'], 1, 'flipCoin')
    p.AddToState('getHawaii', True, 0.5, s.Utilities)
    a.addPath(p)
    p = Path(2, copy.deepcopy(s.InitState), a)
    p.AddToState('madeChoice', True, 1, s.Utilities)
    p.addMech(s.Mechanisms['flipCoin'], 1, 'flipCoin')
    p.AddToState('getNothing', True, 0.5, s.Utilities)
    a.addPath(p)
    s.Branches.append(a)
    return actions

jsonFile = 'Scenarios/Library.json'
s = Scenario()
s.readFromJSON('Scenarios/CoinFlip')
s.addConsideration(ExpectedUtility())
#s.addConsideration(Deontology(['StudentDataCompromised']))


createLibaryActions(s)
#createCoinActions(s)

graph = ArgumentGraph(s)



