  socket.on("msg", function(data){
    console.log("mesaj: " + data)
  });

function goToWaitingRoom(){
    window.location = "/waiting-room";
}

  //socket on sa asculte dupa start game
  //login screen emite cancel_game