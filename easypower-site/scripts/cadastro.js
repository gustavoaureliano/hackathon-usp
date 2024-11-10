let nomeInput = document.querySelector("#nome").value
let emailInput = document.querySelector("#email").value
let senhaImput = document.querySelector("#senha").value

let btn = document.querySelector("#btnCadastro");

btn.addEventListener("click", () => {
	const params = {
		"nome": nomeInput,
		"email": emailInput,
		"senha": senhaImput 
	};
	const options = {
		method: 'POST',
		body: JSON.stringify( params )  
	};
	fetch( 'http://localhost:3000', options )
		.then( response => response.json() )
		.then( response => {
			console.log(response);
			window.localStorage.setItem('id-user', response.id);
			window.location.replace("/login.html");
			// Do something with response.
		} );
})
