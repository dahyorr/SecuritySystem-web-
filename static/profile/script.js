
$("button").click(
    function(){
        const value = $(this).val();
        if(value === "edit-profile"){
            $("#edit-profile").css("display", "block");
            $('#edit-password').css('display', 'none');
            }
        else if(value === "change-password"){
            $("#edit-password").css("display", "block");
            $('#edit-profile').css('display', 'none');
            }
        }
)

