$(document).ready(function () {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    data.results.forEach(element => {
        $('<li>').text(element.title).appendTo('UL#list_movies');
    });
  });
});
