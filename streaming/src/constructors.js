export function SearchConstructor(chat, id, name) {
  return {
    type: 'search',
    data: {
      chat,
      ticker: {
        id,
        name,
      },
    },
  };
}

export function SearchErrorConstructor(name) {
  return {
    type: 'search-error',
    data: {
      ticker: {
        name,
      },
  }
}