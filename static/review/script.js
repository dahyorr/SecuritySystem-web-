function getCookie(name) {
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
let video = ""

$("button").click(
    function(){
        const value = $(this).val();
        if(value === "reviewVideo"){
            $("#reviewVideo").css("display", "block");
            $('#reviewLog').css('display', 'none');
            }
        else if(value === "reviewLog"){
            $("#reviewLog").css("display", "block");
            $('#reviewVideo').css('display', 'none');
            }
        }
)

const player = new Plyr('#player');
if(document.URL.indexOf("#videos") >= 0 || document.URL.indexOf("%23videos") >= 0 ){
    $('#videobtn').click();
}
    else if(document.URL.indexOf("#log") >= 0 || document.URL.indexOf("%23logs") >= 0){
$('#logbtn').click();
}


$('.video-link').on('click', function(){
    let src = $(this).data('src')
    video = $(this).data('name')
    let id = $(this).data('id')
    let videoInfo = Array.from($('.video-info'))
    $('.video-link').removeClass('active')
    $(this).toggleClass('active')
    player.source = {
        type:'video',
        sources:[{
                  src: src,
              }]
    }
    const csrftoken = getCookie('csrftoken')
    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        type: 'POST',
        url: '/review/ajax/video_info/',
        cache:'false',
        data: {
            video: video,
            id: id,
            src: src
        },
        dataType: 'json',
        success: function (data) {
            console.log(data)
            $('#videoBottom').css("display", "block")
            videoInfo[0].textContent = 'Filename: ' + video
            videoInfo[1].textContent = 'Size: ' + data.video_size
            videoInfo[2].textContent = 'Available Space: ' + data.free_space
            videoInfo[3].textContent = 'Recordings Size: ' + data.recordings_size
        }

    })
    player.play()
})

$('.download').on('click', function(){
   window.location=`video/download/${video}/`
})
$('.delete').on('click', function(){
   window.location=`video/delete/${video}/`
})