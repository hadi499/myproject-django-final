const values = [...document.querySelectorAll('.price')]
        .map(element => element.innerText.replace('.', '').replace(',00', '')) 

total = 0
for(i = 0; i <values.length; i++){   
    total += Number(values[i]);
}


let bil = total.toString()

let reverse = bil.toString().split('').reverse().join('')
let ribuan 	= reverse.match(/\d{1,3}/g);
let bil_ribuan	= ribuan.join('.').split('').reverse().join('');     

document.getElementById("hasil").innerHTML = "Total Pendapatan = Rp. " + bil_ribuan + ",00";

        