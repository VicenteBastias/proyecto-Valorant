const btn = document.querySelector(".switch");
const theme = document.querySelector("#dark-theme");

btn.addEventListener("click", function() {
  if (theme.getAttribute("href") == "{% static 'styles.css' %}") {
    theme.href = "{% static 'modoOscuro.css' %}";
  } else {
    theme.href = "{% static 'styles.css' %}";
  }
});