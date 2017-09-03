function setFilter(columnID, checked) {
  var checkmark = '\u2713' // the unicode code for the checkmark
  var column = $("#table").DataTable().column(columnID);
  if (checked) {
    column.search(checkmark).draw();
  }
  else {
    column.search("").draw();
  }
}

$(function() {
  $("#table").DataTable();
  var checkmark = '\u2713' // the unicode code for the checkmark

  $("#lecturenotes").click(function(evt) {
    setFilter(4, evt.target.checked)
  });

  $("#lecturevideos").click(function(evt) {
    setFilter(5, evt.target.checked);
  });

  $("#assignments").click(function(evt) {
    setFilter(6, evt.target.checked);
  })

  $("#book").click(function(evt) {
    setFilter(7, evt.target.checked)
  })


});
