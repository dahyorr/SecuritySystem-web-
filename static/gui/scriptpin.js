// function pinajaxget() {
//     var result="";
//     $.ajax({
//       url:"configgetpin.php",
//       async: false,
//       success:function(data) {
//          result = data;
//       }
//    });
//    return result;
//   }
//
//
//
// function pinchange(){
//   pininhtml="      "
//
//   var pin = pinajaxget()
//   if(pininhtml != pin ){
//     pininhtml=pin.concat("      ")
//
//     document.getElementById("pinin").innerHTML = pininhtml[0].concat(" ", pininhtml[1], " ", pininhtml[2], " ", pininhtml[3], " ", pininhtml[4], " ", pininhtml[5] )
//   }
//
//
//   }
// setInterval(pinchange,200);