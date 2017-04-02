$('.email').on('click', function () {
    var email = $(this).attr('email');
    $('#modal-body').html(email);
});