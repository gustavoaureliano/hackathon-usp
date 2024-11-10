let listPeriodos = []

// for (let i = 0; i < 5; i++) {
// 	let periodo = {
// 		"inicio": `${18+i+1}:00`,
// 		"fim": `${19+i+1}:00`
// 	}
// 	listPeriodos.push(periodo)
// }

let templatePerido = `
	<div>
	 20:30 - 22:30
	</div>
`
let btnAddPeriodo = document.querySelector("#btnAddPeriodos");
let btnAddEquip = document.querySelector("#btnAddEquip");

let user_id = window.localStorage.getItem("id-user");

let objteste;

btnAddEquip.addEventListener("click", () => {
	
	let nome = document.querySelector("#nome").value
	let fabricante = document.querySelector("#fabricante").value
	let potencia = document.querySelector("#potencia").value

	const params = {
		"usuario_id": user_id, 
		"nome_equipamento": nome,
		"nome_fabricante": fabricante,
		"potencia": potencia,
		"rigidez_de_horario": 1,
		"periodos": listPeriodos,
		"eh_input_do_usuario": 1
	};
	
	const options = {
		method: "POST",
		headers: {
			"Content-Type": "application/json"  // Tells the server you're sending JSON
		},
		body: JSON.stringify(params) 
	};
	console.log(params)
	
	objteste = params;
	
	fetch( 'http://localhost:8080/api/equipamento', options )
		.then( response => response.json() )
		.then( response => {
			console.log(response);
			window.location.replace("/equipamentos.html");
			//window.location.replace("/");
		} );
})

btnAddPeriodo.addEventListener("click", () => {
	let inicioInput = document.querySelector("#inicio").value
	let fimInput = document.querySelector("#fim").value
	let periodo = {
		"inicio": inicioInput,
		"fim": fimInput
	}
	listPeriodos.push(periodo)
	updatePeriodos();
})


function updatePeriodos() {
	let parentDiv = document.querySelector(".periodos")
	parentDiv.innerHTML = "";
	for(let i = 0; i < listPeriodos.length; i++) {
		let templatePeriodo = `
			<div>
			${listPeriodos[i].inicio} - ${listPeriodos[i].fim}
			</div>
			`
		parentDiv.innerHTML += templatePeriodo
	}
}
