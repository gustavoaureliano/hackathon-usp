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

const options = {
	method: 'GET',
};

fetch( 'http://localhost:3000', options )
	.then( response => response.json() )
	.then( response => {
		let gotlist = [
			{
					"nome": "equip",
					"consumo": 10
			},
			{
					"nome": "equip",
					"consumo": 12
			}
		]

		console.log(gotlist);
		let parent = document.querySelector(".list-equip")

		for(let i = 0; i < 5; i++) {
			let template = `<div class="equipamento">
						<p class="name">${gotlist[i].nome} ${gotlist[i].consumo}w </p>
					</div>`

			parent.innerHTML += template
		}
		
		// Do something with response.
	} );

