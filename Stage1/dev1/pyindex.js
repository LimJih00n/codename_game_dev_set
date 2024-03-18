
function sendCompletionMessage() {
    window.parent.postMessage({ type: "gameCompleted", message: "PyScript game completed successfully." }, "*");
}
function sendXY(X,Y){
    window.parent.postMessage({type:"XY_state",message:{x: X,y: Y}},"*");
}