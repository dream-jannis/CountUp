function verify_stroke(stroke_id){
    $.ajax({
      url: 'verify_stroke',
      method: 'POST',
      data: {
        "stroke_id": String(stroke_id),
      },
      success: function(){ 
        alert('success!');
      },
      error: function(){
        alert('error!');
      }
    });
}