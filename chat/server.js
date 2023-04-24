const app = require('express')();
const server = require('http').Server(app);
const io = require('socket.io')(server);

const PORT = 3001;

io.on('connection', (socket) => {
  console.log(`Socket connected: ${socket.id}`);

  socket.on('message', (message) => {
    console.log(`Received message: ${message}`);
    io.emit('message', message);
  });
});

server.listen(PORT, () => {
  console.log(`WebSocket server listening on port ${PORT}`);
});
