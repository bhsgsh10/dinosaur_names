var callOnLoad = function() {
    $.each(questions, function(index, question){
        var container_div = "<div class='container trivia'>"
        var row_div = "<div class='row'>"
        var result_div = "<div class='result'>"
        var question_id_div = "<div class='col-md-12 question'>Question "+question['id']+":</div>"
        var question_text_div = "<div class='col-md-12'>"+question['text']+"</div>"
        var divs = [container_div, row_div, result_div, question_id_div, question_text_div]
        if (question['image'] !== "") {
            var image_div = "<div class='col-md-12 image_div'><img src="+question['image']+"></div>"
            divs.push(image_div)
        }
        var options = question['options']
        if (options.length > 0) {
            var form_div = "<div><form>"
            $.each(options, function(idx, option) {
                var option_index = idx + 1
                var question_index = index + 1
                var option_div = `<div class="radio">
                                <label><input type="radio" name="optradio" id='`+question_index+`_`+option_index+`'> `+ option +`</label>
                                </div>`
                // var radioValue = $("input[name='optradio']:checked").val();
                // if(radioValue){
                //     alert("Your are a - " + radioValue);
                // }
                
                form_div = form_div + option_div
            })
            form_div = form_div + "</form></div>"
            
            divs.push(form_div)
        }
        var whole_html = ""
        $.each(divs, function(index, div){
            whole_html = whole_html + div
        })
        var end_tags = "</div></div></div>"
        whole_html = whole_html + end_tags

        //var link_div = "<div class='col-md-12'><a href='/item/"+fruit['Id']+"' id='know_more'>Know more</a></div>"
        //var whole_html = container_div + row_div + result_div + info_div1 + info_div2 + link_div + "</div></div></div>"
        $(".header").append(whole_html)
    })
    var button_div = "<div id='submit'><button class='btn btn-primary'>Submit</button></div>"
    $(".header").append(button_div)
}


$(document).ready(function() {
    callOnLoad()
    var question_answer_map = {}
    // $('input[type=radio][name=optradio]').change(function() {
    //     myID = $(".radio").find(":radio:checked").first().attr('id');
    //     //extract question number and option index from myID
    //     var ids = myID.split("_")
    //     question_answer_map[ids[0]] = ids[1]
    //  });
    $("#submit").on('click', function(){
        $('input:radio:checked').each(function() {
            var id = $(this).attr('id')
            var ids = id.split("_")
            question_answer_map[ids[0]] = ids[1]
         })
        // make an AJAX call here to send the responses to the server
        // collect responses using the ids for which radio buttons are selected
        console.log(question_answer_map)
        $.ajax({
            type: "POST",
            url: "evaluate",
            dataType: "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(question_answer_map),
            success: function(result){
                // parse the wrong answers here
                var wrongs = result["wrong_answers"]
                wrong_answers = wrongs
                var alert_text = ""
                var count = Object.keys(wrongs).length
                
                if (count > 0) {
                    // show alert here with the wrong question numbers
                    $("#exampleModalLongTitle").text("You got some questions wrong..")
                    alert_text = ""
                    $.each(wrong_answers, function(key, value){
                        alert_text += "\n" + "Question " + key + ", You answered - " + value
                    })
                    
                    $(".modal-body").text(alert_text)
                    $(".footer-text").text("Please try again")
                    //alert(alert_text)
                } else {
                    $("#exampleModalLongTitle").text("Success!")
                    $(".modal-body").text("Congratulations! You got everything right!")
                    $(".footer-text").text("")
                    //alert("Congratulations! You got everything right!")
                }
                $("#getCode").html(result);
                $('#exampleModalCenter').modal('show')
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        })
    })

})