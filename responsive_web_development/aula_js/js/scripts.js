
	function contar(){
				
		//var campo = document.frmCad.txtMsg.value;
		var campo = document.getElementById("txtMsg").value;
		
		var palavras = campo.split(" ");
		
		palavras = palavras.length;
		
		var n = campo.length;
		
		//alert(n);
		
		document.getElementById("contador").innerHTML = n;
		document.getElementById("contador1").innerHTML = palavras;

	}