import { createServer } from 'nodejs-websocket';
// eslint-disable-next-line import/extensions
import { getTickerPage, getTickerId } from './src/scrapper.js';

const server = createServer((conn) => {
  conn.on('text', (message) => {
    const msg = JSON.parse(message);
    switch (msg.command) {
      case 'search':
        getTickerPage(msg.data).then((url) => getTickerId(url).then((tickerId) => conn.sendText(JSON.stringify({ command: 'search', data: { ticker: msg.data, id: tickerId } }))));
        break;
      default:
        conn.sendText();
        break;
    }
  });
  conn.on('close', (code, reason) => {
    console.log(code, reason);
  });
}).listen(3000);

function broadcast(message) {
  server.connections.forEach((connection) => {
    connection.sendText(message);
  });
}
