//page assign
pagename = ''
function getCookie(name='csrftoken') {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function clearBox(elementID)
{
    document.getElementById(elementID).innerHTML = "";
}
const csrftoken = getCookie()
function check() {
    $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            type: 'POST',
            url: '/gui/page/',
            cache:'false',
            data: {},
            dataType: 'json',
            success: function (data) {
                if (data.page !== pagename) {
                    pagename = data.page
                    document.querySelector('#gui_content').innerHTML = ''
                    get_content(data.page)
                    // location.reload();
                }
            }

        })
    }
setInterval(check,300);

function get_content(page) {
    $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            type: 'POST',
            url: '/gui/html/',
            cache:'false',
            data: {page: page},
            dataType: 'json',
            success: function (data) {
                document.querySelector('#gui_content').innerHTML = data.content
            }

        })
    }