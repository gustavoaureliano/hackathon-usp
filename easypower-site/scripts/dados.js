
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
			<div class="comparar">
				<div>
					Com a tarifa branca: R$ ${response.numero_tarifabranca}
				</div>
				<div class="images">
					Com a tarifa comum: R$ ${response.numero_tarifaconvencional}
				</div>
			</div>
			<div>
				<img style='display:block; width:100px;height:100px;' id='base64image' src='data:image/jpeg;base64, ${total_imagem}'/>
				<img style='display:block; width:100px;height:100px;' id='base64image' src='data:image/jpeg;base64, ${response.total_imagem}'/>
			</div>
			<div class="ai">
				<p>chatgptmethod</p>
			</div>
		`
		let parent = document.querySelector(".container-all");
		parent.innerHTML += content;
		
		// Do something with response.
	} );


