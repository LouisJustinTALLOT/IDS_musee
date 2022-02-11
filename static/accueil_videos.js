$(document).ready(function(){

    var socket = io.connect("http://" + document.domain + ":" + location.port );

    // suppress the ability to right-click (for interactive touchscreen)
    document.addEventListener('contextmenu', event => event.preventDefault());

    const NOMS_VIDEOS = [
        "presentation_musee",
        "histoire",
        "sepiolite",
        "calcite",
        "azurite",
    ]; 

    function launch_video(nom_video){
        $("#video_" + nom_video).fadeIn(3000);
        $("#video_" + nom_video).children("video").get(0).currentTime = 0;
        $("#video_" + nom_video).children("video").get(0).play();

        if (nom_video === "azurite"){
            $.ajax({
                url : "172.16.16.0/blink_led", // replace the 0
            });
        }
    }

    for (let nom_video of NOMS_VIDEOS){
        $("#" + nom_video).click(
           () => {launch_video(nom_video);}
        );


        $("#video_" + nom_video).children("video").on("ended", function(){
            $("#video_" + nom_video).fadeOut(600);
        });
    }


    $("html").click(
        function(e){
            let width = $(window).width();
            let height = $(window).height();
            let x_pos = e.pageX;
            let y_pos = e.pageY;

            let x_percent = x_pos/width;
            let y_percent = y_pos/height;

            if (x_percent<=0.1 || x_percent>=0.9 || y_percent<=0.1 || y_percent>=0.9){
                $(".one_video").hide();

                $(".one_video").each(function() {
                    let vid = $(this).children("video");
                    console.log(vid);
                    vid.get(0).pause();
                    vid.get(0).currentTime = 0;
                });
            }
        }
    );

    socket.on("launch", function (data) {
        launch_video(data.nom_video);
    });
});