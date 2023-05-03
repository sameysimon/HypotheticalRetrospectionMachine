//import cytoscape from "./cytoscape.esm.min.js";
Arguments = {}
Edges = []
ArgumentDisplay = null
function setData(actions, edges, _arguments) {
  Arguments = _arguments;
  Edges = edges
  ArgumentDisplay = document.getElementById('desc');
  showGraph(actions, edges);

}

function showArgument(evt) {
  var node = evt.target;
  ArgumentDisplay.innerHTML = Arguments[node.id()];
}
function showAttack(evt) {
  var node = evt.target;
  ArgumentDisplay.innerHTML = Edges[node.id()][2] + ' attack.'

}

function showGraph(actions, edges) {
  // Create elements list from g
  elements = {nodes: [], edges: []}
  actionCount = -1

  for (let action in actions) {
    actionCount = actionCount + 1
    elements['nodes'].push({data: {id: action, actionIndex: actionCount}})

    for (let i=0;i < actions[action].length; i++) {
      elements['nodes'].push({ 
        data: {id: actions[action][i], parent: action}
      });
    } 
  }
  
  for (let i=0; i<edges.length; i++) {
    elements['edges'].push({data: {id: i, source: edges[i][0], target: edges[i][1]}});
  }
  console.log(elements)
  

  var cy = cytoscape({
    container: document.getElementById('cy'),
    layout: {name: 'grid'},
    elements: {
      nodes: elements['nodes'],
      edges: elements['edges']
    },
    style: [ // the stylesheet for the graph
      {
        selector: 'node',
        style: {
          'background-color': '#ccc',
          'label': 'data(id)'
        }
      },
      {
        selector: 'edge',
        style: {
          'width': 2,
          'line-color': '#000',
          'curve-style': 'bezier',
          'target-arrow-color': 'black',
          'target-arrow-shape': 'triangle'
        }
      },
      {
        selector: ':parent',
        css: {
          'text-valign': 'top',
          'text-halign': 'center',
          'background-color': 'mapData(actionIndex, 0,' + actionCount + ', #6495ED, #de4331)',
          'shape': 'round-rectangle'
        }
      }
    ]
  }
  );
  cy.fit()
  cy.on('tap', 'node', showArgument)
  cy.on('tap', 'edge', showAttack)

}