function show_topics(subject) {
  // set the local storage subject field so we can restore the current search it when we come back
  localStorage.setItem("subject", subject)

  // get the list of topics for the given subject with AJAX
  $.get("/getTopics", {"subject" : subject}, function(topics_html) {
    $("#topics").html(topics_html);
  });
}

// call this when the user changes the selected subject
function select_subject() {
  var subject = $("#subjects").val();
  show_topics(subject);
  $("#subject-heading").text(subject);
}

$(function() {
  // when the page first loads, check the local storage for the last searched subject
  var subject = localStorage.getItem("subject");
  if (subject) {
    show_topics(subject);
    $("#subject-heading").text(subject);
  }
});
