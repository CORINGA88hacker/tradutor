
async function gerarImagem() {
  const prompt = document.getElementById('prompt').value.trim();
  const imagemDiv = document.getElementById('imagem');
  if (!prompt) {
    imagemDiv.innerHTML = "<p>⚠️ Por favor, digite uma descrição.</p>";
    return;
  }

  imagemDiv.innerHTML = "<p>⏳ Gerando imagem usando IA pública...</p>";

  // Usando API pública com prompt embutido como parte do nome (fake endpoint de exemplo)
  const encodedPrompt = encodeURIComponent(prompt);
  const url = `https://image.pollinations.ai/prompt/${encodedPrompt}`;

  imagemDiv.innerHTML = `<img src="${url}" alt="Imagem gerada com IA">`;
}
