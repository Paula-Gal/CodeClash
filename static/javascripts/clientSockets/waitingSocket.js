function findGame(){
    socket.emit("find_game");
}

socket.on("start_game", () => {
    console.log("Game started!");
    location.replace('/room')
});