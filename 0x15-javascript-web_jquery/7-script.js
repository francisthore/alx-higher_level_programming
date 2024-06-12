// Fetches character name from an api
$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(url, function (data) {
    $('DIV#character').text(data.name);
  });
});
