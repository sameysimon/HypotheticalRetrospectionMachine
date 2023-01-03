from Path import Path
from Action import Action
from Laws.ExpectedUtility import ExpectedUtility
import io
import copy
import json

class OutcomeFinder:
    # Returns a dictionary of each action to an array of its possible end states.
    def FindOutcomes(self, scenario):
        self.scenario = scenario
        self.pathID = 0
        self.ActionID = 0
        time = 0

        # List of action objects containing correct paths.
        self.Actions = []

        # Iterates through each action
        for count, seedAction in enumerate(scenario.Actions):
            if (self.checkActionCompatable(self.scenario.Actions[seedAction], time, self.scenario.InitState)):
                # Create Action object for new choice being investigated.
                self.Actions.append(Action(count, seedAction))
                # Create a path object to represent each end state. Starts with one, but more can be added for each branch.
                newPath = Path(self.pathID, copy.deepcopy(self.scenario.InitState), self.scenario.Utilities, self.Actions[count])
                self.pathID += 1

                newPath.addAction(self.scenario.Actions[seedAction], seedAction)
                # Add initial path containing initial action to action object.
                self.Actions[count].addPath(newPath)
                self.Actions[count].rootAction = self.Actions[count]
                # Adds to list of paths, all possible end points from action.
                self._findActionOutcomes(actionPaths=self.Actions[count].PathList, path=self.Actions[count].PathList[0], action=self.scenario.Actions[seedAction], time=time)

        for actionBranch in self.Actions:
            if len(actionBranch.PathList) > 1:
                actionBranch.PathList.sort()
                actionBranch.PathList.reverse()
            for path in actionBranch.PathList:
                path.bestExpectation = actionBranch.PathList[0]
  
        return self.Actions

    def ToString(self):
        # Temporary, prints all end points for each action.
        for actionBranch in self.Actions:
            print("Paths resulting from action " + actionBranch.Name + "...")
            for path in actionBranch.PathList:
                print(path.ToString())


    # For each effect from the action, adds to actionPath, all outcome paths from choosing action
    def _findActionOutcomes(self, actionPaths, path, action, time=0):
        for effect in action['effects']:
            self._findMechOutcomes(actionPaths, path, self.scenario.Mechanisms[effect], time)

    # For each possible outcome of the mechanism, adds to actionPath, all outcome paths resulting from mechanism.
    def _findMechOutcomes(self, actionPath, path, mech, time):
        # For every mechanism rule
        for operator in mech:
            # Determine the nature of the rule (and/or)
            if (operator == "and"):
                # For every element of the rule, add its outcomes to the path.
                # 'And' means no branching at this stage, so add all state changes to current path.
                for element in mech[operator]:
                    if element['Type'] == 'State':
                        #Add to path
                        path.AddToState(element['Name'], element['Value'], Utilities=self.scenario.Utilities)
                    elif (element['Type'] == 'Mech'):
                        path.addMech(self.scenario.Mechanisms[element['Name']], element['Probability'], element['Name'])
                        self._findMechOutcomes(actionPath=actionPath, path=path, mech=self.scenario.Mechanisms[element['Name']], time=time)
                    elif(element['Type'] == 'Action'):
                        path.addAction(self.scenario.Actions[element['Name']], element['Name'])
                        self._findActionOutcomes(actionPaths=actionPath, path=path, mech=self.scenario.Mechanisms[self.scenario.Actions['Name']], time=time)
            elif (operator=="or"):
                # For every element of the rule, add its outcomes to a new path.
                # 'Or' means branching at this stage. So create new paths from this one.
                for element in mech[operator]:
                    if element['Type'] == 'State':
                        #Add to path
                        
                        newPath = copy.deepcopy(path)
                        
                        newPath.ID = copy.deepcopy(self.pathID)
                        newPath = Path(copy.deepcopy(self.pathID), copy.deepcopy(path.State), {}, path.rootAction)
                        self.pathID += 1
                        newPath.Actions = copy.deepcopy(path.Actions)
                        newPath.Mech = copy.deepcopy(path.Mech)
                        newPath.Log = copy.deepcopy(path.Log)
                        newPath.Sequence = copy.deepcopy(path.Sequence)
                        newPath.lastAction = copy.deepcopy(path.lastAction)
                        newPath.bestUtilityClass = copy.deepcopy(path.bestUtilityClass)
                        newPath.Utility = copy.deepcopy(path.Utility)

                        newPath.AddToState(element['Name'], element['Value'], element['Probability'], self.scenario.Utilities)
                        
                        actionPath.append(newPath)
                    elif (element['Type'] == 'Mech'):
                        newPath = copy.deepcopy(path)
                        newPath.addMech(self.scenario.Mechanisms[element['Name']], element['Probability'], element['Name'])
                        actionPath.append(newPath)
                        self._findMechOutcomes(actionPath, newPath, self.scenario.Mechanisms[element['Name']], time)      
                    elif(element['Type'] == 'Action'):
                        # Add to queue to call findActionOutcomes
                        newPath = copy.deepcopy(path)
                        newPath.addAction(self.scenario.Actions[element['Name']], element['Action'])
                        self._findActionOutcomes(actionPath, newPath, element, time)
                    # Removes initial half finished path.
                    if (path in actionPath):
                        actionPath.remove(path)

    # For a given action, checks if the agent can fire it according to the state and the action's preconditions, plus the current time step.
    def checkActionCompatable(self, action, time, state):
        compat = False
        if action['StartTime'] != -1 and ((action['StartTime'] <= time) and (time <= action['EndTime'] or action['EndTime'] == -1)):
            compat = True
            for precond in action['preconditions']:
                if (state[precond] != action['preconditions'][precond]):
                    compat = False
        return compat


