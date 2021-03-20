// eslint-disable-next-line import/extensions
import { getTickerPage, getTickerId } from './scrapper.js';

export function search(conn, msg) {
  getTickerPage(msg.data).then(
    (url) => getTickerId(url).then(
      (tickerId) => conn.sendText(
        JSON.stringify(
          {
            type: 'search',
            data: {
              ticker: msg.data,
              id: tickerId,
            },
          },
        ),
      ),
    ),
  );
}

export function defaultError(conn, msg) {
  conn.sendText(
    JSON.stringify(
      {
        type: 'error',
        data: `No such type ${msg.type}`,
      },
    ),
  );
}
