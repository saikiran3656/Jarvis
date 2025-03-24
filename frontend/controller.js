$(document).ready(function () {

    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {

        $(".siri-messege li:first").text(message);
        $('.siri-messege').textillate('start');

    }

    // Display hood
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Ovel").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
        
    }

});