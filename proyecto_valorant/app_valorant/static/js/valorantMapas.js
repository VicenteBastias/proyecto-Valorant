$.get("https://valorant-api.com/v1/maps", function () {
    console.log("success valo");
})
    .done(function (resp) {
        console.log("second Success");
        for (var mapa of resp.data) {

            console.log(mapa.displayName);
            var displayName = '';
            var displayIcon = '';
            if (mapa.displayIcon !== null) {
                $('#mapasValo').append(`<div class="carousel-item">
                <img src="${mapa.displayIcon}" class="d-block w-100" alt="mapas">
                <div class="carousel-caption d-none d-md-block">
                  <h5>${mapa.displayName}</h5>
                </div>
              </div>`);
            }

        }
    })



    .fail(function () {
        console.log("error valo");
    });