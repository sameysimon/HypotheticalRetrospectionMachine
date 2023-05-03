from Scenario import Scenario
from Action import Action
from Path import Path
import copy

class ScenarioFactory:

    def createCoinActions(s):
        s.readFromJSON('./Scenarios/CoinFlip.json')
        a = Action(0,"Apple", "ChooseApple", s)

        # Student uses book and passes:
        p = Path("a1b1",copy.deepcopy(s.InitState), a)
        p.AddToState('madeChoice', True, 1)
        p.AddToState('getApple', True, 1)
        a.addPath(p)
        s.Branches.append(a)

        a = Action(1, "CoinFlip", "ChooseCoin", s)
        
        p = Path("a2b1", copy.deepcopy(s.InitState), a)
        p.AddToState('madeChoice', True, 1)
        p.addMech(s.Mechanisms['flipCoin'], 1, 'flipCoin')
        p.AddToState('getHawaii', True, 0.5)
        a.addPath(p)
        p = Path("a2b2", copy.deepcopy(s.InitState), a)
        p.AddToState('madeChoice', True, 1)
        p.addMech(s.Mechanisms['flipCoin'], 1, 'flipCoin')
        p.AddToState('getNothing', True, 0.5)
        a.addPath(p)
        s.Branches.append(a)

    def createKentCoinActions(s):
        s.readFromJSON('./Scenarios/CoinFlip.json')
        a = Action(0,"Apple", "ChooseApple", s)

        # Student uses book and passes:
        p = Path("a1b1",copy.deepcopy(s.InitState), a)
        p.AddToState('madeChoice', True, "Certain")
        p.AddToState('getApple', True, "Certain")
        a.addPath(p)
        s.Branches.append(a)

        a = Action(1, "CoinFlip", "ChooseCoin", s)
        
        p = Path("a2b1", copy.deepcopy(s.InitState), a)
        p.AddToState('madeChoice', True, "Certain")
        p.addMech(s.Mechanisms['flipCoin'], "Certain", 'flipCoin')
        p.AddToState('getHawaii', True, "Chances about even")
        a.addPath(p)
        p = Path("a2b2", copy.deepcopy(s.InitState), a)
        p.AddToState('madeChoice', True, "Certain")
        p.addMech(s.Mechanisms['flipCoin'], "Certain", 'flipCoin')
        p.AddToState('getNothing', True, "Chances about even")
        a.addPath(p)
        s.Branches.append(a)



    def createLibraryActions(s):
        s.readFromJSON('Scenarios/Library.json')
        a = Action(0,"Recommend Book", "StudentSeesBook", s)

        # Student uses book and passes:
        p = Path("b_1",copy.deepcopy(s.InitState), a)
        p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
        p.addMech(s.Mechanisms['BookTest'], 0.6, 'BookTest')
        p.AddToState('StudentDataCompromised', True, 1)
        p.addMech(s.Mechanisms['GoodTest'], 1, 'GoodTest')
        p.AddToState('Passed', True, 0.7)
        p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
        p.AddToState('OthersFindTest', True, 0.05)
        a.addPath(p)
        

        p = Path("b_2",copy.deepcopy(s.InitState), a)
        p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
        p.addMech(s.Mechanisms['BookTest'], 0.6, 'BookTest')
        p.AddToState('StudentDataCompromised', True, 1)
        p.addMech(s.Mechanisms['GoodTest'], 1, 'GoodTest')
        p.AddToState('Passed', True, 0.7)
        p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
        p.AddToState('Secret', True, 0.95)
        a.addPath(p)

        # Student uses book and fails:
        p = Path("b_3",copy.deepcopy(s.InitState), a)
        p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
        p.addMech(s.Mechanisms['BookTest'], 0.6, 'BookTest')
        p.AddToState('StudentDataCompromised', True, 1)
        p.addMech(s.Mechanisms['GoodTest'], 1, 'GoodTest')
        p.AddToState('Failed', True, 0.3)
        p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
        p.AddToState('OthersFindTest', True, 0.05)
        a.addPath(p)

        p = Path("b_4",copy.deepcopy(s.InitState), a)
        p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
        p.addMech(s.Mechanisms['BookTest'], 0.6, 'BookTest')
        p.addMech(s.Mechanisms['GoodTest'], 1, 'GoodTest')
        p.AddToState('Failed', True, 0.3)
        p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
        p.AddToState('Secret', True, 0.95)
        a.addPath(p)

        # Student doesn't use book and passes
        p = Path("b_5",copy.deepcopy(s.InitState), a)
        p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
        p.addMech(s.Mechanisms['BlindTest'], 0.4, 'BlindTest')
        p.AddToState('StudentDataCompromised', True, 1)
        p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
        p.AddToState('Passed', True, 0.3)
        p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
        p.AddToState('OthersFindTest', True, 0.05)
        a.addPath(p)
        p = Path("b_6",copy.deepcopy(s.InitState), a)
        p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
        p.addMech(s.Mechanisms['BlindTest'], 0.4, 'BlindTest')
        p.AddToState('StudentDataCompromised', True, 1)
        p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
        p.AddToState('Passed', True, 0.3)
        p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
        p.AddToState('Secret', True, 0.95)
        a.addPath(p)

        # Student doesn't use book and fails
        p = Path("b_7",copy.deepcopy(s.InitState), a)
        p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
        p.addMech(s.Mechanisms['BlindTest'], 0.4, 'BlindTest')
        p.AddToState('StudentDataCompromised', True, 1)
        p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
        p.AddToState('Failed', True, 0.7)
        p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
        p.AddToState('OthersFindTest', True, 0.05)
        a.addPath(p)
        p = Path("b_8",copy.deepcopy(s.InitState), a)
        p.addMech(s.Mechanisms['StudentSeesBook'], 1, 'StudentSeesBook')
        p.addMech(s.Mechanisms['BlindTest'], 0.4, 'BlindTest')
        p.AddToState('StudentDataCompromised', True, 1)
        p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
        p.AddToState('Failed', True, 0.7)
        p.addMech(s.Mechanisms['DatabaseHack'], 1, 'DatabaseHack')
        p.AddToState('Secret', True, 0.95)
        a.addPath(p)

        s.Branches.append(a)

        a = Action(1,"Ignore book", "BadTest", s)
        p = Path("b_9",copy.deepcopy(s.InitState), a)
        p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
        p.AddToState('Passed', True, 0.3)
        a.addPath(p)

        p = Path("b_10",copy.deepcopy(s.InitState), a)
        p.addMech(s.Mechanisms['BadTest'], 1, 'BadTest')
        p.AddToState('Failed', True, 0.7)
        a.addPath(p)

        s.Branches.append(a)

    def createTrolleyActions(s):
        s.readFromJSON('./Scenarios/TrolleySituation.json')
        a = Action(0, "PullLever", "SecondTrackPath", s)
        
        p = Path("a1b1", copy.deepcopy(s.InitState), a)
        p.AddToState('A_Alive', False, 1)
        p.AddToState('bystander', False, 1)
        a.addPath(p)
        s.Branches.append(a)

        a = Action(1, "Whistle", "FirstTrackPath", s)
        p = Path("a2b2", copy.deepcopy(s.InitState), a)
        p.AddToState('B_Alive', False, 1)
        p.AddToState('C_Alive', False, 1)
        p.AddToState('D_Alive', False, 1)
        p.AddToState('E_Alive', False, 1)
        p.AddToState('F_Alive', False, 1)
        a.addPath(p)
        s.Branches.append(a)
