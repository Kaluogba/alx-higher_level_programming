const characterUri = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
const $characterDiv = $('div#character');

$.ajax({
  url: characterUri,
  dataType: 'json'
}).done((data) => {
  $characterDiv.text(data.name);
});
