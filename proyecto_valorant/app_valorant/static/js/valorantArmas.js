
$.get("https://valorant-api.com/v1/weapons", function () {
   console.log("success valo");
})
   .done(function (resp) {
      resp.data.sort(function (a, b) {
         if (a.shopData === null) {
            return
         }
         return a.shopData.cost - b.shopData.cost;
      });
      for (var weapon of resp.data) {
         //console.log( `${JSON.stringify(weapon)}`);
         //console.log(weapon.displayName)
         var headDamage = ''
         var bodyDamage = ''
         var legDamage = ''

         if (weapon.weaponStats === null) {
            headDamage = '0'
            bodyDamage = '0'
            legDamage = '0'
         }
         else {
            for (var rango of weapon.weaponStats.damageRanges) {
               headDamage += `${Math.round(rango.headDamage)} - `;
               bodyDamage += `${Math.round(rango.bodyDamage)} - `;
               legDamage += `${Math.round(rango.legDamage)} - `;
            }
         }
         if (headDamage.substring(headDamage.length - 1, headDamage.length) === ' ') {
            headDamage = headDamage.slice(0, -3)
         };
         if (bodyDamage.substring(bodyDamage.length - 1, bodyDamage.length) === ' ') {
            bodyDamage = bodyDamage.slice(0, -3)
         };
         if (legDamage.substring(legDamage.length - 1, legDamage.length) === ' ') {
            legDamage = legDamage.slice(0, -3)
         };
         $('#armasValo').append(`<tr>
          <td>${weapon.displayName}</td>
          <td>${weapon.shopData === null ? '' : weapon.shopData.cost}</td>
          <td>${headDamage}</td>
          <td>${bodyDamage}</td>
          <td>${legDamage}</td>
          </tr>`);
      };

   })
   .fail(function () {
      console.log("error valo");
   });
