//import cytoscape from "./cytoscape.esm.min.js";
Arguments = {}
ArgumentDisplay = null
function setData(actions, edges, _arguments) {
  Arguments = _arguments;
  ArgumentDisplay = document.getElementById('desc');
  showGraph(actions, edges);

}

function showArgument(evt) {
  console.log('Show Argument');
  var node = evt.target;
  ArgumentDisplay.innerHTML = Arguments[node.id()];
}

function showGraph(actions, edges) {
  // Create elements list from g
  elements = {nodes: [], edges: []}
  console.log(edges)
  for (let action in actions) {
    elements['nodes'].push({data: {id: action}})
    for (let i=0;i < actions[action].length; i++) {
      elements['nodes'].push({ 
        data: {id: actions[action][i], parent: action}
      });
    } 
  }
  
  for (let i=0; i<edges.length; i++) {
    console.log(edges[i])
    elements['edges'].push({data: {id: edges[i][0].toString() + ',' + edges[i][1].toString(), source: edges[i][0], target: edges[i][1]}});
  }
  

  var cy = cytoscape({
    container: document.getElementById('cy'),
    elements: elements,
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
          'width': 3,
          'line-color': '#ccc',
          'curve-style': 'straight',
          'width': 10,
          'target-arrow-color': '#c55',
          'target-arrow-shape': 'triangle'
        }
      },
      {
        selector: ':parent',
        css: {
          'text-valign': 'top',
          'text-halign': 'center',
          'background-color': '#666'
        }
      }
    ]
  }
  );

  cy.on('tap', 'node', showArgument)

}