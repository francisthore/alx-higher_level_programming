// Fetches from an api and says hello val from api
$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  $.get(url, function (data) {
    $('DIV#hello').html('<p>' + data.hello + '</p>');
  });
});
