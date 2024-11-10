updateOption();

function updateOption() {
	let btnLogin = `
			<a class="btn-round-small" href="login.html">
				<p>faça seu login</p>
			</a>
	`
	let btnCadastro = `
			<a class="btn-round-small" href="cadastro.html">
				<p>faça seu cadastro</p>
			</a>
	`

	let btnEquipamentos = `
			<a class="btn-round-small" href="equipamentos.html">
				<p>Ver meus equipamentos</p>
			</a>
	`
	let parentDiv = document.querySelector("#buttons")
	id_user = window.localStorage.getItem('id-user');
	if (id_user === undefined || id_user === null) {
		parentDiv.innerHTML = btnLogin + btnCadastro 
	} else {
		parentDiv.innerHTML = btnEquipamentos  	
	}
	console.log("id-user is:");
	console.log(id_user);
}
