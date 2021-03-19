import axios from 'axios';
import { load } from 'cheerio';

const instrumentIdReg = /\\"instrument_id\\":\\"\d*\\"/gmius;
const digitsReg = /[0-9]+/gmius;
const baseUrl = 'https://ru.investing.com';

function parseHref(response) {
  const $ = load(response.data);
  return $($('.js-inner-all-results-quote-item.row')[0]).attr('href');
}

export function getTickerPage(ticker) {
  return axios.get(`${baseUrl}/search`, {
    params: {
      q: ticker,
    },
  }).then((response) => parseHref(response));
}

function parseScript(response) {
  const $ = load(response.data);
  const json = String($('#__NEXT_DATA__').contents());
  return digitsReg.exec(instrumentIdReg.exec(json)[0])[0];
}

export function getTickerId(url) {
  return axios.get(`${baseUrl}${url}`).then((response) => parseScript(response));
}
