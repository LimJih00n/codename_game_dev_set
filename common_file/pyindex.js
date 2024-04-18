
function sendCompletionMessage() {
    window.parent.postMessage({ type: "gameCompleted", message: "PyScript game completed successfully." }, "*");
}
function sendXY(X,Y){
    window.parent.postMessage({type:"XY_state",message:{x: X,y: Y}},"*");
}

function sendPyErrorMessage(e){
    window.parent.postMessage({ type: "pythonErrorCompleted", message: e }, "*");
}
function checkAndSendMessage() {          
    const outputDiv = document.querySelector('py-script div:nth-child(2)');
    console.log(outputDiv);
    if (outputDiv && outputDiv.textContent.includes('Error')) {
        
        window.parent.postMessage({ type: "specificMessageFound", message: outputDiv.textContent }, "*");
    }
}
  
