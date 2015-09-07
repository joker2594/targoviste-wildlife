$(document).ready(function() {
    $('.image').hover(
        function(){
            $(this).find('.overlay').show(); //.fadeIn(250)
        },
        function(){
            $(this).find('.overlay').hide(); //.fadeOut(205)
        }
    );

    $('#myModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var username = button.data('username');
        var description = button.data('description');
        var picture = button.data('picture');
        var profile_pic = button.data('profilepic');
        var date_posted = button.data('posted');

        // Extract info from data-* attributes
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.

        var modal = $(this);
        modal.find('.modal-post-image img').attr('src', picture);
        modal.find('.profile-pic img').attr('src', profile_pic);
        modal.find('.user-name').text(username);
        modal.find('.post-date').text(date_posted);
        modal.find('.description').text(description);


    })
});
