function findGame(){
    console.log("ma apelez");
    socket.emit("find_game");
}

socket.on("start_game", () => {
    console.log("Game started!");
    location.replace('/room')
});