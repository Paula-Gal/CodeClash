const socket = io("localhost:5000");

socket.on('connect', () => {
  console.log("[open] Connection established");
});