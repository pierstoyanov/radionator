// $("#a").each(function() {
//     if (this.pathname == window.location.href) {
//         $(this).addClass("active");
//     }
// });
//TODO Active current page in navbar

$(document).ready(function(e){
         var pathname = window.location.pathname;
         atag = $('.dropdown a[href="'+pathname+'"]'); "navbar-item"
         atag.parent().addClass("active");
       });