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
    if (vars[i] == "color") // TODO: Add "note"/identifier/comment feature. I.e. "First Color:"
    {
      $(".vars").append("<input class='varINPUT varcolor' id='colorinput" + i + "' value='rgb(0,255,0)' data-jscolor='{previewSize:60}'><br>");
      jscolor.install()
    }
    if (vars[i].startsWith("int"))
    {
      var split = vars[i].split("_");
      if (split.length == 1) // Defaults to "Unbounded Text Input"
      {
        $(".vars").append("<input onkeypress='return isNumberKey(event)' class='varINPUT varint' id='intinput" + i + "'><br>"); // Important that we just use isNumberKey for unbounded
      }
      if (split[1] == "bound" ) // Attr low, high
      {
        $(".vars").append("<input onkeypress='return valBoundInput(event)' class='varINPUT varint' id='intinput" + i + "' low=" + split[2] + " high=" + split[3] + "><br>");
      };
      // TODO: Add slider
    }
  }
  $(".vars").append("<button class='send'>Send</button>")
};

$(document).on("click", ".send", function()
{
  fVars = "";
  send = true;
  $(".varINPUT").each(function(i, obj)
  {
    if ($(obj).hasClass('varcolor')){
      c = document.querySelector("#" + $(obj).attr('id')).jscolor.channels;
      fVars += Math.floor(c.r) + "," + Math.floor(c.g) + "," + Math.floor(c.b);
    };
    if ($(obj).hasClass('varint')){
      if ($(obj)[0].value == "") { send = false; }
      fVars += $(obj)[0].value;
    };
    fVars += ","
  });
  if (send) { $.get("LED", { set: "var_" + lastFile, vars: fVars }); };
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

function valBoundInput(evt)
{
    //console.log(evt.target.value + "" + evt.key);
    //console.log(evt.target.attributes.low);
    //console.log(evt.target.attributes.high);
    if (isNumberKey(evt) && inRange(evt.target.value + "" + evt.key, evt.target.attributes.low.value, evt.target.attributes.high.value)) { return true; }
    else { return false; }
}

function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : evt.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
}

function inRange(input, low, high){
  if (low <= parseInt(input) && parseInt(input) <= high){
    return true;
  }
  else{ return false; }
}
