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
            effect:"fadeIn",
            sequence: true

        },
        out:{
            effect:"fadeOut",
            sequence: true

        }
    })

});