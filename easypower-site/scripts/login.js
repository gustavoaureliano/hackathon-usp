

let btn = document.querySelector("#btnLogin");

btn.addEventListener("click", () => {
	let nomeInput = document.querySelector("#nome").value
	let senhaImput = document.querySelector("#senha").value

	const params = {
		"nome": nomeInput,
		"senha": senhaImput 
	};
	const options = {
		method: "POST",
		headers: {
			"Content-Type": "application/json"  // Tells the server you're sending JSON
		},
		body: JSON.stringify(params) 
	};
	console.log(params)
	
	fetch( 'http://localhost:8080/login', options )
		.then( response => response.json() )
		.then( response => {
			if (response.message != 0) {
				console.log(response);
				window.localStorage.setItem('id-user', response.message);
				window.location.replace("/");
			}
			// Do something with response.
		} );
})



