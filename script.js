var listOfButtons = ["default.png", "green.png", "purple.png", "red.png", "blue.png"];
var index = 1;


function updateValue() {
    var slideShow = document.getElementById("themeImage");
    var currentValue = listOfButtons[index];
    var newValue = currentValue.replace(/(\d+)/, function(match, num) {
        return String(parseInt(num) + 1);
    });
    listOfButtons[index] = newValue;
    index = (index + 1) % listOfButtons.length;
    themeImage.style.transition = "opacity 0.5s";
    themeImage.style.opacity = 0;
    setTimeout(function() {
        slideShow.setAttribute("src",newValue);
        themeImage.style.opacity = 1;
      }, 200);
}

setInterval(updateValue, 2500);
