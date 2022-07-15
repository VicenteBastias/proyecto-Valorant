$.get("https://valorant-api.com/v1/agents?language=es-ES&isPlayableCharacter=true", function () {
    console.log("success valo");
})
    .done(function (resp) {
        console.log("second Success");
        for (var agente of resp.data) {
            var displayName = '';
            var description = '';
            var displayIcon = '';
            console.log(agente.description);
            $('#agentesValo').append(`<div class="col" style="padding-top:10px"><div class="card" style="width: 18rem;">
                <img src="${agente.displayIcon}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title text-black">${agente.displayName}</h5>
                        <p class="card-text text-black">${agente.description}</p>
                    </div>
                </div>
                </div>`);
        }
        
    })



    .fail(function () {
        alert("error: no se pudo conectar a la api");

    });