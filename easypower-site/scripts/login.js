
let nomeInput = document.querySelector("#nome").value
let senhaImput = document.querySelector("#senha").value

let btn = document.querySelector("#btnLogin");

btn.addEventListener("click", () => {
	const params = {
		"nome": nomeInput,
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
			window.location.replace("/");
			// Do something with response.
		} );
})



