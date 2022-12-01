async function updateCart(data){
  const response = await fetch("/updateCart", {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(data),
  });
}

var inputs = document.getElementsByClassName('quant-inp');
var hiddens = document.getElementsByClassName('hidden-inp');

for (let i = 0; i < inputs.length; i++) {
  var input = inputs[i];
  input.addEventListener("change", () => {
    var items = document.getElementsByClassName('item-price');
    var data = {};
    var total = 0;
    for (let i = 0; i < items.length; i++){
      var price = parseFloat(items[i].innerHTML.split(" ")[0]);
      var amount = parseFloat(inputs[i].value);
      if (isNaN(amount)){
        amount = 0;
      }

      var total = total + price * amount;
      data[hiddens[i].value] = amount;
    }
    
    var delivery = parseFloat(document.getElementById("del").innerHTML.split(" ")[0]);
    console.log(delivery)

    var proc = document.getElementById("proc")
    if (cpn == undefined){
      var cpn = 100
    } else {
      var cpn = parseFloat(proc.innerHTML)
      console.log(cpn)
      document.getElementById("cpn").innerHTML = `- ${Math.round((total + delivery) * (cpn / 100)*100)/100} DKK`
    }

    var all = (total + delivery) * (cpn / 100)
    var tax = all*0.26
    console.log("all price", all, "tax", tax)

    document.getElementById("tot").innerHTML = `${Math.round(total*100)/100} DKK`;
    document.getElementById("tax").innerHTML = `${Math.round(tax*100)/100} DKK`;
    document.getElementById("all").innerHTML = `${Math.round((all + tax)*100)/100} DKK`;

    updateCart(data);
  });
}
