from Environment import Environment
from Path import Path
import copy

class Evaluator:
    def __init__(self) -> None:
        self.Out = {}

    def FindEndpoints(self, fileName='DoorBell.json'):
        self.env = Environment()
        self.env.readFile(fileName)
        self.actions = self.env.Model['Actions']
        initState = self.env.Model['State']
        mech = self.env.Model['Mechanisms']
        time = 0

        for seedAction in self.actions:
            if (self.checkActionCompatable(self.actions[seedAction], time, initState)):
                newPath = Path(copy.deepcopy(initState))
                newPath.addAction(self.actions[seedAction], seedAction)

                self.Out[seedAction] = []
                self.Out[seedAction].append(newPath)
                
                self.findActionOutcomes(actionPaths=self.Out[seedAction], path=self.Out[seedAction][0], startAction=self.actions[seedAction],mechanisms=mech, time=time)
        print(self.env.Model['Name'])
        for branch in self.Out:
            print("Paths resulting from action " + branch + "...")
            for path in self.Out[branch]:
                print(path.ToString())


    def findActionOutcomes(self, actionPaths, path, startAction, mechanisms, time=0):
        for effect in startAction['effects']:
            self.findMechOutcomes(actionPaths, path, mechanisms, mechanisms[effect], time)

    def findMechOutcomes(self, actionPaths, path, mechansisms, mech, time):
        for operator in mech:
            if (operator == "and"):
                #Make new state with all of them
                for element in mech[operator]:
                    if element['Type'] == 'State':
                        #Add to path
                        path.AddToState(element['Name'], element['Value'])
                    elif (element['Type'] == 'Mech'):
                        path.addMech(mechansisms[element['Name']], element['Probability'], element['Name'])
                        self.findMechOutcomes(actionPaths=actionPaths, path=path, mechansisms=mechansisms, mech=mechansisms[element['Name']], time=time)
                    elif(element['Type'] == 'Action'):
                        path.addAction(self.actions[element['Name']], element['Name'])
                        self.findActionOutcomes(actionPaths=actionPaths, path=path, mechanisms=mechansisms, mech=mechansisms[self.actions['Name']], time=time)
            elif (operator=="or"):
                # p much the same I think, but new paths for every _mech and _act
                for element in mech[operator]:
                    if element['Type'] == 'State':
                        #Add to path
                        newPath = copy.deepcopy(path)
                        newPath.AddToState(element['Name'], element['Value'], element['Probability'])
                        actionPaths.append(newPath)
                    elif (element['Type'] == 'Mech'):
                        #Add to queue to call findMechOutcomes
                        newPath = copy.deepcopy(path)
                        newPath.addMech(mechansisms[element['Name']], element['Probability'], element['Name'])
                        self.findMechOutcomes(actionPaths, newPath, mechansisms, mechansisms[element['Name']], time)
                        actionPaths.append(newPath)
                    elif(element['Type'] == 'Action'):
                        # Add to queue to call findActionOutcomes
                        newPath = copy.deepcopy(path)
                        newPath.addAction(self.actions[element['Name']], element['Action'])
                        self.findActionOutcomes(actionPaths, newPath, mechansisms, element, time)  
                    
                    actionPaths.remove(path)
                    

    def checkActionCompatable(self, action, time, state):
        compat = False
        if action['StartTime'] != -1 and ((action['StartTime'] <= time) and (time <= action['EndTime'] or action['EndTime'] == -1)):
            compat = True
            for precond in action['preconditions']:
                if (state[precond] != action['preconditions'][precond]):
                    compat = False
        return compat

x = Evaluator()
x.FindEndpoints()

def evaluate():
    #Evaluates the options available to the agent.
    
    # 1. Identify all possible options
    # 2. Finds the end-state of all possible branches
    # 3. Choose one outcome and compare to other outcomes
    # 4. If other outcome is better, switch to that outcome and compare it to all others.
    # 5. Evaluate outcomes until one is found
    # 6. Output correct output.
    pass



