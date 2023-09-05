function verify_stroke(stroke_id, btn_ele, profile_pic){
    var div_element = document.getElementById(`div_ele_${stroke_id}`)
    var vote_element = document.getElementById(`ele_vote_${stroke_id}`)
    $.ajax({
      url: 'verify_stroke',
      method: 'POST',
      data: {
        "stroke_id": String(stroke_id),
      },
      success: function(){ 
        div_element.classList.remove("strokes_on_reservation");
        div_element.classList.add("strokes_on_reservation_remaining");
        btn_ele.style.display = "none";
        var vote_count = parseInt(vote_element.textContent.split(" ")[1])
        vote_element.textContent = `Votes: ${vote_count + 1}`
        addElement(stroke_id, profile_pic)
      },
      error: function(){
        alert('error!');
      }
    });
}


function addElement(stroke_id, profile_pic) {
  var img = document.createElement("img");
  img.setAttribute("data-bs-toggle","tooltip");
  img.setAttribute("data-bs-placement","top");
  img.setAttribute("data-bs-title","current_user");
  img.style.cssText = "max-height: 30px; border-radius: 50%; margin: 10%;"
  img.src = `static/profile_pictures/${profile_pic}`

  document.getElementById(`profile_picture_section_${stroke_id}`).appendChild(img);
}