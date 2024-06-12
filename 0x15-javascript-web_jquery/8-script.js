// fetches film titles from api
$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  $.get(url, function (data) {
    const results = data.results;
    for (const film of results) {
      $('UL#list_movies').append('<li>' + film.title + '</li>');
    }
  });
});
