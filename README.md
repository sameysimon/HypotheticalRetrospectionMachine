# The Hypothetical Retrospection Machine
For evaluating moral decisions with uncertain outcomes using the hypothetical retrospection procedure from Sven Hannson's book, The Ethics of Risk: Ethical analysis in an uncertain world.
The implementation can either used in the Python console or as a Flask webapp.

### Instructions to Run in Command Line
To use in the console, ensure you have installed Python 3. The code has been tested with Python 3.8.9
Run.py shows a basic configuration of the machine with a Coin-Apple Scenario being evaluated with consideration of Expected-Utility Utilitarianism. A Deontological principle to forbid apples can be added by uncommenting the line above.
The Coin-Apple scenario can be changed from the appropriate function in ScenarioBuilder.py

### Instructions to Run from Flask Web-App
To get a user-interface showing the retrospection visually, you will need to locally host the Flask Web App.
Install Python 3, I developed and tested with Python 3.8.9, and install Flask with the included pip package manager. I developed and tested with Flask 2.2.2
Next you will need to set two environment variables. First, FLASK_APP is set to the string of the directory of WebApp.py, removing the .py; FLASK_ENV is set to the string 'development'. In later versions of Flask, you may need to use FLASK_DEBUG instead. Then you can run flask and the app will be locally hosted, the address should appear in the console.
If you execute the runApp.sh script, it should set the environment variables and host the webapp for you.

![](https://github.com/sameysimon/HypotheticalRetrospectionMachine/blob/main/ReadMeSrc/RunWebApp.gif)


Once you open the web page, go to the side panel to change between the prebuilt Coin-Apple, Library, and Trolley scenarios. 
Select from drop down and click Change Environment to switch. 
You can change utilities, utility classes and add deontological forbidden states below. Click Load Environment to apply changes to the graph.
You can click on individual nodes to reveal the hypothetical retrospective argument they represent.
You can click on edges to reveal the ethical theory used in the attack.


### Libraries
I used Flask to build the web app: https://github.com/pallets/flask
I used the Javascript library, Cytoscape.js, to generate the graphs in the web app: https://github.com/cytoscape/cytoscape.js







