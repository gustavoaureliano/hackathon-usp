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

let nome = document.querySelector("#nome").value
let fabricante = document.querySelector("#fabricante").value
let potencia = document.querySelector("#potencia").value

let user_id = window.localStorage.getItem("id-user");

btnAddEquip.addEventListener("click", () => {
	const params = {
		"usuario_id": user_id, 
		"nome_equipamento": nome,
		"nome_fabricante": fabricante,
		"potencia": potencia,
		"rigidez_de_horario": 1,
		"periodos": listPeriodos
	};
	console.log(params)
	const options = {
		method: 'POST',
		body: JSON.stringify( params )  
	};
	fetch( 'http://localhost:3000', options )
		.then( response => response.json() )
		.then( response => {
			console.log(response);
			window.localStorage.setItem('id-user', response.id);
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
