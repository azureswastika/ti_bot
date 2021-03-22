/* eslint-disable import/named */
/* eslint-disable import/extensions */
import { getTickerPage, getTickerId } from './scrapper.js';
import { SearchConstructor, SearchErrorConstructor } from './constructors.js';

export function search(conn, data) {
  getTickerPage(data.ticker.name).then(
    (url) => getTickerId(url).then(
      (tickerId) => {
        if (url) {
          conn.sendText(
            JSON.stringify(SearchConstructor(data.chat, tickerId, data.ticker.name)),
          );
        } else {
          conn.sendText(
            JSON.stringify(SearchErrorConstructor(data.ticker.name)),
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
