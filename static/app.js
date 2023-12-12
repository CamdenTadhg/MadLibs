$promptForm = $('#prompt-form');
$promptInputs = $('input');
$newStoryForm = $('#new-story-form');
$storyText = $('#story-text');
$partsOfSpeech = $('#parts-of-speech');
$storyName = $('#story-name');

let counter = 0;

$promptForm.on('submit', validate_prompt_form);
$newStoryForm.on('submit', validate_new_story_form);

function validate_prompt_form(event) {
    for (let input of $promptInputs.get()){
        if (input.value === ''){
            event.preventDefault();
            input.placeholder = "INPUT REQUIRED"
        }
    }
}

function validate_new_story_form(event) {
    if ($storyName[0].value === '' || $storyName[0].value === undefined){
        event.preventDefault();
        $storyName[0].placeholder = "INPUT REQUIRED";
    }
    if ($storyText[0].value === '' || $storyText[0].value === undefined){
        event.preventDefault();
        $storyText[0].placeholder = "INPUT REQUIRED";
    }
    if ($partsOfSpeech[0].value === '' || $partsOfSpeech[0].value === undefined){
        event.preventDefault();
        $partsOfSpeech[0].placeholder = "INPUT REQUIRED";
    }
}