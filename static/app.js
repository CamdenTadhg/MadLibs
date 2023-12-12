$promptForm = $('#prompt-form');
$promptInputs = $('input');
$promptLabels = $('label');

counter=0
helperText = {'adjective': 'Describing word. Example: colorful', 'adverb': 'word describing how you do something. Often ends in "ly". Example: quickly','body_part': 'Example: toe', 'building': 'Example: library', 'color': 'Example: blue', 'comparative_adjective': 'describing word ending in "er". Example: faster', 'gerund': 'Verb ending in "ing". Example: running', 'living_thing': 'Example: dog', 'name': 'Example: Austin', 'noun': 'Person, place, or thing. Example: rose', 'past_tense_verb': 'action word that already happend. Often ends in "ed". Example: walked', 'place': 'Example: town', 'plural_noun': 'More than one person, place, or thing. Example: roses', 'sound': 'Example: screech', 'verb': 'action word. Example: run'}

$promptForm.on('submit', validate_form);
$promptLabels.on('mouseover', show_helper_text);

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

// function show_helper_text(event){
//     console.log('entering show helper text');
//     for (let [key, value] of Object.entries(helperText)){
//         if (event.target.innerText.startsWith(key)) {
//             event.target.
//         }
//     }
// }