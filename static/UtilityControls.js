

function addToUtilTable(literalList, e) {
    defaultLit = literalList[0];
    table = document.getElementById('Utilities');
    newRow = document.createElement('tr');
    // Create Remove Column
    newCol = document.createElement('th');
    input = document.createElement('input');
    hiddenRemove = document.createElement('input')
    hiddenRemove.setAttribute('type', 'hidden')
    hiddenRemove.setAttribute('id', 'Remove[]');
    hiddenRemove.setAttribute('name', 'UtilRemove[]');
    hiddenRemove.setAttribute('value', 'false');

    input.setAttribute('type', 'checkbox');
    input.addEventListener('click', () => {this.previousSibling.value = ((this.previousSibling.value=='true') ? 'false' : 'true');});
    //Add remove Column
    newCol.appendChild(hiddenRemove);
    newCol.appendChild(input);
    newRow.appendChild(newCol)

    // Create Name column
    newCol = document.createElement('th');
    select = document.createElement('select');
    select.setAttribute('id', 'Literal[]');
    select.setAttribute('name', 'UtilLiteral[]');
    for (i=0; i<literalList.length; i++) {
        option = document.createElement('option')
        option.setAttribute('value', literalList[i]);
        if (i==0) {
            option.setAttribute('selected', 'selected');
        }
        option.appendChild(document.createTextNode(literalList[i]));
        select.appendChild(option);
    }
    newCol.appendChild(select);
    newRow.appendChild(newCol);

    // Create State column
    newCol = document.createElement('th');
    select = document.createElement('select');
    select.setAttribute('name', 'UtilState[]');
    select.setAttribute('id', 'State[]');

    option = document.createElement('option');
    option.setAttribute('value', 'True');
    option.appendChild(document.createTextNode('True'))
    select.appendChild(option);
    option = document.createElement('option');
    option.setAttribute('value', 'False');
    option.appendChild(document.createTextNode('False'))
    select.appendChild(option);

    newCol.appendChild(select);
    newRow.appendChild(newCol);

    // Create Utility column
    newCol = document.createElement('th');
    input = document.createElement('input')
    input.setAttribute('class', 'numberInput');
    input.setAttribute('value', 0);
    input.setAttribute('id', 'Utility[]');
    input.setAttribute('name', 'UtilUtility[]');
    input.setAttribute('type', 'number');
    newCol.appendChild(input);
    newRow.appendChild(newCol)

    // Create Class column
    newCol = document.createElement('th');
    input = document.createElement('input')
    input.setAttribute('class', 'numberInput');
    input.setAttribute('value', 0);
    input.setAttribute('id', 'Class[]');
    input.setAttribute('name', 'UtilClass[]');
    input.setAttribute('type', 'number');
    newCol.appendChild(input);
    newRow.appendChild(newCol);

    table.appendChild(newRow);
    
}


function addToDeonTable(literalList, e) {
    defaultLit = literalList[0];
    table = document.getElementById('Forebidden');
    newRow = document.createElement('tr');
    // Create Remove Column
    newCol = document.createElement('th');
    input = document.createElement('input');
    
    hiddenRemove = document.createElement('input')
    hiddenRemove.setAttribute('type', 'hidden')
    hiddenRemove.setAttribute('name', 'DeonRemove[]');
    hiddenRemove.setAttribute('value', 'false');

    input.setAttribute('type', 'checkbox');
    input.addEventListener('click', () => {this.previousSibling.value = ((this.previousSibling.value=='true') ? 'false' : 'true');});
    //Add remove Column
    newCol.appendChild(hiddenRemove);
    newCol.appendChild(input);
    newRow.appendChild(newCol)

    // Create Name column
    newCol = document.createElement('th');
    select = document.createElement('select');
    select.setAttribute('name', 'DeonLiteral[]');
    for (i=0; i<literalList.length; i++) {
        option = document.createElement('option')
        option.setAttribute('value', literalList[i]);
        if (i==0) {
            option.setAttribute('selected', 'selected');
        }
        option.appendChild(document.createTextNode(literalList[i]));
        select.appendChild(option);
    }
    newCol.appendChild(select);
    newRow.appendChild(newCol);

    // Create State Column
    newCol = document.createElement('th');
    select = document.createElement('select');
    select.setAttribute('name', 'DeonState[]');

    option = document.createElement('option');
    option.setAttribute('value', 'True');
    option.appendChild(document.createTextNode('True'))
    select.appendChild(option);
    option = document.createElement('option');
    option.setAttribute('value', 'False');
    option.appendChild(document.createTextNode('False'))
    select.appendChild(option);

    newCol.appendChild(select);
    newRow.appendChild(newCol);

    table.appendChild(newRow);

}
