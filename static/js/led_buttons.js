$( '.selection' ).click(function() {
  if ($(this).attr('vars') == "None")
  {
    // No special consideration
    $.get("LED", { set: $(this).attr('file')});
  }
  else
  {
    $.get("LED", { set: "var_" + $(this).attr('file'), vars: "0,255,0"})
  }
});
