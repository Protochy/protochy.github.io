// add custom js in this file

document.querySelectorAll('video').forEach(function(vid) {
    vid.onmouseover = function() {
      this.play();
    }
    vid.onmouseout = function() {
      this.load(); // stop and show poster
    }
  });

  var isInIframe = (window.location !== window.parent.location);

  $(document).ready(function() {

    var isInIframe = (window.location !== window.parent.location);
    var offsetAdjustment = 0;  // -100 or whatever value you want to scroll up by
    let timeout;
    
    function showBox(targetId) {
        clearTimeout(timeout);
        $("#" + targetId).show();
    }
    
    function scheduleHideBox(targetId) {
        clearTimeout(timeout);
        timeout = setTimeout(function() {
            $("#" + targetId).hide();
        }, 250); // 250ms grace period
    }

    $("a.popup-link").on("mouseenter", function() {
        const targetId = $(this).data('target');
        console.log(`SHOWING ${targetId}`)
        showBox(targetId);
    });

    $("a.popup-link, .pbox").on("mouseleave", function() {
        const targetId = $(this).hasClass('popup-link') ? $(this).data('target') : $(this).attr('id');
        console.log(`HIDING ${targetId}`)
        scheduleHideBox(targetId);
    });

    $(".pbox").on("mouseenter", function() {
        clearTimeout(timeout);
    });

});

function loonify(h){
    //console.log("SEEING")
    // console.log(h)
   // $(`#${h}`).show()
    //var cw = document.getElementById(h).contentWindow;
    //cw.scrollBy(0, 100);
}