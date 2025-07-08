
async function gerarImagem() {
  const prompt = document.getElementById('prompt').value.trim();
  const imagemDiv = document.getElementById('imagem');
  if (!prompt) {
    imagemDiv.innerHTML = "<p>⚠️ Por favor, digite uma descrição.</p>";
    return;
  }

  imagemDiv.innerHTML = "<p>⏳ Gerando imagem...</p>";

  try {
    const response = await fetch("https://corsproxy.io/?https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer hf_***" // opcional: insira sua HuggingFace API key aqui se quiser
      },
      body: JSON.stringify({ inputs: prompt })
    });

    const blob = await response.blob();
    const imgURL = URL.createObjectURL(blob);
    imagemDiv.innerHTML = `<img src="\${imgURL}" alt="Imagem gerada">`;

  } catch (error) {
    imagemDiv.innerHTML = "<p>❌ Erro ao gerar imagem. Tente novamente mais tarde.</p>";
  }
}
