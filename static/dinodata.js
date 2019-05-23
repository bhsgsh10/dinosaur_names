var callOnLoad = function() {
    var dino = dinos[dino_id]
    var name_div = "<div class='name'><h2>"+dino["name"]+"</h2></div>"
    var mn_div = "<div class='col-md-12' id='mn'><div id='found_in'>means <span class='found'>"+dino["meaning"]+"</span></div></div>"
    var container_div = "<div class='container dino'>"
    var row_div = "<div class='row' id='dino-content'>"
    var results_div = "<div class='result'>"
    var image_div = "<div class='col-md-12' id='image_div'><img class='center-block' src='"+dino["image"]+"'></img></div>"
    var origin_div = "<div class='col-md-12' id='origin'><div><span class='found'> Origin of name: </span> "+dino["origin"]+"</div></div>"
    var funfacts_div = "<div class='col-md-12' id='fun-facts'><div><span class='found'> Fun facts: </span> "+dino["details"]+"</div></div>"
    var end_divs = "</div></div>"
    var whole_html = name_div + mn_div + container_div + row_div + image_div + origin_div + funfacts_div + end_divs
    if (dino_id == 9) {
        // add a button that allows the user to go to the quiz page
       var button = "<div id='quiz-button'><a href='/trivia' class='btn btn-primary'>Take the quiz</a></div>"
        whole_html += button
    }
    $("#placeholder").append(whole_html)

    // set up paginated links
    $.each(dinos, function(index, dino){
        var page_num = index + 1
        var link = ""
        if (dino_id == index) {
            link = "<a href=/dinodata/"+index+" class='active'>"+page_num+"</a>"
        } else {
            link = "<a href=/dinodata/"+index+">"+page_num+"</a>"
        }
        $(".pagination").append(link)
    })
    // console.log(dino_id)
    // // if the user is on the last dinosaur, show Take Quiz button, else hide it
    // if (dino_id == 9) {
    //     // add a button that allows the user to go to the quiz page
    //     var button = "<a href='localhost:5000/trivia' class='btn btn-primary'>Take the quiz</a>"
    //     $("#placeholder").append(button)
    // }
}

$(document).ready(function() {
    callOnLoad()
})