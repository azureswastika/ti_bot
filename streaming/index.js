import { createServer } from 'nodejs-websocket';
// eslint-disable-next-line import/extensions
import { search, defaultError } from './src/websocket.js';

const server = createServer((conn) => {
  conn.on('text', (message) => {
    console.log(message);
    const msg = JSON.parse(message);
    switch (msg.type) {
      case 'search':
        search(conn, msg.data);
        break;
      default:
        defaultError(conn, msg);
        break;
    }
  });
  conn.on('close', (code, reason) => {
    console.log(`Disconnection code: ${code} ${reason}`);
  });
}).listen(3000);

function broadcast(message) {
  server.connections.forEach((connection) => {
    connection.sendText(message);
  });
}
