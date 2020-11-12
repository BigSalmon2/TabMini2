function suggestion() {
    var textarea = document.getElementById("context");
    var context = textarea.value; 

    var models = document.getElementById("model"); 
    var model = models.options[models.selectedIndex].value;

    var lengths = document.getElementsByName("length"); 
    var length = '';
    if (lengths[0].checked){
        length = lengths[0].value;
    }
    else{
        length = lengths[1].value;
    }


    var formData = new FormData(); 
    formData.append("context", context );
    formData.append("model", model);
    formData.append("length", length);
    fetch(
        "/gpt2",
        {
            method: "POST",
            body:formData
        }
    )
    .then(response => {
        if (response.status == 200){
            return response
        }
        else{
            throw Error("Failed");
        }
    })
    .then(response => response.json())
    .then(response => {
        var items = document.getElementsByClassName("item");

        for (let index = 0; index < items.length; index++) {
            items[index].innerHTML = response[index];
        }
    })
    .catch(e => {
        var item = document.getElementsByClassName("item")[0];
        item.innerHTML=e;
    })
}

function concat(newText) {
    var context = document.getElementById("context");
    var text = context.value;
    text += newText; 

    context.value = text;
    clearSelect();
}

function clearSelect() {
    var items = document.getElementsByClassName("item");
    for (let index = 0; index < items.length; index++) {
        items[index].innerHTML = "";
    }
}