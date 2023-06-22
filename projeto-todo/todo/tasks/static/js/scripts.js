$(document).ready(function () {

    var deleteBtn = $('.delete-btn');
    var searchBtn = $('#search-btn');
    var searchForm = $('#search-form');

    $(deleteBtn).on('click', function (e) {

        e.preventDefault();

        var dellink = $(this).attr('href');
        var result = confirm('Quer deletar esta tarefa?');

        if (result) {
            window.location.href = dellink;
        }

    });

    $(searchBtn).on('click', function () {
        searchForm.submit();
    });

});

