$promptForm = $('#prompt-form');
$promptInputs = $('input');
$promptLabels = $('label');

counter=0

$promptForm.on('submit', validate_form);

function validate_form(event) {
    originalEvent = event;
    if (counter = 0){
        event.preventDefault();
    }
    errorlog = false
    for (let input of $promptInputs.get()){
        if (input.value === ''){
            errorlog = true;
            input.placeholder = "INPUT REQUIRED"
        }
    }
    if (errorlog === false){
        counter = 1;
        $(this).trigger(originalEvent);
    }
}