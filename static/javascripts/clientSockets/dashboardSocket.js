  const socket = io("localhost:5000");

  socket.on('connect', () => {
    console.log("[open] Connection established");
    socket.emit("find_game");
  });
  

  socket.on("msg", function(data){
    console.log("mesaj: " + data)
  });

  //socket on sa asculte dupa start game
  //login screen emite cancel_game