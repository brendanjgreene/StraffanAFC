    //Set the stuff we want to be able to use in javascript, but not display in the browser window invisible

$patients = $("#patients");

$(document).ready(function () {
    $patients.addClass("hidden")
});

$(document).ajaxStart(function() {
    $patients.removeClass("hidden")
});
$(document).ajaxStop(function() {
    $patients.removeClass("hidden")
});