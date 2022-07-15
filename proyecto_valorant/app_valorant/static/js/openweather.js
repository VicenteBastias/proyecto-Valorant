navigator.geolocation.getCurrentPosition((position) => {
    console.log(position.coords.latitude, position.coords.longitude);
    $.get( `https://api.openweathermap.org/data/2.5/weather?lat=${position.coords.latitude}&lon=${position.coords.longitude}&units=metric&appid=c89034788035313982116048a28f8e4b`, function() {
    console.log( "success" );
    $('#map-container-google-2').append(`<iframe src="https://maps.google.com/maps?q=${position.coords.latitude},${position.coords.longitude}" frameborder="0"
    style="border:0" allowfullscreen></iframe>`)
})
.done(function(data) {
    console.log( "second success" );
    console.log(JSON.stringify(data.main.temp));
    $('#temperatura').append(`Temperatura: ${data.main.temp} c°`)
})
.fail(function(error) {
    console.log(error);
});
if('geolocation' in navigator) {
    console.log("U w U")
    
} else {
    console.log("O w O")
}
});
