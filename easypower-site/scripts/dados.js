
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


fetch( 'http://localhost:8080/api/output', options )
	.then( response => response.json() )
	.then( response => {
		console.log("response")
		console.log(response);
		let content = `
			<h1>Relatório de consumo diário</h1>
			<div class="comparar">
				<p>
					Com a tarifa branca: ${response.numero_tarifabranca.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
					-> Mensalmente ${(response.numero_tarifabranca*30).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
				</p>
				<p >
					Com a tarifa comum: ${response.numero_tarifaconvencional.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
					-> Mensalmente ${(response.numero_tarifaconvencional*30).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' })}
				</p>
			</div>
			<div class="images">
				<img id='base64image' src='data:image/jpeg;base64, ${response.equipamento_imagem}'/>
				<img id='base64image' src='data:image/jpeg;base64, ${response.total_imagem}'/>
			</div>
			<div class="ai">
				<p>${
					response.mensagem_maritaka.substring()
				}</p>
			</div>
		`
		console.log(content)
		let parent = document.querySelector(".container-all");
		parent.innerHTML = content;
		
		// Do something with response.
	} );


