$(document).ready(function () {
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect:"bounceIn",

        },
        out:{
            effect:"bounceOut",

        }
    })
    // siri wave cofiguration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 400,
        style:"ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
    });

    //siri wave messege animation

    $('.siri-messege').textillate({
        loop: true,
        sync: true,
        in:{
            effect:"fadeInUp",
            sync: true

        },
        out:{
            effect:"fadeOutUp",
            sync: true

        }
    })

    // mic button click event
    $("#MicBtn").click(function () { 
        eel.ClickSound();        
        $("#Ovel").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.AllCommands()()
        
    });
});