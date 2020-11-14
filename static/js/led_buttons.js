var lastFile = "";

$( '.selection' ).click(function() {
  if ($(this).attr('vars') == "None")
  {
    // No special consideration
    $.get("LED", { set: $(this).attr('file')});
  }
  else
  {
    //$.get("LED", { set: "var_" + $(this).attr('file'), vars: "0,255,0"});
    var split = $(this).attr('vars').split(",");
    populateVars(split);
  }
  lastFile = $(this).attr('file');
});


// Currently only "color" supported.
function populateVars(vars)
{
  $(".vars").html("");
  for (i=0; i<vars.length; i++)
  {
    if (vars[i] == "color")
    {
      $(".vars").append("<input id='colorinput1' value='rgb(0,255,0)' data-jscolor='{previewSize:60}'><br>"); // TODO: Change to allow for more than 1 color input
      jscolor.install()
    }
  }
  $(".vars").append("<button class='send'>Send</button>")
};

$(document).on("click", ".send", function()
{
  c = document.querySelector('#colorinput1').jscolor.channels;
  $.get("LED", { set: "var_" + lastFile, vars: Math.floor(c.r) + "," + Math.floor(c.g) + "," + Math.floor(c.b) }) // TODO: Allow for more than one color
});


$(".dropbtn").click(function()
{
  if($(".dropdown-content").attr('style') == "display:block;")
  {
    $(".dropdown-content").attr('style', " ")
  }
  else
  {
    $(".dropdown-content").attr("style", "display:block;")
  }
})
