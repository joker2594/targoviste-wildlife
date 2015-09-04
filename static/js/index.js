$(document).ready(function() {
    $('.image').hover(
        function(){
            $(this).find('.overlay').show(); //.fadeIn(250)
        },
        function(){
            $(this).find('.overlay').hide(); //.fadeOut(205)
        }
    );
});
