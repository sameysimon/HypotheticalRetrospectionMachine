from Path import Path
import io
import copy
import json

class OutcomeFinder:
    # Returns a dictionary of each action to an array of its possible end states.
    def FindOutcomes(self, fileName='Scenarios/DoorBell.json'):
        with io.open(fileName) as data_file:
            self.Model = json.load(data_file)

        self.actions = self.Model['Actions']
        initState = self.Model['State']
        self.mechanisms = self.Model['Mechanisms']
        self.Utilities = self.Model['Values']

        time = 0

        # Maps action names to possible end states
        self.Out = []

        # Iterates through each action
        for count, seedAction in enumerate(self.actions):
            if (self.checkActionCompatable(self.actions[seedAction], time, initState)):
                # Creates a path object to represent each end state. Starts with one, but more can be added for each branch.
                newPath = Path(copy.deepcopy(initState), self.Utilities)
                newPath.addAction(self.actions[seedAction], seedAction)
                # Add initial path containing initial action to dictionary for paths from this action.
                self.Out.append([])
                self.Out[count].append(newPath)
                # Adds to list of paths, all possible end points from action.
                self._findActionOutcomes(self.Out[count], self.Out[count][0], self.actions[seedAction], time=time)
                

        # Temporary, prints all end points for each action.
        for branch in self.Out:
            print("Paths resulting from action " + branch[0].lastAction + "...")
            for path in branch:
                print(path.ToString())
        return self.Out


    # For each effect from the action, adds to actionPath, all outcome paths from choosing action
    def _findActionOutcomes(self, actionPaths, path, action, time=0):
        
        for effect in action['effects']:
            self._findMechOutcomes(actionPaths, path, self.mechanisms[effect], time)

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
                        path.AddToState(element['Name'], element['Value'], Utilities=self.Utilities)
                    elif (element['Type'] == 'Mech'):
                        path.addMech(self.mechanisms[element['Name']], element['Probability'], element['Name'])
                        self._findMechOutcomes(actionPath=actionPath, path=path, mech=self.mechanisms[element['Name']], time=time)
                    elif(element['Type'] == 'Action'):
                        path.addAction(self.actions[element['Name']], element['Name'])
                        self._findActionOutcomes(actionPaths=actionPath, path=path, mech=self.mechanisms[self.actions['Name']], time=time)
            elif (operator=="or"):
                # For every element of the rule, add its outcomes to a new path.
                # 'Or' means branching at this stage. So create new paths from this one.
                for element in mech[operator]:
                    if element['Type'] == 'State':
                        #Add to path
                        newPath = copy.deepcopy(path)
                        newPath.AddToState(element['Name'], element['Value'], element['Probability'], self.Utilities)
                        actionPath.append(newPath)
                    elif (element['Type'] == 'Mech'):
                        newPath = copy.deepcopy(path)
                        newPath.addMech(self.mechanisms[element['Name']], element['Probability'], element['Name'])
                        actionPath.append(newPath)
                        self._findMechOutcomes(actionPath, newPath, self.mechanisms[element['Name']], time)      
                    elif(element['Type'] == 'Action'):
                        # Add to queue to call findActionOutcomes
                        newPath = copy.deepcopy(path)
                        newPath.addAction(self.actions[element['Name']], element['Action'])
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


