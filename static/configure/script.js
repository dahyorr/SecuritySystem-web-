$("button").click(
    function(){
        const value = $(this).val();
        if(value === "manage-users"){
            $("#manage-users").css("display", "block");
            $('.fa-times').css('display', 'block');
            $('#rfid-manage').css('display', 'none');
            $('#sysinfo').css('display', 'none');
            $('#restart').css('display', 'none');
            $('#change-pin').css('display', 'none');
            $('#maintain').css('display', 'none');

        }
        else if(value === "exit"){
           $("#manage-users").css("display", "none");
           $("#rfid-manage").css("display", "none");
           $(".fa-times ").css("display", "none");
           $("#sysinfo ").css("display", "none");
           $('#restart').css('display', 'none');
           $('#change-pin').css('display', 'none');
           $('#maintain').css('display', 'none');

        }
        else if(value === "rfid-manage"){
           $("#manage-users").css("display", "none");
           $(".fa-times ").css("display", "block");
           $("#rfid-manage").css("display", "block");
           $("#sysinfo").css("display", "none");
           $('#restart').css('display', 'none');
           $('#change-pin').css('display', 'none');
           $('#maintain').css('display', 'none');

        }
        else if(value === "sysinfo"){
           $("#manage-users").css("display", "none");
           $(".fa-times ").css("display", "block");
           $("#rfid-manage").css("display", "none");
           $("#sysinfo").css("display", "block");
           $('#restart').css('display', 'none');
           $('#change-pin').css('display', 'none');
           $('#maintain').css('display', 'none');

        }
        else if(value === "restart"){
           $("#manage-users").css("display", "none");
           $(".fa-times ").css("display", "block");
           $("#rfid-manage").css("display", "none");
           $("#sysinfo").css("display", "none");
           $('#restart').css('display', 'block');
           $('#change-pin').css('display', 'none');
           $('#maintain').css('display', 'none');



        }
        else if(value === "change-pin"){
           $("#manage-users").css("display", "none");
           $(".fa-times ").css("display", "block");
           $("#rfid-manage").css("display", "none");
           $("#sysinfo").css("display", "none");
           $('#restart').css('display', 'none');
           $('#change-pin').css('display', 'block');
           $('#maintain').css('display', 'none');
        }
        else if(value === "maintain"){
           $("#manage-users").css("display", "none");
           $(".fa-times ").css("display", "block");
           $("#rfid-manage").css("display", "none");
           $("#sysinfo").css("display", "none");
           $('#restart').css('display', 'none');
           $('#maintain').css('display', 'block');
           $('#change-pin').css('display', 'none');

        }
    }

    );






