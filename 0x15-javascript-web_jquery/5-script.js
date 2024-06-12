// appends to a list
$(document).ready(function () {
  let i = 0;
  $('DIV#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</item>');
    i = i + 1;
  });
});
