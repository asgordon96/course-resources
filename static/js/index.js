$(function() {
  function show_topics(subject) {
    $("#topichidden").val(subject); // set the hidden field so we can restore it when we come back
    // get the list of topics for the given subject with AJAX
    $.get("/getTopics", {"subject" : subject}, function(topics_html) {
      $("#topics").html(topics_html);
    });
  }

  // when the page first loads, check the hidden field for the topic
  var subject = $("#subjecthidden").val();
  if (subject) {
    show_topics(subject)
  }

  $("#subjects").editableSelect();

  $("#search").click(function(evt) {
    var subject = $("#subjects").val();
    $("#subjecthidden").val(subject)
    show_topics(subject);
  });

});
