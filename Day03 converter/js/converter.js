
var select_from = document.getElementById("from");
var select_to = document.getElementById("to");

function showHide() {
    var select = document.getElementById("whattoconvert");
    var selected = select.options[select.selectedIndex].value;
    

    var options = select_from.options;
    for (var i = 0; i < options.length; i++) {
        options[i].style.display = "none";
    }

    if (selected == "Weight") {
        document.getElementById("m").style.display = "block";
        document.getElementById("cm").style.display = "block";
        document.getElementById("mm").style.display = "block";
        document.getElementById("km").style.display = "block";
        document.getElementById("mi").style.display = "block";
        document.getElementById("yd").style.display = "block";
        document.getElementById("ft").style.display = "block";
        document.getElementById("in").style.display = "block";
    }
}

function convert() {
    var valueToConvert = parseFloat(document.getElementById("valueToConvert").value);
    var fromUnit = select_from.options[select_from.selectedIndex].value;
    var toUnit = select_to.options[select_to.selectedIndex].value;
    var result = 0;

    if (fromUnit === "m" && toUnit === "cm") {
        result = valueToConvert * 100;
    } else if (fromUnit === "cm" && toUnit === "m") {
        result = valueToConvert / 100;
    }

    document.getElementById("result").textContent = "Result: " + result;
}
