// eslint-disable-next-line import/extensions
import { getTickerPage, getTickerId } from './scrapper.js';

export function search(conn, data) {
  getTickerPage(data.ticker.name).then(
    (url) => getTickerId(url).then(
      (tickerId) => {
        if (url) {
          conn.sendText(
            JSON.stringify(
              {
                type: 'search',
                data: {
                  chat: data.chat,
                  ticker: {
                    id: tickerId,
                    name: data.ticker.name,
                  },
                },
              },
            ),
          );
        } else {
          conn.sendText(
            JSON.stringify(
              {
                type: 'search-error',
                data: {
                  ticker: {
                    name: data.ticker.name,
                  },
                },
              },
            ),
          );
        }
      },
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
