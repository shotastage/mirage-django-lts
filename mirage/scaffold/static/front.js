var modal_close = null;

try {
    modal_close = document.getElementById("modal_close");

    modal_close.addEventListener("click", function () {
        document.getElementsByClassName("modal")[0].classList.toggle("is-active");
    });
}
catch (e) {
    monthName = "unknown"
    logMyErrors(e)
}
