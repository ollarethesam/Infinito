$(document).ready(function(){
    $(document).on('click clean', '.clean-btn', function(){
        var form = $(this).closest('.drag-container')
        form.find('.form-control').val('')
        form.find(".form-control").prop('checked', false)
        form.find('.grid .grid-row').remove()
    })
})