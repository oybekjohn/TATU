$(document).ready(function() {
    var max_fields      = 50; //maximum input boxes allowed
    var wrapper   		= $(".input_fields_wrap"); //Fields wrapper
    var add_button      = $(".add_field_button"); //Add button ID
    var add_input       = $(".add_field_input");
    var add_input       = $(".add_field_label");

    var file_from       = $(".file_from")
    var saqlash_btn     = $("#saqlash_btn");
    var add_clone       = $(".add_clone");
    var clone_form      = $(".clone_form");
    
    var x = 1; //initlal text box count
    $(add_button).click(function(e){ //on add input button click
        e.preventDefault();
        if(x < max_fields){ //max input box allowed
            x++; //text box increment
            $(wrapper).append('<div style="padding:10px"><label style="margin-right: 10px" for="file" id="file" >Shartnoma nomi</label><input type="text" name="mytext[]"/><input type="file" name="mytext[]"/><a href="#" class="remove_field">Remove</a></div>'); //add input box
        }
    });

    $("#download").click(function(e){
        var url = $(this).attr('data')
        // e.preventDefault();
        // window.location.href = url;

        const url_parts = url.split('/')
        console.log(url)
        fetch(url).then(function(t) {
          return t.blob().then((b)=>{
            var a = document.createElement("a");
            a.href = URL.createObjectURL(b);
            a.setAttribute("download", url_parts[url_parts.length - 1]);
            a.click();
          }
          );
        });
    })
    
    $(wrapper).on("click",".remove_field", function(e){ //user click on remove text
        e.preventDefault(); $(this).parent('div').remove(); x--;
    })

    file_from.on('click',function(e) { 
         e.preventDefault()
        window.location = '{% url "account_form"%}'
    })

    saqlash_btn.on("click" , function (e) {
        e.preventDefault()
        window.location = '{% url "account"%}'
    })

    add_clone.on("click" , function(e) {
        e.preventDefault()
        clone_form.clone().insertAfter( clone_form );
    }) })