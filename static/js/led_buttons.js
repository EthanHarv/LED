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
    if (vars[i] == "color") // TODO: Add more available variables
    {
      $(".vars").append("<input class='varINPUT varcolor' id='colorinput" + i + "' value='rgb(0,255,0)' data-jscolor='{previewSize:60}'><br>");
      jscolor.install()
    }
  }
  $(".vars").append("<button class='send'>Send</button>")
};

$(document).on("click", ".send", function()
{
  fVars = "";
  $(".varINPUT").each(function(i, obj)
  {
    if ($(obj).hasClass('varcolor')){
      c = document.querySelector("#" + $(obj).attr('id')).jscolor.channels;
      fVars += Math.floor(c.r) + "," + Math.floor(c.g) + "," + Math.floor(c.b);
    };
    fVars += ","
  });
  $.get("LED", { set: "var_" + lastFile, vars: fVars });
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
