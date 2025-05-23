const form = document.getElementById("chat-form");
const chatBox = document.getElementById("chat-box");
const imagemInput = document.getElementById("imagem");

form.addEventListener("submit", async function(e) {
    e.preventDefault();
    const pergunta = document.getElementById("pergunta").value;
    if (!pergunta && imagemInput.files.length === 0) return;

    if (pergunta) {
        chatBox.innerHTML += `<div class="user"><b>Você:</b> ${pergunta}</div>`;
        document.getElementById("pergunta").value = "";

        const resposta = await fetch("/perguntar", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({pergunta})
        }).then(res => res.json());

        chatBox.innerHTML += `<div class="bot"><b>Alici:</b> ${resposta.resposta}</div>`;
    }

    if (imagemInput.files.length > 0) {
        const formData = new FormData();
        formData.append("imagem", imagemInput.files[0]);

        const resposta = await fetch("/classificar", {
            method: "POST",
            body: formData
        }).then(res => res.json());

        chatBox.innerHTML += `<div class="bot">🔍 <b>Classe:</b> ${resposta.classe} | <b>Confiança:</b> ${resposta.confianca}</div>`;
        imagemInput.value = '';
    }

    chatBox.scrollTop = chatBox.scrollHeight;
});
