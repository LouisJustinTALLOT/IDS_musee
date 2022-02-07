$(document).ready(function(){
    $("#presentation_musee").click(
        function(){
            $("#video_presentation_musee").show();
            $("#video_presentation_musee").children("video").get(0).play();
            console.log($("#video_presentation_musee").children("video").get(0));
        }
    );

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
});