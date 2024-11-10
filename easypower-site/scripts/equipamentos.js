let template = `<div class="equipamento">
			<p class="name">Equipamento 1</p>
			<p class="value"> 10 kw </p>
		</div>`
console.log(template)

let equipamentos = [
	{
			"nome": "equip",
			"consumo": 1
	},
	{
			"nome": "equip",
			"consumo": 1
	}
]

for (let i = 0; i < 5; i++) {
	let obj = {
	   	"nome": `equip${i}`,
	   	"consumo": (i*10)
	}
	equipamentos.push(obj)
}

let user_id = window.localStorage.getItem("id-user");
console.log("user_id")
console.log(user_id)

const params = {
	"usuario_id": user_id,
};

const options = {
	method: "POST",
	headers: {
		"Content-Type": "application/json"  // Tells the server you're sending JSON
	},
	body: JSON.stringify(params) 
};
console.log(params)


fetch( 'http://localhost:8080/equipamentos', options )
	.then( response => response.json() )
	.then( response => {
		console.log("response")
		console.log(response);
		let correctedString = response.equipamento.replace(/'/g, '"');
		let obs = JSON.parse(correctedString);
		let parent = document.querySelector(".list-equip");

		for(let i = 0; i < 5; i++) {
			let template = `<div class="equipamento">
						<p class="name">${obs[i].nome_equipamento} ${obs[i].potencia}W </p>
					</div>`

			parent.innerHTML += template;
		}
		
		// Do something with response.
	} );

