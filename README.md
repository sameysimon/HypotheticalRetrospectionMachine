# HypotheticalRetrospectionMachine
A Machine for evaluating moral decisions using Hypothetial Retrospection. Built as a web app with a python backend and a react front-end.
Allows ethical decision scenarios to be formally described. Each initial action's alternate branches of future development are inferred. Hypothetical retrospection from the end point of each alternate branch is modelled as an argumentation procedure. An argument representing each action's possible branches are made in the form of 'Given circumstances s0, the root action a1 was correct, resulting in state...' Each action's arguments are compared. One branch attacks another if: the attacker has a higher utility state, and the defender doesn't have a higher expectation of a greater state; the attacker doesn't break a moral rule that the defender does, adn the defender doesn't have a higher expectation of not breaking that rule. These rules need to be investigated to ensure they don't produce adverse effects.

### TO-DO List
* Add morality rules for comprison
* Performance optimisation
* User Interface (possibly a graph to show arguments)

