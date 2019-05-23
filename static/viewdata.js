var callOnLoad = function() {
    $.each(dinos, function(index, dino){
        //build the HTML for each of the search results
        var idx = dino["id"] - 1
        var container_div = "<div class='container dino'>"
        var row_div = "<div class='row'>"
        //var result_div = "<div class='result'>"
        var image_div = "<div class='col-md-4 image_div'><img src="+dino['image']+" alt=No image found></div>"
        var info_div1 = "<div class='col-md-8'><div class='name'><h2>"+ dino['name'] +"</h2></div>"
        var info_div2 = "<div class='description'><p>"+ dino['description'] +"</p></div>"
        var link_div = "<div class='know-more'><a href='/dinodata/"+idx+"'</a>Know more</div>"
        var whole_html = container_div + row_div + image_div + info_div1 + info_div2 + link_div + "</div></div>"
        $(".header").append(whole_html)
    })









    // var container_div = "<div class='container tab'>"
    // var row_div = "<div class='row'>"
    // var column_div = "<div class='col-md-12'>"
    // var table_div = "<table class='table'><thead><tr><th scope='col'>ID</th><th scope='col'>Dinosaur Name</th><th scope='col'>Period</th><th scope='col'>Found in</th><th scope='col'>Height</th><th scope='col'>Weight</th></tr></thead><tbody>"
    // $.each(dinos, function(index, dino){
    //     var idx = dino["id"] - 1
    //     var tr_tag = "<tr><th scope='row'>"+dino["id"]+"</th>"
    //     var link = "<div><a href='/dinodata/"+idx+"'</a>"+dino["name"]+"</div>"
    //     var name_tag = "<td>"+link+"</td>"
    //     var period_tag = "<td>"+dino["period"]+"</td>"
    //     var found_tag = "<td>"+dino["found"]+"</td>"
    //     var height_tag = "<td>"+dino["height"]+"</td>"
    //     var weight_tag = "<td>"+dino["weight"]+"</td>"
    //     var tr_end = "</tr>"
    //     var table_element_tag = tr_tag + name_tag + period_tag + found_tag + height_tag + weight_tag + tr_end
    //     table_div = table_div + table_element_tag
    // })
    // var end_tags = "</body></table></div></div></div>"
    // var whole_html = container_div + row_div + column_div + table_div + end_tags
    // $("#buttons").append(whole_html)
}

$(document).ready(function() {
    callOnLoad()
})