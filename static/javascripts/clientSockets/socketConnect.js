//const socket = io("localhost:5000");
const socket = io(location.host);

socket.on('connect', () => {
  console.log("[open] Connection established");
});
